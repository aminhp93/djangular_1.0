'use strict';

angular.module("confirmClick").directive('confirmClick', function(){
	return {
		restrict: "A",
		link: function(scope, element, attr){
			console.log(attr)
			var msg = attr.confirmClick || "Are you sure"
			var clickAction = attr.confirmedClick;
			element.bind("click", function(e){
				e.stopImmediatePropagation();
				e.preventDefault();
				
				if (window.confirm(msg)){
					scope.$eval(clickAction);
				} else {
					console.log("Canceled")
				}
				
			})
		}
	}
})

// angular.module('confirmClick').directive('confirmClick', function($rootScope, $location){
// 	return {
// 		scope: {
// 			message: "@message",
// 			eq: "=eq",
// 			post: "=post",
// 		},
// 		restrict: "E",
// 		// restrict: "A",
// 		// template: "<a ng-href='/blog/{{post.id}}'/>{{ post.title }} </a>", 
// 		template: "<a ng-href='#'/>{{ post.title }} </a>",
// 		link: function(scope, element, attr){
// 			var msg = scope.message || "are you sure"
// 			element.bind("click", function(e){
// 				if (window.confirm(msg)){
// 					console.log("/blog" + scope.post.id)
// 					$rootScope.$apply(function(){
// 						$location.path("/blog" + scope.post.id)						
// 					})
// 				}
// 			})
// 			console.log(scope, element, attr)
// 		}
// 	}
// })