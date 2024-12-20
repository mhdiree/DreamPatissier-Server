from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import QuestionView, SubmitView, ResultView

app_name = 'test'

urlpatterns = [
    path('test/questions/<int:page_number>',QuestionView.as_view(), name='question_page'),
    path('test/submit',SubmitView.as_view(),name='submit_page'),
    path('test/result/<str:pk>', ResultView.as_view(), name='result-detail') #null 처리를 위해 str로 수정
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)