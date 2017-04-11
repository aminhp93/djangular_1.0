'use strict'

angular.module('post').factory("Post", function($resource){
	var url = "/static/json/posts.json"
	return $resource(url, {}, {
		query: {
			method: "GET",
			params: {},
			isArray: true,
			cache: true,
			// transformResponse: function(data, headersGetter, status){
			// 	console.log(data);
			// 	var finalData = angular.fromJson(data);
			// 	return finalData.results
			// }
			// interceptor
		},
		get: {
			method: "GET",
			// params: {"id": @id},
			isArray: true,
			cache: true,

		}
	})

})