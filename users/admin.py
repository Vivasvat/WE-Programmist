from django.contrib import admin

"""
Данный импорт нужен для того, чтобы наша таблица отображалась в admin панеле
"""
from users.models import User

admin.site.register(User)