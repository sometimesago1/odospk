from django import forms

class ConsultationForm(forms.Form):
    name = forms.CharField(
        label = 'Ваше имя',
        max_length = 25,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Иван',
                'class': 'focus__fixer bg-neutral-150 border border-neutral-400 px-4 py-5 text-neutral-850 placeholder:text-neutral-500 font-medium rounded-2xl text-base leading-none',
                'id': 'customer_name',
            }
        )
    )

    phone = forms.CharField(
        label = 'Телефон',
        max_length = 11,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': '+7 999 999 99 99',
                'class': 'focus__fixer bg-neutral-150 border border-neutral-400 px-4 py-5 text-neutral-850 placeholder:text-neutral-500 font-medium rounded-2xl text-base leading-none',
                'id': 'customer_phone',
            }
        )
    )

    checkbox = forms.BooleanField(
        label = 'Я даю согласие на обработку персональных данных в соответствии с Политикой конфиденциальности',
        required = True,
        widget = forms.CheckboxInput(
            attrs = {
                'class': '',
                'id': 'agreement'
            }
        )
    )