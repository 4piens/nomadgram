from django.urls import path
from . import views


app_name = "images"
urlpatterns = [
	path("all/", view=views.ListAllImages.as_view(), name="all_images"),
    path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
    path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
    path("", view=views.Images.as_view(), name="feed"),
    path("<int:image_id>/", view=views.ImageDetail.as_view(), name="image_detail"),
    path("<int:image_id>/likes", view=views.LikeImage.as_view(), name="likes_image"),
    path("<int:image_id>/unlikes", view=views.UnLikeImage.as_view(), name="unlikes_image"),
    path("<int:image_id>/comment", view=views.CommentOnImage.as_view(), name="moderate_image"),
    path("<int:image_id>/comment/<int:comment_id>", view=views.ModerateComments.as_view(), name="comment_image"),
    path("comments/<int:comment_id>", view=views.Comment.as_view(), name="comment"),
    path("search/", view=views.Search.as_view(), name="search")
]
