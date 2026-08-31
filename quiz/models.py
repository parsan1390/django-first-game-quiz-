from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, default='🎮')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'آسان'),
        ('medium', 'متوسط'),
        ('hard', 'سخت'),
    ]
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='quizzes', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    time_limit = models.PositiveIntegerField(default=10, help_text='زمان پایه به دقیقه (برای سطح متوسط)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def total_questions(self):
        return self.questions.count()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500, verbose_name='متن سوال')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'

    def __str__(self):
        return self.text[:60]


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'گزینه'
        verbose_name_plural = 'گزینه‌ها'

    def __str__(self):
        return self.text


class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='attempts', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='attempts', on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=Quiz.DIFFICULTY_CHOICES, default='medium')
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', '-started_at']
        verbose_name = 'تلاش'
        verbose_name_plural = 'تلاش‌ها'

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - {self.score}'

    @property
    def percentage(self):
        if self.total_questions == 0:
            return 0
        return round((self.score / self.total_questions) * 100)


class UserAnswer(models.Model):
    attempt = models.ForeignKey(Attempt, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'پاسخ کاربر'
        verbose_name_plural = 'پاسخ‌های کاربر'

    @property
    def is_correct(self):
        return self.selected_choice is not None and self.selected_choice.is_correct


class Comment(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت‌ها'

    def __str__(self):
        return f'{self.user.username}: {self.text[:30]}'

    @property
    def like_count(self):
        return self.likes.count()


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('comment', 'user')
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک‌ها'