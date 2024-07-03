from user.models import Profile

def profile(request):
    data = Profile.objects.get(user=request.user)
    print(f'data: {data}')
    return {'profile' : data}