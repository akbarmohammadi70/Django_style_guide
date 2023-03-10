from django.urls import path, include

urlpatterns = [
     path('blog/', include(('django_style_guide.blog.urls', 'blog')))
]
