from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib import messages

from django_filters.views import FilterView


class BasicAppsMixin:
    title = ''
    crud_message = 'criado'

    def get_success_message(self):
        return f'Registro {self.crud_message} com sucesso!'

    def get_title(self):
        return self.title

    def get_back_url(self):
        return self.request.META.get('HTTP_REFERER')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        context['back_url'] = self.get_back_url()
        return context


class BasicDetailView(BasicAppsMixin, DetailView):
    title_detail = ''

    def get_title_detail(self):
        return self.title_detail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_detail'] = self.get_title_detail()
        return context


class BasicListView(FilterView, BasicAppsMixin, ListView):
    pass


class BasicCreateView(BasicAppsMixin, CreateView):

    def do_create(self, form):
        self.object = form.save()

    def form_valid(self, form):
        self.do_create(form)
        messages.success(self.request, self.get_success_message())
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        try:
            self.object = None
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)

            return self.form_invalid(form)
        except Exception as e:
            return HttpResponseRedirect(self.request.path)


class BasicUpdateView(BasicAppsMixin, UpdateView):
    crud_message = 'atualizado'

    def do_update(self, form):
        self.object = form.save()

    def form_valid(self, form):
        self.do_update(form)
        messages.success(self.request, self.get_success_message())
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)

            return self.form_invalid(form)
        except Exception as e:
            return HttpResponseRedirect(self.request.path)


class BasicDeleteView(BasicAppsMixin, DeleteView):
    perform_destroy = True

    def get_extra_data(self, data):
        pass

    def do_delete(self):
        try:
            if self.perform_destroy:
                self.object.delete()
            else:
                self.object.ativo = False
                self.object.save()
        except Exception as e:
            raise Exception('Não foi possivel fazer a exclusão do registro.')

    def delete(self, request, *args, **kwargs):
        data = dict()
        self.object = self.get_object()
        try:
            self.do_delete()
            data['status'] = 'success'
            self.get_extra_data(data)

        except Exception as e:
            data['status'] = 'error'
            data['mensagem'] = str(e)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
