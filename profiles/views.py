from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import CustomerProfile, FreelancerProfile


def signup(request):
    """Регистрация пользователя с выбором роли"""

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data["role"]
            if role == "customer":
                try:
                    customer_profile = CustomerProfile.objects.create(
                        user_id=user.id,
                        name=user,
                        order_description="Order_description",
                        company="Default Company",
                    )
                    return redirect("customer_profile", pk=customer_profile.id)
                except Exception as e:
                    return render(
                        request,
                        "error.html",
                        {"message": f"Error creating customer profile: {str(e)}"},
                    )
            elif role == "freelancer":
                try:
                    freelancer_profile = FreelancerProfile.objects.create(
                        user_id=user.id,
                        name=user,
                        contact_info="contact_info",
                        experience=0,
                    )
                    return redirect("freelancer_profile", pk=freelancer_profile.id)
                except Exception as e:
                    return render(
                        request,
                        "error.html",
                        {"message": f"Error creating freelancer profile: {str(e)}"},
                    )
            login(request, user)
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def update_customer_profile(request, pk):
    """Изменение данных заказчика"""

    profile = get_object_or_404(CustomerProfile, pk=pk)

    if request.method == "POST":
        profile.company = request.POST.get("company")
        profile.name = request.POST.get("name")
        profile.order_description = request.POST.get("order_description")
        profile.save()

        messages.success(request, "Profile updated successfully")
        return redirect("customer_profile", pk=profile.pk)

    return render(request, "customer_profile.html", {"profile": profile})


def update_freelancer_profile(request, pk):
    """Изменение данных исполнителя"""

    profile = get_object_or_404(FreelancerProfile, pk=pk)

    if request.method == "POST":
        profile.name = request.POST.get("name")
        profile.contact_info = request.POST.get("contact_info")
        profile.experience = request.POST.get("experience")
        profile.save()

        messages.success(request, "Profile updated successfully")
        return redirect("freelancer_profile", pk=profile.pk)
    return render(request, "freelancer_profile.html", {"profile": profile})


def all_customers(request):
    """Вывод всех заказчиков"""

    customers = CustomerProfile.objects.all()
    return render(request, "all_customers.html", {"customers": customers})


def all_freelancers(request):
    """Вывод всех фрилансеров"""

    freelancers = FreelancerProfile.objects.all()
    return render(request, "all_freelancers.html", {"freelancers": freelancers})
