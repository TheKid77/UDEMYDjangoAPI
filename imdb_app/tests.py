from django.contrib.auth.models import User  
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from imdb_app.api import serializers
from imdb_app import models  

class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", 
                                            password="newpassword")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")

    def test_streamplatform_create(self):
        data = {
            "name": "netflix", 
            "about": "#1 Streaming Platform", 
            "website": "http://www.netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_admincreate(self):
        data = {
            "name": "netflix2", 
            "about": "#1 Streaming Platform", 
            "website": "http://www.netflix.com"
        }
        # switch to admin user
        self.user.is_staff=True
        self.user.save()
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_streamplatform_update(self):
        data = {
            "name": "updated name",
            "about": "#1 Streaming Platform", 
            "website": "http://www.netflix.com"
        }
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_adminupdate(self):
        data = {
            "name": "updated name",
            "about": "#1 Streaming Platform",
            "website": "http://www.netflix.com"
        }
        # switch to admin user
        self.user.is_staff=True
        self.user.save()
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_streamplatform_delete(self):

        self.delstream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")
        response = self.client.delete(reverse('streamplatform-detail', args=(self.delstream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_admindelete(self):

        self.delstream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")
        # switch to admin user
        self.user.is_staff=True
        self.user.save()
        response = self.client.delete(reverse('streamplatform-detail', args=(self.delstream.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)     

class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", 
                                            password="newpassword")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                storyline="Story", active=True)
    def test_watchlist_create(self):
        data = {
            "platform": self.stream.id, 
            "title": "Example Movie", 
            "storyline": "Example Story",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_admincreate(self):
        data = {
            "platform": self.stream.id, 
            "title": "Example Movie", 
            "storyline": "Example Story",
            "active": True 
        }
        # switch to admin user
        self.user.is_staff=True
        self.user.save()

        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_watchlist_update(self):
        data = {
            "platform": self.stream.id, 
            "title": "Updated Example Movie", 
            "storyline": "Example Story",
            "active": True 
        }
        response = self.client.put(reverse('movie-detail', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_adminupdate(self):
        data = {
            "platform": self.stream.id, 
            "title": "Updated Example Movie", 
            "storyline": "Example Story",
            "active": True 
        }
        # switch to admin user
        self.user.is_staff=True
        self.user.save()
        response = self.client.put(reverse('movie-detail', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_watchlist_delete(self):

        self.delmovie = models.WatchList.objects.create(platform=self.stream, 
            title="Example Movie2", storyline= "Example Story2",active= True,)
        response = self.client.delete(reverse('movie-detail', args=(self.delmovie.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_admindelete(self):

        self.delstream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")
        # switch to admin user
        self.user.is_staff=True
        self.user.save()
        self.delmovie = models.WatchList.objects.create(platform=self.stream, 
            title = "Example Movie2", storyline= "Example Stry2",active= True,)
        response = self.client.delete(reverse('movie-detail', args=(self.delmovie.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # revert to normal user
        self.user.is_staff=False
        self.user.save()

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_watchlist_ind(self):      
        response = self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')

class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", 
                                            password="newpassword")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name="netflix",
                                about="#1 Streaming Platform", website="http://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                storyline="Story", active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                                storyline="Story", active=True)
        self.review = models.Review.objects.create(review_user=self.user,
                                            rating=5, description="Great Movie!",
                                            watchlist=self.watchlist2,active=True)
    
    def test_review_create(self):
        data = {
            "review-user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review-user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review-user": self.user,
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }

        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        self.delreview = models.Review.objects.create(review_user=self.user,
                                            rating=5, description="Great Movie!",
                                            watchlist=self.watchlist2,active=True)
        response = self.client.delete(reverse('review-detail', args=(self.delreview.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

