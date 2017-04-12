'use strict';

angular.module('app', [
	// external
	'angularUtils.directives.dirPagination',
	'ngCookies',
	'ngResource',
	'ngRoute',
	'ui.bootstrap',

	// internal
	'blogDetail',
	'blogList',
	'confirmClick',
	'loginDetail',
	'tryNav',
	]);