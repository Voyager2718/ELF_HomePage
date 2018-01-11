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
            $scope.currentLanguage = language_pack[lang];
            $scope.displayLang = lang;
            if ($scope.currentLanguage == undefined) {

                $scope.browserLanguage=(window.navigator.languages
                    ? window.navigator.languages[0]
                    : (window.navigator.language || window.navigator.userLanguage)).substr(0,2);

                    switch($scope.browserLanguage){
                        case "zh-c": $scope.currentLanguage = language_pack['chs'] ; break;
                        case "zh": $scope.currentLanguage = language_pack['cht'] ; break
                        case "en": $scope.currentLanguage = language_pack['en'] ; break;
                        case "fr": $scope.currentLanguage = language_pack['fr'] ; break;
                        default  : $scope.currentLanguage = language_pack['en'] ; break;
                    }
               
                $scope.displayLang = $scope.currentLanguage;
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