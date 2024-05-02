from django.urls import path

from .views import (
    update_customer_profile,
    update_freelancer_profile,
    signup,
    all_customers,
    all_freelancers,
)

urlpatterns = [
    path("signup/", signup, name="signup"),
    path(
        "update_customer_profile/<int:pk>/",
        update_customer_profile,
        name="customer_profile",
    ),
    path(
        "update_freelancer_profile/<int:pk>/",
        update_freelancer_profile,
        name="freelancer_profile",
    ),
    path(
        "all_customers/",
        all_customers,
        name="all_customers",
    ),
    path(
        "all_freelancers/",
        all_freelancers,
        name="all_freelancers",
    ),
]
