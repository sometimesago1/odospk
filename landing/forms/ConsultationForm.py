from django import forms

class ConsultationForm(forms.Form):
    name = forms.CharField(
        label = 'Ваше имя', 
        max_length = 25, 
        required = True, 
        widget = forms.TextInput(
            attrs={
                'placeholder':'Иван', 
                'class':'bg-neutral-850 px-6 py-6 font-medium rounded-2xl mt-4 text-base leading-none focus__fixer',
                'id':'customer_name',
            }
        )
    )

    phone = forms.CharField(
        label = 'Ваш телефон', 
        max_length=11, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder':'+7 999 999 99 99', 
                'class': 'bg-neutral-850 px-6 py-6 font-medium rounded-2xl mt-4 text-base leading-none focus__fixer',
                'id':'customer_phone',
            }
        )
    )

    checkbox = forms.BooleanField(
        label='Я даю согласие на обработку персональных данных в соответствии с Политикой конфиденциальности', 
        required=True, 
        widget=forms.CheckboxInput(
            attrs={
                'class':'checkbox__fixer',
                'id':'checkbox',
            }
        )
    )