from django import forms 
class MyForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.Textarea()

    class Meta:
        error_messages = {
            'name': {
                'required': 'Please enter a name.',
                'max_length': 'Name should be less than 255 characters.'
            },
            'email': {
                'required': 'Please enter an email.',
                'invalid': 'Please enter a valid email.'
            },
            'message': {
                'required': 'Please enter a message.'
            }
        }