from django.shortcuts import render, redirect

from django.views import View

from .models import Award, Skill, Technology, Project, Teammate, Message, Service
# Create your views here.

class IndexPageView(View):
    def get(self, request):

        data = {
            "title": "Davronbek Nazarov Back-end Developer (Junior)",
            "about_me": """Salom men Davronbek Nazarov Back-end Developer (Junior) man. O'zbekistonning Farg'ona shahrida tug'ilganman.
                IT sohasini 2022-yildan buyon o'rganib kelaman. O'zbekistonning Top o'quv markazlaridan bo'lgan Najot Ta'lim bitiruvchisiman. 
                Najot Ta'lim o'quv markazida 8 Oy o'quv faoliyatimni olib borganman. Hozir esa o'z ustimda ishlayapman.""",

            "phone_number": "+998 (77) 317-0154",
            "email": "dav2danderson@gmail.com",
            
            "awards": Award.objects.all(),
            "skills": Skill.objects.all(),
            "technologies": Technology.objects.all(),
            "projects": Project.objects.all(),
            "teammates": Teammate.objects.all(),

            "projects_count": Project.objects.count(),
            "teammates_count": Teammate.objects.count(),
            "feedbacks_count": Message.objects.count(), 
            "services_count": Service.objects.count()

        }

        return render(request, 'index.html', context=data)
    

class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            Message.objects.create(name=name, email=email, message=message)
        
        return redirect('/')

