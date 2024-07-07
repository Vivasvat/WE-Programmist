from users.models import OneTimeLink
from django.urls import reverse

def generate_one_time_link(user):
    one_time_link = OneTimeLink.objects.create(user=user)
    link = reverse('users:use_one_time_link', args=[one_time_link.token])
    return link