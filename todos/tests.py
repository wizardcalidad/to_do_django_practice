from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='this is gonna be cool', )

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(
            expected_object_name, 'first todo'
        )

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_body_name = f'{todo.body}'
        self.assertEquals(
            expected_body_name, 'this is gonna be cool'
        )
