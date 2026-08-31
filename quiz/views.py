import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Quiz, Question, Choice, Attempt, UserAnswer, Comment, CommentLike

DIFFICULTY_SETTINGS = {
    'easy':   {'count': 5,  'minutes': 3, 'label': 'Easy'},
    'medium': {'count': 10,  'minutes': 3, 'label': 'Medium'},
    'hard':   {'count': 15, 'minutes': 3, 'label': 'Hard'},
}


def quiz_list(request):
    categories = Category.objects.prefetch_related('quizzes').all()
    return render(request, 'quiz/quiz_list.html', {'categories': categories})


def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    total = quiz.total_questions
    difficulties = []
    for key, conf in DIFFICULTY_SETTINGS.items():
        difficulties.append({
            'key': key, 'label': conf['label'],
            'count': min(conf['count'], total), 'minutes': conf['minutes'],
        })

    comments = quiz.comments.select_related('user').prefetch_related('likes')
    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(
            CommentLike.objects.filter(user=request.user, comment__quiz=quiz)
            .values_list('comment_id', flat=True)
        )

    return render(request, 'quiz/quiz_detail.html', {
        'quiz': quiz, 'difficulties': difficulties,
        'comments': comments, 'liked_ids': liked_ids,
    })


@login_required
def quiz_play(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'POST':
        difficulty = request.POST.get('difficulty', 'medium')
        ids_raw = request.POST.get('question_ids', '')
        question_ids = [int(x) for x in ids_raw.split(',') if x.strip()]
        questions = list(
            Question.objects.filter(id__in=question_ids, quiz=quiz).prefetch_related('choices')
        )

        attempt = Attempt.objects.create(
            user=request.user, quiz=quiz, difficulty=difficulty,
            score=0, total_questions=len(questions),
        )

        score = 0
        for q in questions:
            selected_id = request.POST.get(f'question_{q.id}')
            selected_choice = None
            if selected_id:
                try:
                    selected_choice = q.choices.get(pk=selected_id)
                    if selected_choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass
            UserAnswer.objects.create(attempt=attempt, question=q, selected_choice=selected_choice)

        attempt.score = score
        attempt.save(update_fields=['score'])

        request.user.total_score += score
        request.user.save(update_fields=['total_score'])

        return redirect('quiz:quiz_result', pk=attempt.pk)

    # ---- GET: انتخاب رندوم سوالات ----
    difficulty = request.GET.get('difficulty', 'medium')
    if difficulty not in DIFFICULTY_SETTINGS:
        difficulty = 'medium'

    all_questions = list(quiz.questions.prefetch_related('choices').all())
    count = min(DIFFICULTY_SETTINGS[difficulty]['count'], len(all_questions))
    questions = random.sample(all_questions, count)

    # به‌هم ریختن ترتیب گزینه‌های هر سوال
    for q in questions:
        q.shuffled_choices = random.sample(list(q.choices.all()), len(q.choices.all()))

    minutes = DIFFICULTY_SETTINGS[difficulty]['minutes']
    question_ids_csv = ','.join(str(q.id) for q in questions)

    return render(request, 'quiz/quiz_play.html', {
        'quiz': quiz,
        'questions': questions,
        'difficulty': difficulty,
        'time_limit_seconds': minutes * 60,
        'question_ids_csv': question_ids_csv,
    })


@login_required
def quiz_result(request, pk):
    attempt = get_object_or_404(Attempt, pk=pk, user=request.user)
    answers = attempt.answers.select_related('question', 'selected_choice').prefetch_related('question__choices')
    return render(request, 'quiz/quiz_result.html', {'attempt': attempt, 'answers': answers})


@login_required
def add_comment(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(quiz=quiz, user=request.user, text=text)
    return redirect('quiz:quiz_detail', pk=pk)


@login_required
def toggle_like(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    like, created = CommentLike.objects.get_or_create(comment=comment, user=request.user)
    if not created:
        like.delete()
    if comment.quiz_id:
        return redirect('quiz:quiz_detail', pk=comment.quiz_id)
    return redirect('core:home')