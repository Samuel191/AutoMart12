from main_app import views
from . import views #el punto nos manda a raiz


urlpatterns = [
    path('',viewsindex),
]