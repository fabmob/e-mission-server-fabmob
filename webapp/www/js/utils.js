$(document).ready(function () {
    $(document).keydown(function (e) {
        if (e.keyCode === 37) {
            $(".carousel").carousel('prev');
        }
        if (e.keyCode === 39) {
            $(".carousel").carousel('next');
        }
    });
});

