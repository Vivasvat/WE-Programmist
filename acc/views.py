from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

import json
import requests

from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialApp

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth

from django.http import HttpResponseRedirect

from users.models import User

@login_required(login_url='users:login')
def profile(request):
    if SocialAccount.objects.filter(user=request.user, provider="steam").exists():
        social_account = SocialAccount.objects.get(user=request.user, provider="steam")
        user_steam = social_account.extra_data

        steamid = user_steam.get('steamid')

        communityvisibilitystate = user_steam.get('communityvisibilitystate')
        profilestate = user_steam.get('profilestate')
        personaname = user_steam.get('personaname')
        profileurl = user_steam.get('profileurl')
        avatar = user_steam.get('avatar')
        avatarmedium = user_steam.get('avatarmedium')
        avatarfull = user_steam.get('avatarfull')
        avatarhash = user_steam.get('avatarhash')
        lastlogoff = user_steam.get('lastlogoff')
        personastate = user_steam.get('personastate')
        realname = user_steam.get('realname')
        primaryclanid = user_steam.get('primaryclanid')
        timecreated = user_steam.get('timecreated')
        personastateflags = user_steam.get('personastateflags')
        loccountrycode = user_steam.get('loccountrycode')
    
        res_2 = get_listfriends(steamid)

    # data = json.loads(user_steam)
        context = {
            'steamid':steamid,
            'communityvisibilitystate':communityvisibilitystate,
            'profilestate':profilestate,
            'personaname':personaname,
            'profileurl':profileurl,
            'avatar':avatar, # img url
            'avatarmedium':avatarmedium, # img url
            'avatarfull':avatarfull, # img url
            'avatarhash':avatarhash, # img url
            'lastlogoff':lastlogoff,
            'personastate':personastate,
            'realname':realname,
            'primaryclanid':primaryclanid,
            'timecreated':timecreated,
            'personastateflags':personastateflags,
            'loccountrycode':loccountrycode,

            'res_2' : res_2,

            'title': 'Home - Кабинет',
        }
    else:
        user = request.user
        context = {
            'email' : user.email,
            'username' : user.username,
            'phone_number' : user.phone_number,
        }
    return render(request, 'acc/account.html', context) 

# @login_required(login_url='users:login')
# def edit_profile(request, username):
#     try:
#         # pro=MyAccount.objects.get(username=username)
#         if request.method=="POST":
#             pro.name=request.POST.get("name")
#             pro.name_two=request.POST.get("name_two")
#             pro.save()
#             return HttpResponseRedirect("/main/")
#         else:
#             return render(request, "main/next.html", {"pro" : pro})

#     except pro.DoesNotExist:
#         return HttpResponseRedirect("<h2>Not found page :(</h2>")
    
# @login_required(login_url='users:login')
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        auth.logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('/')
    
    return render(request, 'acc/account.html')

def get_extra_data(user, provider):
    if not user or not provider:
        return None
    try:
        social_account = SocialAccount.objects.get(user=user, provider=provider)
    except SocialAccount.DoesNotExist:
        return None
    else:
        return social_account.extra_data

def get_listfriends(steam_id):
    social_app = SocialApp.objects.get(provider="steam")
    client_id = social_app.client_id
    
    url = (f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/'
           f'?key={client_id}'
           f'&steamid={steam_id}'
           f'&relationship=friend')
    
    response = requests.get(url)
    res = response.json()
    tmp = res['friendslist']
    friendlist = tmp['friends']

    return friendlist


# def GetUserStatsForGame():

    

# string = f'https://steamcommunity.com/openid/login'
#          f'?openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select'
#          f'&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select'
#          f'&openid.mode=checkid_setup'
#          f'&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
#          f'&openid.realm=http%3A%2F%2F127.0.0.1%3A8000%2F'
#          f'&openid.return_to=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2F'
#          f'steam%2Fcallback%2F%3Fjanrain_nonce%3D2024-06-05T16%253A06%253A06ZB6d89f'
    

    
    
# http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=222880&key=32F3511A43799D68278EE99A1F138508&steamid=76561198386267617

# http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=222880&key=32F3511A43799D68278EE99A1F138508&steamid=76561198386267617