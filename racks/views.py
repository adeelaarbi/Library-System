from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic
from racks.baseview import ListView
from racks.forms import SignUpForm
from racks.models import Rack, Book

# Create your views here.


def signup(request):
    # errors = []
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts-list')
    else:
        form = SignUpForm()
    return render(request, 'racks/signup.html', {'form': form})


def index(request):
    return redirect("book-list")


class RackListView(ListView):
    model = Rack
    template_name = "racks/rack_list.html"
    context_object_name = "racks"
    queryset = Rack.objects.all()


class RackDetailView(generic.DetailView):
    model = Rack
    context_object_name = "rack"
    template_name = "racks/rack_detail.html"


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "racks/books_list.html"
    queryset = Book.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("query", None)
        if query:
            return list(filter(lambda instance: str(query).lower() in instance.search(), self.queryset))
        return self.queryset