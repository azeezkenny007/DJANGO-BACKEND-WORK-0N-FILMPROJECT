# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form field labels and widget attributes
        self.fields['old_password'].label = 'Current password'
        self.fields['new_password1'].label = 'New password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter a new password'
        self.fields['new_password2'].label = 'Confirm new password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm your new password'

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm

@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Log the user out and redirect to the login page
            return redirect('login')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})
