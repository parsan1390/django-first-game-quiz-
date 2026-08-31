from django.shortcuts import render
from django.contrib.auth import get_user_model
from quiz.models import Category

User = get_user_model()


def leaderboard_view(request):
    top_users = User.objects.order_by('-total_score')[:50]
    categories = Category.objects.all()
    return render(request, 'leaderboard/leaderboard.html', {
        'top_users': top_users,
        'categories': categories,
    })