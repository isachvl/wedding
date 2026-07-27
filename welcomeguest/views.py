from django.shortcuts import render, redirect
from .forms import GuestForm
from .models import Guest


def index(request):

    ip = request.META.get("REMOTE_ADDR")

    if request.method == "POST":

        if Guest.objects.filter(ip_address=ip).exists():
            return redirect("/?registered=1")

        form = GuestForm(request.POST)

        if form.is_valid():
            guest = form.save(commit=False)
            guest.ip_address = ip
            guest = form.save(commit=False)
            guest.ip_address = ip
            guest.save()
            return redirect("/")
        else:
            print(form.errors)

    form = GuestForm()

    return render(request, "main/main.html", {
        "form": form,
        "already_registered": request.GET.get("registered"),
        "success": request.GET.get("success"),
    })

   