### Django REST API for Comments

This project implements a REST API for managing comments using Django and Django REST Framework.

#### Project Overview

The project allows CRUD operations on comments associated with publications. Each comment includes fields for content, publication ID, user ID, creation date, and is stored in a database managed by Django's ORM.

#### Project Structure

The project consists of the following components:

- **Models (`api/models.py`)**:
  ```python
  from django.db import models

  class Comment(models.Model):
      id_comment = models.AutoField(primary_key=True)
      id_publication = models.IntegerField()
      id_usuario = models.IntegerField()
      content = models.TextField()
      creation_date = models.DateTimeField()
  ```
  - Defines the `Comment` model with fields `id_comment`, `id_publication`, `id_usuario`, `content`, and `creation_date`.

- **Serializers (`api/serialize.py`)**:
  ```python
  from rest_framework import serializers
  from .models import Comment

  class CommentSerializer(serializers.ModelSerializer):
      class Meta:
          model = Comment
          fields = '__all__'
  ```
  - Implements `CommentSerializer` to serialize/deserialize `Comment` instances.

- **Views (`api/views.py`)**:
  ```python
  from rest_framework import viewsets
  from .models import Comment
  from .serialize import CommentSerializer

  class CommentViewSet(viewsets.ModelViewSet):
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
  ```
  - Defines `CommentViewSet` using Django REST Framework's `ModelViewSet` for CRUD operations on `Comment` model.

- **URL Configuration (`api/urls.py`)**:
  ```python
  from django.urls import path, include
  from rest_framework import routers
  from api import views

  router = routers.DefaultRouter()
  router.register(r'comments', views.CommentViewSet)

  urlpatterns = [
      path('', include(router.urls)),
  ]
  ```
  - Configures URL routing for the API endpoints using Django's `path` and `include`, and registers `CommentViewSet` with `routers.DefaultRouter`.

#### Usage

1. **Installation and Setup**:
   - Ensure Python and Django are installed. Install Django REST Framework (`pip install djangorestframework` if not installed).
   - Clone the project repository and navigate to its directory.

2. **Database Setup**:
   - Configure your database settings in `settings.py` (`DATABASES` setting).

3. **Running the Server**:
   - Run `python manage.py makemigrations` and `python manage.py migrate` to apply migrations.
   - Start the development server with `python manage.py runserver`.

4. **API Endpoints**:
   - The API endpoints are available under `/api/v1/comments/`, where you can perform CRUD operations on comments.

#### Configuration

- **Dependencies**:
  - The project relies on Django, Django REST Framework, and Python for its functionality.
  - Ensure dependencies are listed in `requirements.txt` for consistency.

- **Settings (`settings.py`)**:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
  }
  ```
  - Configures Django REST Framework to use `AutoSchema` for API schema generation.

- **URL Routing (`urls.py`)**:
  ```python
  from django.urls import path, include
  from rest_framework.documentation import include_docs_urls

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('api.urls')),
      path('docs/', include_docs_urls(title='Social Media API'))
  ]
  ```
  - Configures URL routing for admin panel, API endpoints (`/api/v1/`), and API documentation (`/docs/`).

#### Deployment

- For production deployment, configure `ALLOWED_HOSTS` and set appropriate security settings (`DEBUG=False`, secure database settings, etc.).

#### Further Information

For detailed information on Django and Django REST Framework, refer to their respective documentation:

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

This README provides an overview of the project structure, configuration, usage, and deployment considerations for the Django REST API managing comments. For any issues or improvements, refer to the project repository and its documentation.