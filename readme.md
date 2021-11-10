# Django Simple DRF Project with PostgreSQL

### Simple implementation of api project using django_rest_framework and postgresql database.

The project has one serializer class which subclasses serializers.ModelSerializer from rest_framework.

The project has 5 simple endpoints:
- POST: `/api/tutorials` for adding a new tutorial to the database.
- GET: `/api/tutorials` for retrieving *all tutorials* from the database.
- PUT: `/api/tutorials/:id` to perform PUT operations on a single tutorial.
- GET: `/api/tutorials/published` to retrieve only published tutorials from the database.
- DELETE: `/api/tutorials/:id` to delete a tutorial by id.