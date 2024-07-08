from user.models import Profile

def profile(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        data = Profile.objects.get(user=request.user)
        return {'profile' : data}
    return {}