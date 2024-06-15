from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test-user@example.com', password='qwe123qwe')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Тестовый курс', description='Описание курса', owner=self.user)
        self.lesson = Lesson.objects.create(title='Тестовый урок', description='Описание урока',
                                            url='https://www.youtube.com/watch?v=7wrMH2KQ1SI', course=self.course,
                                            owner=self.user)

    def test_lesson_list(self):
        response = self.client.get(reverse('materials:lesson_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": self.lesson.pk,
                 "title": "Тестовый урок",
                 "description": "Описание урока",
                 "preview": "http://testserver/media/lesson/default_lesson.jpg",
                 "url": "https://www.youtube.com/watch?v=7wrMH2KQ1SI",
                 "course": self.course.pk,
                 "owner": self.user.pk
                 }
            ]
        })

    def test_lesson_retrieve(self):
        response = self.client.get(reverse('materials:lesson_detail', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Тестовый урок",
            "description": "Описание урока",
            "preview": "http://testserver/media/lesson/default_lesson.jpg",
            "url": "https://www.youtube.com/watch?v=7wrMH2KQ1SI",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_create(self):
        data_valid = {
            "title": "Урок 1",
            "description": "Описание урока 1",
            "url": "https://www.youtube.com/watch?v=TDqnsu7zQjQ",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_valid)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            "id": 2,
            "title": "Урок 1",
            "description": "Описание урока 1",
            "preview": "http://testserver/media/lesson/default_lesson.jpg",
            "url": "https://www.youtube.com/watch?v=TDqnsu7zQjQ",
            "course": self.course.pk,
            "owner": self.user.pk
        })

        data_invalid = {
            "title": "Урок 2",
            "description": "Описание урока 2",
            "url": "https://site.com",
            "course": self.course.pk
        }

        response = self.client.post(reverse('materials:lesson_create'), data=data_invalid)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Запрещенная ссылка! Разрешены только с доменом youtube.com']})

    def test_lesson_update(self):
        data = {"title": "Измененный урок",
                "description": "Измененное описание урока",
                "url": "https://www.youtube.com/watch?v=v2mUu5MJoXY",
                "course": self.course.pk}

        response = self.client.patch(reverse('materials:lesson_update', kwargs={'pk': self.lesson.pk}),
                                     data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "id": self.lesson.pk,
            "title": "Измененный урок",
            "description": "Измененное описание урока",
            "preview": "http://testserver/media/lesson/default_lesson.jpg",
            "url": "https://www.youtube.com/watch?v=v2mUu5MJoXY",
            "course": self.course.pk,
            "owner": self.user.pk
        })

    def test_lesson_destroy(self):
        response = self.client.delete(reverse('materials:lesson_delete', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.all().exists())


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test-user@example.com', password='qwe123qwe')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Тестовый курс', description='Описание курса', owner=self.user)

    def test_subscription(self):
        data = {"user": self.user.pk,
                "course": self.course.pk}

        response = self.client.post(reverse('materials:subscribe'), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка добавлена"})

        response = self.client.post(reverse('materials:subscribe'), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка удалена"})
