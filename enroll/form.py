from django import forms
from enroll import models

class AddStudentForm(forms.ModelForm):
    c_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"w-full bg-white rounded border border-gray-300 focus:border-black-500 focus:ring-2 focus:ring-black text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out my-4","autocomplete":"off"}),label="Confirm Password",required=False)
    class Meta:
        model = models.Student
        fields = "__all__"
        widgets = {
         "password":forms.PasswordInput(attrs={"class":"w-full bg-white rounded border border-gray-300 focus:border-black-500 focus:ring-2 focus:ring-black text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out my-4","autocomplete":"off"},render_value=True),
         "roll_num":forms.NumberInput(attrs={"class":"w-full bg-white rounded border border-gray-300 focus:border-black-500 focus:ring-2 focus:ring-black text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out my-4","autocomplete":"off"}),
         "name":forms.TextInput(attrs={"class":"w-full bg-white rounded border border-gray-300 focus:border-black-500 focus:ring-2 focus:ring-black text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out my-4","autocomplete":"off"}),
         "email":forms.EmailInput(attrs={"class":"w-full bg-white rounded border border-gray-300 focus:border-black-500 focus:ring-2 focus:ring-black text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out my-4","autocomplete":"off"})
        }
        labels = {"roll_num":"Roll No"}