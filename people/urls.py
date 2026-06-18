from rest_framework.urls import path


from people.views import (
    ListDocumentTypeView,
    DocumentTypeByNameView,
    ListGenreView,
    GenreByNameView,
    ListPeopleView,
    PersonByLastnameView,
    PersonByDocumentNumberView,
    CreatePersonView,
    UpdatePersonView
)

urlpatterns = [
    path(
        'document/type/list',
        ListDocumentTypeView.as_view(),
        name='document-type-list'
    ),
    path(
        'document/type/name/<str:name>',
        DocumentTypeByNameView.as_view(),
        name='document-type-name'
    ),
    path(
        'genre/list/',
        ListGenreView.as_view(),
        name='genre-list'
    ),
    path(
        'genre/name/<str:name>',
        GenreByNameView.as_view(),
        name='genre-name'
    ),
    path(
        'list/',
        ListPeopleView.as_view(),
        name='list-people'
    ),
    path(
        'name/<str:last_name>',
        PersonByLastnameView.as_view(),
        name='person-last-name'
    ),
    path(
        'document/<str:document_number>',
        PersonByDocumentNumberView.as_view(),
        name='person-document-number'
    ),
    path(
        'create/',
        CreatePersonView.as_view(),
        name='create-person'
    ),
    path(
        'update/<int:id>',
        UpdatePersonView.as_view(),
        name='update-person'
    ),
]
