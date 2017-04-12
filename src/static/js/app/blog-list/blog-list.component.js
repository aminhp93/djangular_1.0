'use strict';

angular.module('blogList').
component("blogList", {
    templateUrl: "/api/templates/blog-list.html",
    controller: function($cookies, $scope, $routeParams, Post, $rootScope, $location, $timeout) {
        console.log($location.search());
        console.log($cookies.get("username"));
        console.log($cookies.get("token"));
        var q = $location.search().q

        if (q) {
            $scope.query = q;
            $scope.searchQuery = true;
        }

        // Post.query(function(data){
        //     angular.forEach(data, function(post){
        //         if (post.id == $routeParams.id){
        //             $scope.notFound = false
        //             $scope.post = post
        //         }
        //     })
        // })

        // console.log($routeParams.id)
        // console.log("hello")

        // var blogItems = [
        //     {title: "Some title1", id: 1, description: "this is a book1"},
        //     {title: "Some title2", id: 2, description: "this is a book2"},
        //     {title: "Some title3", id: 3, description: "this is a book3"},
        //     {title: "Some title4", id: 4, description: "this is a book4"}
        // ]
        $scope.order = "title"

        Post.query(function(data) {
            setupCol(data, 4)

        }, function(error) {

        });

        $scope.changeCol = function() {
            if ($scope.numCols == 2) {
                $scope.numCols = 4
            } else {
                $scope.numCols = 2
            }
            setupCol($scope.items, $scope.numCols)
        }

        function setupCol(data, number) {
            if (angular.isNumber(number)) {
                $scope.numCols = number
            } else {
                $scope.numCols = 4
            }
            $scope.cssClass = "col-sm-" + (12 / $scope.numCols)
            $scope.items = data
            $scope.colItems = chunkArrayInGroups(data, $scope.numCols)
        }

        function chunkArrayInGroups(array, unit) {
            var results = [];
            length = Math.ceil(array.length / unit);
            for (var i = 0; i < length; i++) {
                results.push(array.slice(i * unit, (i + 1) * unit));
            }
            return results;
        }

        // $scope.title = "hi there"
        // $scope.click = 0

        // $scope.someClickTest = function() {
        //     console.log("someClickTest")
        //     $scope.click += 1
        //     $scope.title = "some Click " + $scope.click + " times"
        // }

        $scope.goToItem = function(post) {
            console.log("Some itmes");
            $timeout(function() {
                console.log("success")
                $location.path("/blog/" + post.id)
            }, 0);
        }

        // ===========================================================
        // $scope.loadingQuery = false
        // $scope.$watch(function(){
        //     console.log($scope.query)
        //     if ($scope.query != q){
        //         $scope.loadingQuery = true
        //         $scope.cssClass = "col-sm-12"
        //     } else {
        //         if ($scope.loadingQuery){
        //             setupCol($scope.items, 2)
        //             $scope.loadingQuery = false
        //         }
        //     }
        // })


    }
});
