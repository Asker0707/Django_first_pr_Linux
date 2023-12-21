
import pytest
from students.models import Student, Course
from rest_framework.test import APIClient

@pytest.fixture
def clien():
    return APIClient()
@pytest.mark.django_db
def test_example(client):
    
    Student.objects.create(name="John", birth_date="2000-01-01")
    Course.objects.create(name="Python")
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    