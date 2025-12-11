from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        User.objects.create(name='Batman', email='batman@dc.com', team=dc)

    def test_user_team(self):
        spiderman = User.objects.get(email='spiderman@marvel.com')
        self.assertEqual(spiderman.team.name, 'Marvel')
        batman = User.objects.get(email='batman@dc.com')
        self.assertEqual(batman.team.name, 'DC')
