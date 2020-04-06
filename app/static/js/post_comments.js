$(function () {
    let post_comments = $(".post_comments");

    if (post_comments.find(".comment_form").length || post_comments.find(".comments_title").length)
        post_comments.show();
    else
        post_comments.hide();
});