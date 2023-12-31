from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app_sale.models.tag import Tag
from app_sale.forms.tag_form import TagForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateListTagView(SuccessMessageMixin, CreateView):
    template_name = 'tag/create_tag.html'
    success_message = "Tag has been successfully created!"
    model = Tag
    form_class = TagForm
    success_url = '/tag-create'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TagListView(ListView):
    template_name = 'tag/tag_list.html'
    context_object_name = 'tag_list'
    model = Tag
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        tag = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(tag, self.paginate_by)

        try:
            tag = paginator.page(page)
        except PageNotAnInteger:
            tag = paginator.page(1)
        except EmptyPage:
            tag = paginator.page(paginator.num_pages)
        context['tag'] = tag
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TagDeleteView(DeleteView):
    template_name = 'tag/tag_confirm_delete.html'
    model = Tag
    success_url = '/tag/'
