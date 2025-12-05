from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserTests(APITestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Add similar tests for Activity, Workout, Leaderboard as needed
