from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Johanes W',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)