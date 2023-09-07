from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import markdown2
from django import forms
import random

from . import util


class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea())

    def clean_new_title(self):
        new_title = self.cleaned_data["new_title"]
        if util.get_entry(new_title) != None:
            raise forms.ValidationError("Entry Exists!!!")
        return new_title


class EditEntryForm(forms.Form):
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(util.get_entry(title="title")),
        required=True,
    )


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def details(request, title):
    content = util.get_entry(title)
    if content != None:
        return render(
            request,
            "encyclopedia/details.html",
            {"title": title, "content": markdown2.markdown(content)},
        )
    else:
        raise Http404("Entry not found!")


def search(request):
    title = request.GET.get("q")
    entries = util.list_entries()
    filtered_entries = []
    for s in entries:
        if title in s:
            filtered_entries.append(s)
    if title in entries:
        return HttpResponseRedirect(reverse("encyclopedia:details", args=[title]))

    return render(
        request,
        "encyclopedia/search.html",
        {"filtered_entries": filtered_entries},
    )


def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["new_title"]
            content = form.cleaned_data["content"]
            util.save_entry(new_title, content)
            return HttpResponseRedirect(
                reverse("encyclopedia:details", args=[new_title])
            )
        else:  # if the title found
            return render(
                request,
                "encyclopedia/create.html",
                {"form": form},
            )

    else:
        return render(
            request,
            "encyclopedia/create.html",
            {"form": NewEntryForm()},
        )


def editEntry(request, title):
    if request.method == "GET":
        content = util.get_entry(title)
        return render(
            request,
            "encyclopedia/edit.html",
            {
                "form": EditEntryForm(initial={"content": content}),
                "title": title,
            },
        )
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:details", args=[title]))
        else:
            return render(
                request,
                "encyclopedia/edit.html",
                {
                    "form": form,
                    "title": title,
                },
            )


def randomPage(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return HttpResponseRedirect(reverse("encyclopedia:details", args=[title]))
