'use strict';

angular.module('blogDetail').
component("blogDetail", {
    templateUrl: "/api/templates/blog-detail.html",
    controller: function(Comment, $cookies, $scope, $routeParams, $location, $http, Post) {
        console.log(Post.query())
        console.log(Post.get())
        var slug = $routeParams.slug

        Post.get({ "slug": $routeParams.slug }, function(data) {
            $scope.post = data
            // $scope.comments = data.comments
            Comment.query({"slug": slug, "type": "post"}, function(data){
                $scope.comments = data
            })
            console.log(data);
            console.log($scope.comments, "scope comments")
        })

        // Post.query(function(data) {
        //     angular.forEach(data, function(post) {
        //         if (post.id == $routeParams.id) {
        //             $scope.notFound = false;
        //             $scope.post = post;
        //             resetReply();
        //         }
        //     })
        // })

        $scope.deleteComment = function(comment) {
            $scope.$apply($scope.post.comments.splice(comment, 1))
        }

        // curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im1pbmhAZ21haWwuY29tIiwidXNlcl9pZCI6MSwiZXhwIjoxNDkxNDUwMDQ0LCJ1c2VybmFtZSI6ImFtaW4ifQ.oPPaO5NbqIb3wokYsLEaPeZrDx5p8G_wIXE2riMiD0g" -H "Content-Type: application/json" -d '{"content":"TEst Content"}' 'http://localhost:8000/api/comments/create/?slug=post-2&type=post'


        $scope.addReply = function() {
            console.log($scope.reply)
            var token = $cookies.get("token")
            if (token) {
                var req = {
                    method: "POST",
                    url: "http://localhost:8000/api/comments/create/?slug=" + slug + "&type=post",
                    data: {
                        content: $scope.reply.content
                    },
                    headers: {
                        authorization: "JWT" + token
                    }
                }

                console.log($scope.reply.content, "|||||||", slug, "======", token, req)
                var requestAction = $http(req)
                console.log(requestAction, "WOOOOO");
                console.log($scope.comments);
                requestAction.success(function(r_data, r_status, r_headers, r_config){
                    $scope.comments.push($scope.reply);
                    resetReply();
                })

                requestAction.error(function(e_data, e_status, e_headees, e_config){
                    console.log(e_data);
                })

                // $scope.comments.push($scope.reply)
                // resetReply()
            } else {
                console.log("No token")
            }

        }

        function resetReply() {
            $scope.reply = {
                "id": $scope.post.comments.length + 1,
                "content": ""
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
