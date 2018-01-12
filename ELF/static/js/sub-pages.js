// ===============================
// =====     JS + jQuery     =====
// ===============================

var titleHeightPercent = 0.3;
var headerOpacity = 0.7;

// Set different background for portrait and langscape screen.
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

window.onload = setBackground;

window.onresize = setBackground;

// Set opacity for 
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

// ===============================
// =====     Angular App     =====
// ===============================

var app = angular.module('app', ['ngCookies']);



app.controller('appCtrl', ['$scope', '$cookies', function ($scope, $cookies) {
    $scope.currentLanguage = {};
    $scope.language_pack;

    $scope.init = () => {
        $scope.i18n.render();
        $scope.language_pack = language_pack;   // Import language file to $scope
    }

    $scope.i18n = new function () {
        this.render = () => {
            var lang = $cookies.get('Language')
            lang = lang == undefined ? getDefaultLanguage() : lang;
            $scope.currentLanguage = language_pack[lang]
            $scope.displayLang = lang;
        }

        this.setLanguange = (lang) => {
            var expireDate = new Date();
            expireDate.setTime(2144232732000);
            $cookies.put('Language', lang, { 'path': '/', 'expires': expireDate });
            this.render();
        }

        var getDefaultLanguage = () => {
            var browserLang = navigator.language;
            for (k in language_pack) {
                if (language_pack[k].compatible.indexOf(browserLang) >= 0) {
                    return language_pack[k].id;
                }
            }
            return language_pack[Object.keys(language_pack)[0]].id;
        }
    }

    $scope.switchLanguage = (lang) => {
        $scope.i18n.setLanguange(lang)
    }

    $scope.init();
}]);