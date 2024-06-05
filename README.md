# PythonWebWithDjango
This is my first project using Django to create a web application with Python.
To create a web site:
1. Open folder you want to save your project on VSCode
2. Run terminal and enter code: django-admin startproject 'your_name_project'
3. Enter cd 'your_name_project'
4. Enter python manage.py migrate  
5. To run your project you enter python manage.py runserver 50001
6. To set user and password of account admin: python manage.py createsuperuser
7. To create a page 'home' to replace template example: cd 'your_name_project'
8. Then enter python manage.py startapp 'home'
9. Create new folder 'Templates' on 'home', and create file html on folder 'Templates'
10. Go to 'settings.py' in 'your_name_project' add 'home' at 'INSTALLED_APPS'
11. Go to 'views.py' at 'home' add 'def get_home(request):
                                        return render(request,'home.html')'
. Go to 'urls.py' enter 'from home import views as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home)
]'
