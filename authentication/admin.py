from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Account
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
'''
admin.site.unregister(Group)
@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    icon = '<i class="material-icons">lock</i>'
'''
class AdminAccount(Account):
    class Meta:
        proxy = True    
        app_label='auth'
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = AdminAccount
        exclude=('last_login',)

    def clean_password(self):
        # Check that the two password entries match
        #print self.cleaned_data
        return self.cleaned_data.get("password")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

@admin.register(AdminAccount)
class AAC(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserCreationForm
    icon = '<i class="material-icons">person</i>'
    list_display = ('username', 'email','first_name','last_name', 'is_admin',\
        'created_at','updated_at')
    list_filter = ('username','email')
    readonly_fields=('last_login',)
