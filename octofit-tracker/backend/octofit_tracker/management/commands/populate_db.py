from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-12-10')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2025-12-09')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2025-12-08')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date='2025-12-07')

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750)
        Leaderboard.objects.create(team=dc, points=800)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

        # Ensure unique index on email field
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Unique index created on email field in users collection.'))
