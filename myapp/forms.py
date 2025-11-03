from django import forms
from .models import Student
import re   # 👈 ye line zaroor add karo (regex ke liye)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    # 🧩 First name check — sirf letters allow honge
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match("^[A-Za-z]+$", first_name):
            raise forms.ValidationError("Please enter only characters in First Name.")
        return first_name

    # 🧩 Last name check
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match("^[A-Za-z]+$", last_name):
            raise forms.ValidationError("Only letters allowed.")
        return last_name

    # 🧩 Email check — valid format aur duplicate na ho
    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(pattern, email):
            raise forms.ValidationError("Please enter a valid email address.")
        # optional duplicate check
        from .models import Student
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    # 🧩 Roll number check — empty nahi hona chahiye
    def clean_roll_no(self):
        roll_no = self.cleaned_data.get('roll_no')
        if not roll_no:
            raise forms.ValidationError("Roll number cannot be empty.")
        return roll_no

    # 🧩 Subject check
    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject or not subject.replace(' ', '').isalpha():
            raise forms.ValidationError("Only letters allowed.")
        return subject

    # 🧩 City check
    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city or not city.replace(' ', '').isalpha():
            raise forms.ValidationError(" Only letters allowed.")
        return city
