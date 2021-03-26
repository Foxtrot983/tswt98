from django.shortcuts import render
from django.forms import formset_factory
from .models import Input
from .forms import AddInp


def index(request):
    InputFormset = formset_factory(AddInp, extra=1)
    # request.
    if request.method == "POST":
        form = InputFormset(request.POST)
        if form.is_valid():
            count = form.total_form_count()
            for f in range(count):
                f = Input.objects.create(
                    name=form.cleaned_data[f]['name'],
                    data=form.cleaned_data[f]['data'],
                )
                f.save()
    else:
        InputFormset = formset_factory(AddInp, extra=1)
    context = {'formsets': InputFormset}
    return render(request, 'inp/index.html', context)


def output(request):
    inputs = Input.objects.all()
    return render(request, 'inp/output.html', {'inputs': inputs})
