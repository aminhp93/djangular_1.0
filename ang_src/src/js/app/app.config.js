'use strict';

angular.module('app').config(function($routeProvider, $locationProvider) {
    $routeProvider
    	.when('/', {
    		template: "<blog-list></blog-list"
    	})
    	.when('/about', {
    		templateUrl: "templates/about.html"
    	})
        .when('/blog', {
            // template: "<blog-list></blog-list>"
            redirectTo: '/'
        })
        .when('/blog/:id/', {
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
