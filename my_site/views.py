from django.shortcuts import render


def the_404_error(request, excepton):
    return render(request, '404.html', status=404)
