from django.urls import path, re_path

import feedback.views as feedback

urlpatterns = [
    path('', feedback.feedback),
    path('edit_feedback/<int:feedback_id>/', feedback.editFeedback),
    path('delete_feedback/<int:feedback_id>/', feedback.deleteFeedback),
]