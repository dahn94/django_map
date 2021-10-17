from django.urls import path


from .views import IndexView, CreateAlvoView, UpdateAlvoView, DeleteAlvoView

urlpatterns = [
    path('', IndexView.as_view(template_name="index.html")),
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateAlvoView.as_view(), name='add_alvo'),
    path('<uuid:pk>/update/', UpdateAlvoView.as_view(), name='upd_alvo'),
    path('<uuid:pk>/delete/', DeleteAlvoView.as_view(), name='del_alvo'),
]