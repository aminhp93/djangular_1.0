'use strict'

angular.module('comment').factory("Comment", function($resource){
	// var url = "/static/json/posts.json"
	var url = "/api/comments/:slug/"
	var commentQuery = {
		url: url,
		method: "GET",
		params: {},
		isArray: true,
		cache: false,
		transformResponse: function(data, headersGetter, status){
			var finalData = angular.fromJson(data)
			return finalData.results

		}
	}

	var commentGet = {
		url: url + ":id/",
		method: "GET",
		params: {"id": "@id"},
		isArray: false,
		cache: false,
	}
	return $resource(url, {}, {
		query: commentQuery,
		get: commentGet,
	})

})