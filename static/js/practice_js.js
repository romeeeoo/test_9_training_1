const csrfToken = getCookie('csrftoken')

const btnFavouriteList = $(`.btn_favourite`)
console.log(btnFavouriteList)

for ( const btnFavourite of btnFavouriteList) {
    $(btnFavourite).click(function toggleFavourite(event) {
    event.preventDefault()
    $.ajax({
        url: $(this.parentElement).attr("action"),
        method: 'POST',
        headers: {"X-CSRFToken": csrfToken},
        data: {picture_id: $(btnFavourite).attr("id")},
        success: function (data, status) {
            $(btnFavourite).toggleClass("btn-dark")
            console.log(data);
            console.log(status);
        },
        error: function (data, response, status) {
            console.log(status);
            console.log(data);
        }
    });
});
};

