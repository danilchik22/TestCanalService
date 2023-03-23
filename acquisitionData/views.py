from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from acquisitionData.models import Order
from acquisitionData.services import update_database
from acquisitionData.tasks import update_base

# Create your views here.
class OrderView(ListView):
    model = Order
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
        