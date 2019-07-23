from django import forms


class SoftwareForm(forms.Form):
    subassettype = forms.IntegerField(label="软件类型")
    licensenum = forms.IntegerField(label="授权数量")
    version = forms.CharField(label="软件/系统版本", min_length=1, max_length=64)
    
