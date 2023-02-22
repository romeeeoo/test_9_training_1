console.log(10)

$(document).ready(function () {
    console.log(1)
    let btnFavouriteList = $(`.btn_favourite`)
    let deleteCommentBtnList = $(".delete_submit")
    let commentText = $(".comment_text")
    let commentSubmit = $(".comment_submit")
    let pictureId = $(".card").data("pictureid")
    let detailedUrl = $(".url-detailed").attr("href")


    for (let btnFavourite of btnFavouriteList) {
        $(btnFavourite).click(function toggleFavourite(event) {
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'post',
                headers: {"X-CSRFToken": csrfToken},
                data: {picture_id: $(btnFavourite).attr("id")},
                success: function (data, status) {
                    $(btnFavourite).toggleClass("btn-dark")
                    console.log(data);
                    console.log(status);
                    console.log(4)
                },
                error: function (data, response, status) {
                    console.log(status);
                    console.log(data);
                }
            });
        });
    }


    $(commentSubmit).click(function addComment(event) {
        console.log("нажали на кнопку")
        let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
        event.preventDefault()
        $.ajax({
            url: $(this.parentElement).attr("action"),
            method: 'post',
            headers: {"X-CSRFToken": csrfToken},
            data: {"text": commentText.val(), "picture_id": pictureId},
            success: function (data, status) {
                console.log(data);
                console.log(status);
                $(".new_comments").load(detailedUrl);
                console.log(5)

            },
            error: function (data, response, status) {
                console.log(status);
                console.log(data);
            }
        });
    })


    for (let deleteCommentBtn of deleteCommentBtnList) {
        $(deleteCommentBtn).click(function deleteComment(event) {
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            let commentId = $(deleteCommentBtn).data('commentId')
            console.log(`this is ${commentId}`)
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'DELETE',
                headers: {"X-CSRFToken": csrfToken},
                data: {"comment_id": commentId},
                success: function (data, status) {
                    console.log(data);
                    console.log(status);
                    console.log(6);
                    $(".new_comments").load(detailedUrl);
                },
                error: function (data, response, status) {
                    console.log(status);
                    console.log(data);
                }
            });
        })

    }
    console.log(2)

})




