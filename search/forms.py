from django import forms
from api_queries import get_platform_names

p_names = get_platform_names()
p_choices = [(None, '(Choose Platform)')] + zip(p_names, p_names)


class GameSearchForm(forms.Form):
    required_css_class = 'required'

    title = forms.CharField(label='Game Title', max_length=100,
                            required=True,
                            error_messages={'required': 'Please enter a title'})
    platform = forms.TypedChoiceField(label="Platform", choices=p_choices,
                                      empty_value='(Choose Platform)')
    ## genre not function as of 2/10/2015
    # genre = forms.ChoiceField(label="Genre", choices=p_choices)
