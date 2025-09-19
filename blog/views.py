from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm   # فورم إنشاء مستخدم جديد
from django.contrib import messages                      # للرسائل


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # تقدر تحفظ البيانات في قاعدة البيانات أو تبعتها على الإيميل
        print(f"Name: {name}, Email: {email}, Message: {message}")

        return HttpResponse("<h2>شكراً لتواصلك معنا! سنرد عليك قريباً.</h2>")
    return render(request, "blog/contact.html")


def home(request):
    posts = Post.objects.all().order_by('-published_date')  # جلب كل البوستات
    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # ما تحفظش دلوقتي
            post.author = request.user      # اربطه بالمستخدم الحالي
            post.save()                     # احفظ دلوقتي
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # إنشاء المستخدم
            username = form.cleaned_data.get("username")
            messages.success(request, f"تم إنشاء الحساب {username} بنجاح ✅")
            return redirect("login")  # بعد التسجيل يروح لصفحة تسجيل الدخول
        else:
            print("Form is not valid")
            print(form.errors)  # يطبع الأخطاء في الكونسول
            messages.error(request, "حدث خطأ أثناء التسجيل. يرجى التحقق من البيانات.")
    else:
        form = UserCreationForm()

    return render(request, "blog/register.html", {"form": form})
