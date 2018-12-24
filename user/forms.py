from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'name', 'user_number', 'identity', 'department')


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'user_number', 'name', 'department', 'password', 'identity')





#
# class UserForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = (
#             'user_number')






# class LoginForm(forms.Form):
#     username = UsernameField(required=True,max_length=12,min_length=6)
#     password = PasswordField(required=True,max_length=12,min_length=6)
#
#     def __init__(self, request=None, *args, **kwargs):
#         self.request = request
#         self.user_cache = None
#         super(LoginForm, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username and password:
#             self.user_cache = authenticate(username=username, password=password)
#             # 如果成功返回对应的User对象，否则返回None(只是判断此用户是否存在，不判断是否is_active或者is_staff)
#             if self.user_cache is None:
#                 raise forms.ValidationError(u"您输入的用户名或密码不正确!")
#             elif not self.user_cache.is_active or not self.user_cache.is_staff:
#                 raise forms.ValidationError(u"您输入的用户名或密码不正确!")
#             else:
#                 login(self.request, self.user_cache)
#         return self.cleaned_data
#
#     def get_user_id(self):
#         if self.user_cache:
#             return self.user_cache.id
#         return None
#
#     def get_user(self):
#         return self.user_cache
#
# class ChangePasswordForm(forms.Form):
#     """
#         A form used to change the password of a user in the admin interface.
#     """
#     newpassword = PasswordField(required=True,max_length=12,min_length=6)
#     renewpassword = PasswordField(required=True,max_length=12,min_length=6)
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super(ChangePasswordForm, self).__init__(*args, **kwargs)
#
#     def clean_password2(self):
#         newpassword = self.cleaned_data.get('newpassword')
#         renewpassword = self.cleaned_data.get('renewpassword')
#         if newpassword and renewpassword:
#             if newpassword != renewpassword:
#                 raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
#         raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
#         return renewpassword
#
#     def save(self, commit=True):
#         """
#         Saves the new password.
#         """
#         self.user.set_password(self.cleaned_data["newpassword"])
#         if commit:
#             self.user.save()
#         return self.user
#
#
# class StudentForm(forms.Form):
#     student_id = forms.CharField(required=False)
#     studentid = StudentidField(required=True)
#     studentname = StudentnameField(required=True, max_length=4, min_length=2)
#     studentsex = forms.ChoiceField(required=True, choices=SEX_CHOICES, error_messages={'invalid': u'请您正确选择下拉框'})
#
#     def clean_student_id(self):
#         if self.get_id():
#             try:
#                 Student.objects.get(id=self.get_id())
#             except Student.DoesNotExist:
#                 raise forms.ValidationError(u"请不要非法提交数据")
#             return self.get_id()
#         return self.get_id()
#
#     def clean_studentid(self):
#         if not self.get_id():
#             try:
#                 User.objects.get(username=self.cleaned_data['studentid'])
#             except User.DoesNotExist:
#                 return self.cleaned_data['studentid']
#             raise forms.ValidationError(u"该学号已经存在")
#         else:
#             try:
#                 student = Student.objects.get(id=self.get_id())
#                 try:
#                     oclassid = student.user.username
#                     User.objects.exclude(username=oclassid).get(username=self.cleaned_data['studentid'])
#                     raise forms.ValidationError(u"该学号已经存在")
#                 except User.DoesNotExist:
#                     return self.cleaned_data['studentid']
#             except Student.DoesNotExist:
#                 raise forms.ValidationError(u"请不要非法提交数据")
#         return self.cleaned_data['studentid']
#
#
#     def get_id(self):
#         return self.cleaned_data['student_id']
#
#     def save(self, commit=True):
#         user = User.objects.create_user(self.cleaned_data['studentid'], '', '000000')
#         user.is_staff = True
#         user.save()
#         student = Student(user=user, realname=self.cleaned_data['studentname'], \
#                           sex=self.cleaned_data['studentsex'])
#         if commit:
#             student.save()
#         return student
#
#     def update(self):
#         student = Student.objects.get(id=self.get_id())
#         user = student.user
#         user.username = self.cleaned_data['studentid']
#         user.save()
#         student.realname = self.cleaned_data['studentname']
#         student.sex = self.cleaned_data['studentsex']
#         student.save()