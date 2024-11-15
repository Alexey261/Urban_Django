from django.shortcuts import render
from .forms import UserRegister

users = [['Vasya', 'xyz717~!@', 18]]

def sign_up_by_html(request):

    info = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if any(l[0] == login for l in users):
            err_msg = 'Пользователь уже существует'
        elif not(password == repeat_password):
            err_msg = 'Пароли не совпадают'
        elif int(age) < 18:
            err_msg = 'Вы должны быть старше 18'
        else:
            err_msg = 'Привет, '
            users.append([login, password, int(age)])

        info['error'] = err_msg
        info['user'] = [login, password, repeat_password, age]

        return render(request, 'fifth_task/registration_page.html', context=info)

    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):

    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if any(l[0] == login for l in users):
                err_msg = 'Пользователь уже существует'
            elif not (password == repeat_password):
                err_msg = 'Пароли не совпадают'
            elif int(age) < 18:
                err_msg = 'Вы должны быть старше 18'
            else:
                err_msg = 'Привет, '
                users.append([login, password, int(age)])

            info['error'] = err_msg
            info['user'] = [login, password, repeat_password, age]
            info['form'] = form

            return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html',{'form': form})


