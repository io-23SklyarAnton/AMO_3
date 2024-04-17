from django import forms


class DrawGraphForm(forms.Form):
    a = forms.IntegerField(max_value=1000)
    b = forms.IntegerField(max_value=2000)

    FUNCTIONS_CHOICES = [('sin(x)', 'sin(x)'), ('sin^3(x) + 3cos^2(x)', 'sin^3(x) + 3cos^2(x)')]
    function = forms.ChoiceField(choices=FUNCTIONS_CHOICES, widget=forms.RadioSelect)

    def clean_b(self):
        cd = self.cleaned_data
        if cd['b'] < cd['a']:
            raise forms.ValidationError('b value must be bigger, than a')
        return cd['b']
