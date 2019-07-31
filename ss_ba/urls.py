from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('new/', views.new, name='new'), # 상품 등록
    path('create/', views.create, name='create'), # 상품 등록
    path('', views.main, name='main'), # 등록된 게시글
    path('delete/<int:id>/', views.delete, name='delete'), # 임시
    path('detail/<int:id>/', views.detail, name='detail'), # 상품 상세
    path('edit/<int:id>/', views.edit, name='edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)