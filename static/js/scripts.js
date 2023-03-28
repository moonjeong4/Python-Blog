$("form[name=sign-up-form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error")
    var data = $form.serialize()

    $.ajax({
        url: "signup", type: "POST", data: data, datatype: "json", success: function (resp) {
            window.location.href = "/login";

        }, error: function (resp) {
            if (resp.responseJSON && resp.responseJSON.error) {
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            } else {
                $error.text("An error occurred").removeClass("error--hidden");
            }
        }
    });
    e.preventDefault()
});

$("form[name=login-form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error")
    var data = $form.serialize()

    $.ajax({
        url: "login", type: "POST", data: data, datatype: "json", success: function (resp) {
            window.location.href = "/";

        }, error: function (resp) {
            if (resp.responseJSON && resp.responseJSON.error) {
                $error.text(resp.responseJSON.error).removeClass("error--hidden");
            } else {
                $error.text("An error occurred").removeClass("error--hidden");
            }
        }
    });
    e.preventDefault()
});
