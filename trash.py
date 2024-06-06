# django-allauth
SITE_ID=1

# urlpatterns = [path('accounts/', include('allauth.urls')),
# ]

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Providers
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.google',
    ]

# Add the account middleware:
MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
]

SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APP': {
            'client_id': 'your-vk-client-id',
            'secret': 'your-vk-client-secret',
            'key': ''
        },
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'v': '5.95'},
        'METHOD': 'oauth2',
    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Needed to login by username in Django admin, regardless of `allauth`
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATES = [
    'django.template.context_processors.request', # django-allauth
]


# <!-- <form method="POST" action="{{string}}">
#       {% csrf_token %}
#       <button type="submit">VK</button>
#     </form> -->
#     <form method="POST" action="{{ google_login }}">
#       {% csrf_token %}
#       <button type="submit">Google</button>
#     </form>

"""
host - переменная, которая хранит в себе путь к станице сайта.
На которую должен перейти пользователь после авторизации через VK.
Как сделать Туннель ngrok можно узнать по ссылке:
https://habr.com/ru/articles/697620/

При перезупуске ngrok нужно в переменную host нужно скопировать новый хост.
Также нужно его заменить в "VK dev".
"""

    # Читай документацию к переменным host и string выше!
    # host = "https://unified-sunbird-strictly.ngrok-free.app/main/"
    # string=(f"https://oauth.vk.com/authorize?client_id={51929642}"
    #         f"&display=page"
    #         f"&redirect_uri={host}")
    # google_login=(f"https://accounts.google.com/o/oauth2/v2/auth?"
    #               f"scope=https%3A//www.googleapis.com/auth/drive.metadata.readonly"
    #               #f"&include_granted_scopes=true"
    #               #f"&response_type=token"
    #               f"&state=pass-through value"
    #               f"&redirect_uri={host}"
    #               f"&client_id=533408095131-0bgva6qeub7ff7gmsp3kqenjqvo9qb7d.apps.googleusercontent.com"
    #         )

# play-with-us/main.png

# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user) # files=request.FILES
#         if form.is_valid():
#             # user = form.save()
#             return HttpResponseRedirect(reverse('acc:profile'))
#     else:
#         social_account = SocialAccount.objects.get(user=request.user, provider="steam")
#         user_steam = social_account.extra_data
#     context = {
#         'user_steam' : user_steam,
#         'title': 'Home - Кабинет',
#         # 'form': form,
#     }
#     # acc = MyAccount.objects.get("")
#     return render(request, 'acc/account.html', context) 

        # <!-- <p>{{ user_steam.get('communityvisibilitystate') }}</p>
        # <p>{{ user_steam.get('profilestate') }}</p>
        # <p>{{ user_steam.get('personaname') }}</p>
        # <p>{{ user_steam.get('profileurl') }}</p>
        # <img src="{{ user_steam.get('avatar') }}" alt="avatar">
        # <img src="{{ user_steam.get('avatarmedium') }}" alt="avatarmedium">
        # <img src="{{ user_steam.get('avatarfull') }}" alt="avatarfull">
        # <img src="{{ user_steam.get('avatarhash') }}" alt="avatarhash">
        # <p>{{ user_steam.get('lastlogoff') }}</p>
        # <p>{{ user_steam.get('personastate') }}</p>
        # <p>{{ user_steam.get('realname') }}</p>
        # <p>{{ user_steam.get('primaryclanid') }}</p>
        # <p>{{ user_steam.get('timecreated') }}</p>
        # <p>{{ user_steam.get('personastateflags') }}</p>
        # <p>{{ user_steam.get('loccountrycode') }}</p> -->