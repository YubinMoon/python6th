from django.shortcuts import render
from django.views.generic import TemplateView


class BooksModelView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context
