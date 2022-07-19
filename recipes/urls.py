from django.urls import path
from recipes.views import home, recipes, blog, contact

urlpatterns = [
    path('', home),
    path('recipes/', recipes),
    path('blog/', blog),
    path('contact/', contact),
]
