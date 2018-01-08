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

    $scope.init = () => {
        $scope.i18n.render();
    }

    $scope.i18n = new function () {
        this.render = () => {
            var lang = $cookies.get('Language');
            $scope.currentLanguage = language_pack[lang]
            $scope.displayLang = lang;
            if ($scope.currentLanguage == undefined) {
                $scope.currentLanguage = language_pack['en']
                $scope.displayLang = 'en';
            }
        }

        this.setLanguange = (lang) => {
            $cookies.put('Language', lang);
            this.render();
        }
    }

    $scope.switchLanguage = (lang) => {
        $scope.i18n.setLanguange(lang)
    }

    $scope.init();
}]);