'use strict';

angular.module('app', [
	// external
	'angularUtils.directives.dirPagination',
	'ngResource',
	'ngRoute',
	'ui.bootstrap',

	// internal
	'blogDetail',
	'blogList',
	'confirmClick',
	'tryNav',
	]);