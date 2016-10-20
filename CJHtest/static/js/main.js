login = function () {
    $(".login").css("display","block");
    $("#login-form").css("display","inline-block");
};
cancel = function () {
    $(".login").css("display","none");
    $("#sign-up").css("display","none");
};
sign_up = function () {
    $("#login-form").css("display","none");
    $("#sign-up").css("display","inline-block");
};