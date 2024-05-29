from .models import *
from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField

class MdDivisionForm(ModelForm):
    class Meta:
        model = MdDivision
        fields = ['division']

        widgets = {
            "division": TextInput(attrs={
                'autocomplete': 'off',
                'id': 'decision_input',
                'name': 'decision'
            })
        }

class md_chapterForm(ModelForm):
    class Meta:
        model = md_chapter
        fields = ['chapter']

        widgets = {
            "chapter": TextInput(attrs={
                'autocomplete': 'off',
                'id': 'chapter_input',
                'name': 'chapter'
            })
        }

class MdPeriodForm(ModelForm):
    class Meta:
        model = MdPeriod
        fields = ['period']

        widgets = {
            "period": TextInput(attrs={
                'autocomplete': 'off',
                'id': 'period_input',
                'name': 'period'
            })
        }

class MdResponsibleForm(ModelForm):
    class Meta:
        model = MdResponsible
        fields = ['responsible']

        widgets = {
            "responsible": TextInput(attrs={
                'autocomplete': 'off',
                'id': 'decision_input',
                'name': 'decision'
            })
        }

class MdMethodicalSolutionForm(ModelForm):

    id_chapter = ModelChoiceField(
        queryset=md_chapter.objects.all(),
        empty_label='',
        required=True,
    )

    id_responsible = ModelChoiceField(
        queryset=MdResponsible.objects.all(),
        empty_label='',
        required=True,
    )

    id_division = ModelChoiceField(
        queryset=MdDivision.objects.all(),
        empty_label='',
        required=True,
    )

    id_period = ModelChoiceField(
        queryset=MdPeriod.objects.all(),
        empty_label='',
        required=True,
    )

    class Meta:
        model = MdMethodicalSolution
        fields = ['id_methodical_solution', 'decision', 'note', 'marks_of_completion', 'reason_for_nonfulfillment', 'md_date']
        widgets = {
            "md_date": DateInput(attrs={
                'class': 'add_filling',
                'id': 'date',
                'name': 'date',
                'type': 'date',
                'autocomplete': 'off',
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_chapter'].label_from_instance = lambda obj: obj.chapter
        self.fields['id_responsible'].label_from_instance = lambda obj: obj.responsible
        self.fields['id_division'].label_from_instance = lambda obj: obj.division
        self.fields['id_period'].label_from_instance = lambda obj: obj.period

    def save(self, commit=True):
        mds = super().save(commit=False)
        mds.id_chapter = self.cleaned_data['id_chapter']
        mds.id_responsible = self.cleaned_data['id_responsible']
        mds.id_division = self.cleaned_data['id_division']
        mds.id_period = self.cleaned_data['id_period']
        if commit:
            mds.save()
        return mds

class Update(ModelForm):

    id_chapter = ModelChoiceField(
        queryset=md_chapter.objects.all(),
        empty_label=None,
        required=True,
    )

    id_responsible = ModelChoiceField(
        queryset=MdResponsible.objects.all(),
        empty_label=None,
        required=True,
    )

    id_division = ModelChoiceField(
        queryset=MdDivision.objects.all(),
        empty_label=None,
        required=True,
    )

    id_period = ModelChoiceField(
        queryset=MdPeriod.objects.all(),
        empty_label=None,
        required=True,
    )

    class Meta:
        model = MdMethodicalSolution
        fields = ['decision', 'note', 'marks_of_completion', 'reason_for_nonfulfillment', 'md_date']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = {'id_chapter': instance.id_chapter, 'id_responsible': instance.id_responsible, 'id_division': instance.id_division, 'id_period': instance.id_period}
            kwargs.update(initial=initial)
        super().__init__(*args, **kwargs)
        self.fields['id_chapter'].label_from_instance = lambda obj: obj.chapter
        self.fields['id_responsible'].label_from_instance = lambda obj: obj.responsible
        self.fields['id_division'].label_from_instance = lambda obj: obj.division
        self.fields['id_period'].label_from_instance = lambda obj: obj.period

    def save(self, commit=True):
        mds = super().save(commit=False)
        mds.id_chapter = self.cleaned_data['id_chapter']
        mds.id_responsible = self.cleaned_data['id_responsible']
        mds.id_division = self.cleaned_data['id_division']
        mds.id_period = self.cleaned_data['id_period']
        if commit:
            mds.save()
        return mds
