#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    openslides.assignment.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Forms for the assignment app.

    :copyright: 2011 by the OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from django import forms
from django.forms import ModelForm, Form, ModelChoiceField, Select
from django.utils.translation import ugettext as _

from utils.forms import CssClassMixin
from participant.models import Profile
from assignment.models import Assignment


class AssignmentForm(ModelForm, CssClassMixin):
    class Meta:
        model = Assignment
        exclude = ('status', 'profile', 'elected')


class AssignmentRunForm(Form, CssClassMixin):
    candidate = ModelChoiceField(
        widget=Select(attrs={'class': 'medium-input'}),
        queryset=Profile.objects.all().order_by('user__first_name'),
        label=_("Nominate a participant"),
    )


class ConfigForm(Form, CssClassMixin):
    assignment_publish_winner_results_only = forms.BooleanField(
        required=False,
        label=_("Only publish voting results for selected winners (Projector view only)")
    )
    assignment_pdf_ballot_papers_selection = forms.ChoiceField(widget=forms.Select(),
        required=False,
        label=_("Number of ballot papers (selection)"),
        choices=[
            ("1", _("Number of all delegates")),
            ("2", _("Number of all participants")),
            ("0", _("Use the following custum number"))
        ]
    )
    assignment_pdf_ballot_papers_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class':'small-input'}),
        required=False,
        min_value=1,
        label=_("Custom number of ballot papers")
    )
    assignment_pdf_title = forms.CharField(
        widget=forms.TextInput(),
        required=False,
        label=_("Title for PDF document (all elections)")
    )
    assignment_pdf_preamble = forms.CharField(
        widget=forms.Textarea(),
        required=False,
        label=_("Preamble text for PDF document (all elections)")
    )
