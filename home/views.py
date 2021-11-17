from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.models import Post
import dash_html_components as html
from home.dash_apps.finished_apps.looker_api import get_json
from home.forms import HomeForm
from home.models import Post
import pandas as pd
from django_plotly_dash import DjangoDash
import dash_table
# Create your views here.


def home(requests):
    return render(requests, 'home/welcome.html')

# def get_slug(request):
#   if request.method == "POST":
#       slug = request.POST.get("handle", None)
#       return slug


def get(request):
    template_name = 'home/welcome.html'
    form = HomeForm()
    posts = Post.objects.all().order_by('-id')

    args = {
            'form': form, 'posts': posts
        }

    return render(request, template_name, args)


def post(request):
    template_name = 'home/welcome.html'
    form = HomeForm(request.POST)
    if form.is_valid():
        post = form.save()
        post.save()

        text = form.cleaned_data['post']
        form = HomeForm()

    return render(request, template_name)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

def table(request):
    template_name = 'home/welcome.html'
    query = Post.objects.values_list('post', flat=True)
    slug = str(query[3])
    print(slug)
    slug1 = get_json(slug)

    df = pd.read_json(slug1)
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

    app.layout = html.Div(
        [
            dash_table.DataTable(
                id="table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
                style_cell=dict(textAlign="left"),
                style_header=dict(backgroundColor="paleturquoise"),
                style_data=dict(backgroundColor="lavender"),
            )
        ]
    )
