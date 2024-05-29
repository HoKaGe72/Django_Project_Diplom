from django.shortcuts import render, redirect
from .models import md_chapter, MdMethodicalSolution, MdDivision, MdPeriod, MdResponsible
from .forms import MdDivisionForm, MdPeriodForm, MdResponsibleForm, md_chapterForm, MdMethodicalSolutionForm, Update
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import json
from django.views.generic import UpdateView
from django.contrib.auth.models import User

models_list = {
    'Md': MdMethodicalSolution.objects.all(),
    'md_chapter': md_chapter.objects.all(),
    'Md_Responsible': MdResponsible.objects.all(),
    'Md_Division': MdDivision.objects.all(),
    'Md_Period': MdPeriod.objects.all(),
}

id_list = {
    'Md': "id_methodical_solution",
    'Md_Responsible': "id_responsible",
    'Md_Division': "id_division",
    'Md_Period': "id_period",
    'md_chapter': "id_chapter"
}

def index(request):
    models_list["Md"] = MdMethodicalSolution.objects.all()
    error = ''
    if request.method == 'POST':
        MD_form = MdMethodicalSolutionForm(request.POST)
        if MD_form.is_valid():
            MD_form.save()
            return redirect('home')
        else:
            error = 'Неверный формат'

    MD_form = MdMethodicalSolutionForm()
    Md = models_list.get('Md')
    user = User.objects.get(username=request.user)
    MD_F = {
        'Md': Md,
        'MD_form': MD_form,
        'error': error,
        'user': user
    }
    return render(request, 'main/index.html', MD_F)

def chapter(request):
    models_list["md_chapter"] = md_chapter.objects.all()
    error = ''
    if request.method == 'POST':
        chapter_form = md_chapterForm(request.POST)
        if chapter_form.is_valid():
            chapter_form.save()
            return redirect('chapter')
        else:
            error = 'Неверный формат'

    MDChapter = models_list.get('md_chapter')
    chapter_form = md_chapterForm()
    user = User.objects.get(username=request.user)
    cf = {
        'MDChapter': MDChapter,
        'chapter_form': chapter_form,
        'error': error,
        'user': user
    }
    return render(request, 'main/chapter.html', cf)

def report(request):
    return render(request, 'main/report.html')

def responsible(request):
    models_list['Md_Responsible'] = MdResponsible.objects.all()
    error = ''
    if request.method == 'POST':
        responsible_form = MdResponsibleForm(request.POST)
        if responsible_form.is_valid():
            responsible_form.save()
            return redirect('responsible')
        else:
            error = 'Неверный формат'
    Md_Responsible = models_list.get('Md_Responsible')
    responsible_form = MdResponsibleForm()
    user = User.objects.get(username=request.user)
    rf = {
        'Md_Responsible': Md_Responsible,
        'responsible_form': responsible_form,
        'error': error,
        'user': user
    }
    return render(request, 'main/responsible.html', rf)


def period(request):
    models_list['Md_Period'] = MdPeriod.objects.all()
    error = ''
    if request.method == 'POST':
        period_Form = MdPeriodForm(request.POST)
        if period_Form.is_valid():
            period_Form.save()
            return redirect('period')
        else:
            error = 'Неверный формат'
    Md_Period = models_list.get('Md_Period')
    period_Form = MdPeriodForm()
    user = User.objects.get(username=request.user)
    pf = {
        'Md_Period': Md_Period,
        'period_Form': period_Form,
        'error': error,
        'user': user
    }
    return render(request, 'main/period.html', pf)


def division(request):
    models_list['Md_Division'] = MdDivision.objects.all()
    error = ''
    if request.method == 'POST':
        division_form = MdDivisionForm(request.POST)
        if division_form.is_valid():
            division_form.save()
            return redirect('division')
        else:
            error = 'Неверный формат'
    Md_Division = models_list.get('Md_Division')
    division_form = MdDivisionForm()
    df = {
        'division_form': division_form,
        'Md_Division': Md_Division,
        'error': error
    }
    return render(request, 'main/division.html', df)

@csrf_exempt
def delete_records(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode())
        checkboxValues = data.get('checkboxValues')
        NameTable = data.get('NameTable')
        model_name = models_list.get(NameTable)
        id_name = id_list.get(NameTable)
        for val in checkboxValues:
            model_name.filter(**{id_name: val}).delete()

        return JsonResponse({"result": "success"})
    else:
        return JsonResponse({"result": "error"})

class update(UpdateView):
    model = MdMethodicalSolution
    template_name = 'main/update.html'
    form_class = Update
class update_chapter(UpdateView):
    model = md_chapter
    template_name = 'main/update_spr.html'
    form_class = md_chapterForm

class update_period(UpdateView):
    model = MdPeriod
    template_name = 'main/update_spr.html'
    form_class = MdPeriodForm

class update_division(UpdateView):
    model = MdDivision
    template_name = 'main/update_spr.html'
    form_class = MdDivisionForm

class update_responsible(UpdateView):
    model = MdResponsible
    template_name = 'main/update_spr.html'
    form_class = MdResponsibleForm

def logout_view(request):
    logout(request)
    return redirect('login')
