'use strict';

angular.module("tryNav").directive('tryNav', function(Post, $cookies, $location) {
    return {
        restrict: "E",
        templateUrl: "/api/templates/try-nav.html",
        link: function(scope, element, attr) {
            scope.items = Post.query()
            scope.selectItem = function($item, $model, $label) {
                console.log($item, $model, $label)
                $location.path("/blog/" + $item.id)
                scope.searchQuery = ""
            }
            scope.searchItem = function() {
                console.log(scope.searchQuery)
                $location.path("/blog/").search("q", scope.searchQuery)
                scope.searchQuery = ""
            }

            scope.userLoggedIn = false;
            scope.$watch(function() {
                var token = $cookies.get("token");
                console.log(token);
                if (token) {
                    scope.userLoggedIn = true;
                } else {
                	scope.userLoggedIn = false;
                }
            })

        }
    }
})
