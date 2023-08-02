from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"index.html")
def error(request):
    return render(request,'404.html')
def about(request):
    return render(request,'about.html')
def category(request):
    return render(request,'category.html')
def contact(request):
    return render(request,'contact.html')
def job_detail(request):
    return render(request,'job-detail.html')
def job_list(request):
    return render(request,'job-list.html')
def testimonial(request):
    return render(request,'testimonial.html')
