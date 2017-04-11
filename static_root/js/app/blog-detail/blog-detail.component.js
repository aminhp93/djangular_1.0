'use strict';

angular.module('blogDetail').
component("blogDetail", {
    templateUrl: "/api/templates/blog-detail.html",
    controller: function($scope, $routeParams, $location, $http, Post) {
        console.log(Post.query())
        console.log(Post.get())

        Post.query(function(data) {
            angular.forEach(data, function(post) {
                if (post.id == $routeParams.id) {
                    $scope.notFound = false;
                    $scope.post = post;
                    resetReply();
                }
            })
        })

        $scope.deleteComment = function(comment){
            $scope.$apply($scope.post.comments.splice(comment, 1))
        }

        $scope.addReply = function() {
            console.log($scope.reply)
            $scope.post.comments.push($scope.reply)

            resetReply()
        }

        function resetReply() {
            $scope.reply = {
                "id": $scope.post.comments.length + 1,
                "text": ""
            }

        }

        // var blogItems = [
        //     { title: "Some title1", id: 1, description: "this is a book1" },
        //     { title: "Some title2", id: 2, description: "this is a book2" },
        //     { title: "Some title3", id: 3, description: "this is a book3" },
        //     { title: "Some title4", id: 4, description: "this is a book4" },

        // ]

        // $scope.title = "Blog " + $routeParams.id

        // angular.forEach(blogItems, function(post){
        //     console.log(post)
        //     if (post.id == $routeParams.id){
        //         $scope.post = post
        //         $scope.notFound = false
        //     }
        // })

        // $http.get("/json/posts.json").then(success, error);

        // function success(response, status, config, statusText) {
        //     $scope.notFound = false
        //     console.log(response.data)
        //     var blogItems = response.data
        //     $scope.post = blogItems
        //     angular.forEach(blogItems, function(post) {
        //         console.log(post)
        //         if (post.id == $routeParams.id) {
        //             $scope.post = post
        //             $scope.notFound = false
        //         }
        //     })
        // }

        // function error(response, status, config, statusText) {
        //     console.log(response)
        // }

        if ($scope.notFound) {
            console.log("Not found")
            $location.path("/404")
        }
    }
});
