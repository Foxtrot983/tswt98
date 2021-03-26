from django import forms
import json


class AddInp(forms.Form):
    name = forms.CharField(max_length=20)
    data = forms.CharField(max_length=1024)

    def clean_jsonfield(self):
        jdata = self.cleaned_data['data']
        try:
            jdata = json.loads(jdata)
        except:
            raise forms.ValidationError('Invalid data')
        return jdata
