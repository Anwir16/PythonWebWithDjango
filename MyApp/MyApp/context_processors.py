from user.models import Profile

def profile(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if not Profile.objects.filter(user__username = request.user.username).exists():
            Profile.objects.create(user=request.user)
        data = Profile.objects.get(user=request.user)
        return {'profile' : data}
    return {}