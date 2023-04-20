from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            row_password = form.cleaned_data.get("password1")
            # 사용자 인증 담당 = 아이디와 비밀번호를 디비랑 같은지 조회
            user = authenticate(username=username, password=row_password)
            # 로그인 담당 - 로그인 후 세션 생성
            login(request, user)
            return redirect("index")
    else:  # GET 요청일 때
        form = UserForm()
    return render(request, "common/signup.html", {"form": form})