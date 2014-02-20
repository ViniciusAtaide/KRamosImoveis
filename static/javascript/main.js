angular.module('KleberImoveis', ['ngAnimate', 'ngRoute'])
  .config(function($routeProvider) {
    $routeProvider.when('index', {
        templateUrl: 'partials/index.html',
        controller: 'indexCtrl'
    }).when('lista', {
        templateUrl: 'partials/lista.html',
        controller: 'listaCtrl'
    }).when('detalhe', {
        templateUrl: 'partials/detalhe.html',
        controller: 'detalheCtrl'
    }).otherwise({
        redirectTo: 'index'
    });

  });