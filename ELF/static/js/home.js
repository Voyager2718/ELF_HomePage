var titleHeightPercent = 0.8;
var headerOpacity = 0.7;

var setBackground = function (e) {
    if (window.innerHeight < window.innerWidth) {
        $("#title").css({
            "background": "url('" + baseDir + "/ELF/static/img/background.jpg')",
            "background-size": "100% auto",
            "background-position": "100% 100%",
        });
    } else {
        $("#title").css({
            "background": "url('" + baseDir + "/ELF/static/img/background_vertical.jpg')",
            "background-size": "100% auto",
            "background-position": "100% 100%",
        });
    }
}

var setVideoPosition = function (e) {
    var v = $(".video");
    var width = v.css("width");
    width = width.substr(0, width.length - 2);
    v.css({
        "height": width / 1.777778
    })
}

var resizeActions = function (e) {
    setBackground(e);
    setVideoPosition(e);
}

var loadActions = function (e) {
    resizeActions(e);
}

window.onload = loadActions;

window.onresize = resizeActions;

window.onscroll = function (e) {
    if (document.documentElement.scrollTop > window.innerHeight * titleHeightPercent) {
        $("#header").css({
            "background": "rgba(255, 255, 255, 1)",
            "box-shadow": "gray 0 0 10px"
        });
    } else {
        $("#header").css({
            "background": "rgba(255, 255, 255, " + headerOpacity + ")",
            "box-shadow": "none"
        });
    }
}