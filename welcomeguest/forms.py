from django import forms
from .models import Guest
import re

class GuestForm(forms.ModelForm):
    

    def clean_full_name(self):
        name = self.cleaned_data["full_name"].strip()

        # Фамилия Имя Отчество
        pattern = r"^[А-ЯЁA-Z][а-яёa-z-]+ [А-ЯЁA-Z][а-яёa-z-]+ [А-ЯЁA-Z][а-яёa-z-]+$"

        if not re.match(pattern, name):
            raise forms.ValidationError(
                "Введите ФИО полностью (Фамилия Имя Отчество)."
            )

        return name
    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        phone = re.sub(r"\D", "", phone)   # оставить только цифры

        # если ввели 8XXXXXXXXXX
        if len(phone) == 11 and phone.startswith("8"):
            phone = "7" + phone[1:]

        if len(phone) != 11 or not phone.startswith("7"):
            raise forms.ValidationError(
                "Введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX"
            )

        return "+{}".format(phone)

    class Meta:
        model = Guest

        fields = [
            "full_name",
            "phone",
            "attendance",
            "extra_guests",
            "comment",
            "wish",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Введите ФИО"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "+7 (900) 000-00-00"
            }),

            "attendance": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),

            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
            }),

            "wish": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Пожелания по еде/алкоголю"
            }),
            "extra_guests": forms.Textarea(attrs={
                "class":"form-control",
                "rows":4,
                "placeholder":"Иванов Иван Иванович\nПетров Петр Петрович"
            }),

        }