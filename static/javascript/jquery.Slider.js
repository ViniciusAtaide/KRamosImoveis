'use strict';
(function ($) {
	$.fn.Slider = function(attrs) {
		var defaults = {
			items : '.slide',
			linkproximo : '.next',
			linkpaginador : '.paginador',
			linkanterior : '.prev',
			selector : '.selector',
			timeout : 5000
		};
		// constrói a função nos defaults para cada campo em branco
		var opcoes = $.extend(defaults, attrs);

		//seletores	
		var $lista = $(opcoes.items);
		var $prox = $(opcoes.linkproximo);
		var $ant = $(opcoes.linkanterior);
		var $paginador = $(opcoes.linkpaginador);
		var $seletor = $(opcoes.selector);
		var $wrapper = $('.wrapper');
		///////////////////////////
		var timeout = opcoes.timeout;
		var timing = opcoes.timing;
		var prop = opcoes.property;
		var tempo = opcoes.tempoAnim;
		var i=0,interval_obj;

		// css do slider		

		/////////////////////////		

		function remakeInterval() {
			clearInterval(interval_obj);
			interval_obj = setInterval(function() {
				trocaPagina(1);	 
			}, timeout);
		}

		//ciclo de controle
		return this.each(function() {
			$paginador.eq(0).addClass('ativo');
			// proxima pagina
			$prox.click(function() {
				remakeInterval();
				trocaPagina(1);
			});
			// página anterior
			$ant.click(function() {
				remakeInterval();
				trocaPagina(2);
			});
			
			// mouse no numero
			$paginador.click(function() {
				remakeInterval();
				trocaPagina(3,this);
			});
			//timer entre a troca de imagens
			remakeInterval();
		});
		///
		function trocaPagina(caso,pagina) {
			//Foto Atual
			$lista.removeClass('ativo');
			$paginador.removeClass('ativo');
			//////////////////////////////////////////////////
			// Caso seja para a proxima
			switch (caso) {
				//proxima pagina
				case 1:
					i++;
					if (i >= $lista.length)
						i=0;
					break;
				//pagina anterior
				case 2:
					i--;
					if (i < 0)
						i=$lista.length-1;
				break;
				//pagina clicada diretamente
				case 3:
					i = $(pagina).attr("data-val");
			}

			///////////////////////////////////////////////////
			// Proxima foto
			$lista.eq(i).addClass('ativo');
			$paginador.eq(i).addClass('ativo');
			$paginador.eq(i).addClass('active');

		}
	};
})(jQuery);
