from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from quiz.models import Category, Quiz, Comment, CommentLike

User = get_user_model()


def home(request):
    categories = Category.objects.all()[:6]
    top_users = User.objects.order_by('-total_score')[:5]
    total_quizzes = Quiz.objects.count()

    site_comments = Comment.objects.filter(quiz__isnull=True).select_related('user').prefetch_related('likes')[:20]
    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(
            CommentLike.objects.filter(user=request.user, comment__quiz__isnull=True)
            .values_list('comment_id', flat=True)
        )

    return render(request, 'core/home.html', {
        'categories': categories,
        'top_users': top_users,
        'total_quizzes': total_quizzes,
        'site_comments': site_comments,
        'liked_ids': liked_ids,
    })


@login_required
def add_site_comment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(user=request.user, quiz=None, text=text)
    return redirect('core:home')