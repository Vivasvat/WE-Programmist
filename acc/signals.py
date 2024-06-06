# from allauth.socialaccount.models import SocialAccount
# from allauth.account.signals import user_logged_in, user_signed_up

# from acc.forms import ProfileForm

# from django.dispatch import receiver

# from acc.models import MyAccount

# @receiver(user_logged_in)
# def get_login_up_callback(request, user, **kwargs):
#     try:
#         social_account = SocialAccount.objects.get(user=user)
#         extra_data = social_account.extra_data
#         provider = social_account.provider
#         form = ProfileForm(instance=request.user)

#         if provider == "google":
#             get_data_google(user, extra_data)
#         if provider == "steam":
#             get_data_steam(user, extra_data, form)
#     except social_account.DoesNotExist:
#         pass

# def get_data_google(user, extra_data):
#     google_id = extra_data.get('id')
#     email = extra_data.get('email')
#     name = extra_data.get('name')
#     picture = extra_data.get('picture')
#     # Дополнительная логика для Google

#     # Обновите или создайте профиль пользователя
#     acc = MyAccount.objects.get_or_create(user=user)
#     acc.google_id = google_id
#     acc.email = email
#     acc.name = name
#     acc.picture = picture
#     acc.save()

# def get_data_steam(user, extra_data, form):

#     steamid = extra_data.get('steamid')
#     personaname = extra_data.get('personaname')
#     avatarfull = extra_data.get('avatarfull')
#     # Дополнительная логика для Steam

#     # Обновите или создайте профиль пользователя

#     acc = MyAccount.objects.get_or_create(username=form.username.value)
#     acc.id = steamid
#     acc.username = personaname
#     acc.avatar = avatarfull
#     acc.save()

# @receiver(user_signed_up)
# def user_signed_up_callback(request, user, **kwargs):
#     try:
#         social_account = SocialAccount.objects.get(user=user)
#         extra_data = social_account.extra_data
#         provider = social_account.provider

#         if provider == 'google':
#             handle_google_signup(user, extra_data)
#         elif provider == 'steam':
#             handle_steam_signup(user, extra_data)
#         # Добавьте другие провайдеры по мере необходимости

#     except social_account.DoesNotExist:
#         pass  # Пользователь не использует социальный аккаунт для регистрации

# def handle_google_login(user, extra_data):
#     google_id = extra_data.get('id')
#     email = extra_data.get('email')
#     name = extra_data.get('name')
#     picture = extra_data.get('picture')
#     # Дополнительная логика для Google

#     # Обновите или создайте профиль пользователя
#     acc = MyAccount.objects.get_or_create(user=user)
#     acc.google_id = google_id
#     acc.email = email
#     acc.name = name
#     acc.picture = picture
#     acc.save()

# def handle_google_signup(user, extra_data):
#     # Аналогичная логика для регистрации через Google
#     handle_google_login(user, extra_data)

# def handle_steam_login(user, extra_data):
#     steamid = extra_data.get('steamid')
#     personaname = extra_data.get('personaname')
#     avatarfull = extra_data.get('avatarfull')
#     # Дополнительная логика для Steam

#     # Обновите или создайте профиль пользователя
#     acc = MyAccount.objects.get_or_create(user=user)
#     acc.steamid = steamid
#     acc.personaname = personaname
#     acc.avatarfull = avatarfull
#     acc.save()

# def handle_steam_signup(user, extra_data):
#     # Аналогичная логика для регистрации через Steam
#     handle_steam_login(user, extra_data)