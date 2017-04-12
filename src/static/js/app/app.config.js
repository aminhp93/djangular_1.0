'use strict';

angular.module('app').config(function($resourceProvider, $routeProvider, $locationProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;

    $routeProvider
    	.when('/', {
    		template: "<blog-list></blog-list"
    	})
    	.when('/about', {
    		templateUrl: "/api/templates/about.html"
    	})
        .when('/blog', {
            // template: "<blog-list></blog-list>"
            redirectTo: '/'
        })
        .when('/login', {
            template: "<login-detail></login-detail>"
        })
        .when("/logout", {
            redirectTo: "/login"
        })
        .when('/blog/:slug/', {
        	template: "<blog-detail></blog-detail>"
        })
        // .when('/blog/:id/', {
        //     template: "<blog-list></blog-list>"
        // })
        .otherwise({
        	template: "Not Found"
        })

    $locationProvider.html5Mode({
    	enabled:true,
    })
});
