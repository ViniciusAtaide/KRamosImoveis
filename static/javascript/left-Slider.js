// last update on 26-04-13 14:41

(function($){

    var 

        default_options = {
            timeout : 8000,
            do_timeout : false, 
            animation_time : 400,
            current : 0,
            paddingLeft : 0,

            timing : 'swing',
            slideObjs : '.slide_obj',
            box : '.slide_box',
            paginatorActive : 'active',
            slider : '.slider',
            center_if_has_little : true,
            right_if_has_little : false,
            hide_paginator_if_has_little : true,
            callback_if_has_little : function() {},

            paginator : null,
            prevPaginator : null,
            nextPaginator : null
        },

        toString = Object.prototype.toString;


    function ResponsiveManySlider(father, options) {
        var 
            that = this,
            opt;
        
        opt = $.extend({}, default_options, options);

        this.opt = opt;


        this.timeout = opt['timeout'];
        this.do_timeout = opt['do_timeout'];
        this.center_if_has_little = opt['center_if_has_little'];
        this.right_if_has_little = opt['right_if_has_little'];
        this.callback_if_has_little = opt['callback_if_has_little'];
        this.father = $(father);
        this.box = this.father.find( opt['box'] );
        this.timing = this.father.find( opt['timing'] );
        this.minMargin = parseInt( opt['minMargin'] );
        this.current = parseInt( opt['current'] );
        this.paginatorActive = opt['paginatorActive'];
        this.slider =  this.father.find(opt['slider']);
        this.animation_time = parseInt( opt['animation_time'] );
        this.paddingLeft = parseInt( opt['paddingLeft'] );
        this.slideObjs = this.father.find( opt['slideObjs'] );
        this.childCount = this.slideObjs.length;

        this.init();

        return this;
    };

    ResponsiveManySlider.prototype = {
        init : function () {
            var that = this;

            this.box.css({
                position: 'relative'
            });

            this.appendListeners();

            this.resizer();
            $(window).resize(function(){
                that.resizer();
            });

            this.slideObjs.length > 1 && this.remakeTimeout();

            this.slider.css('position', 'relative');

            this.changePaginator( this.current );

        }

        , appendListeners : function() {
            // testa se tem paginator
            var opt = this.opt,
                that = this;

            if ( toString.call(opt['paginator']) === '[object String]' && opt['paginator'] !== '' ) {
                this.paginator = this.father.find( opt['paginator']);
                this.hasPaginator = this.paginator.length > 0;

                this.paginator.each(function(index){

                    $(this).attr('data-index', index);

                }).click(function(e){

                    if ( e.preventDefault ) {
                        e.preventDefault();
                        e.stopPropagation();
                    }

                    that.set( parseInt($(this).attr('data-index')) );

                    return false;
                });

            } else {
                this.hasPaginator = false;
            }

            // testa se tem prev and next
            if ( toString.call(opt['prevPaginator']) === '[object String]' && opt['prevPaginator'] !== '' ) {
                this.prevPaginator = this.father.find( opt['prevPaginator'] );
                this.hasPrevPaginator = this.prevPaginator.length > 0;

                this.prevPaginator.click(function(e){
                    if ( e.preventDefault ) {
                        e.preventDefault();
                        e.stopPropagation();
                    }

                    that.prev();

                    return false;
                });
            } else {
                this.hasPrevPaginator = false;
            }

            if ( toString.call(opt['nextPaginator']) === '[object String]' && opt['nextPaginator'] !== '' ) {
                this.nextPaginator = this.father.find( opt['nextPaginator'] );
                this.hasNextPaginator = this.nextPaginator.length > 0;

                this.nextPaginator.click(function(e){
                    if ( e.preventDefault ) {
                        e.preventDefault();
                        e.stopPropagation();
                    }

                    that.next();

                    return false;
                });
            } else {
                this.hasNextPaginator = false;
            }
        }

        , resizer : function() {
            this.boxWidth = this.box[0].offsetWidth;
            this.paginate();
            this.animate();

        }

        , paginate : function() {
            var 
                paginator = this.paginator,
                paginator_length,
                AUXpaginator_length_array = [],
                AUXpertenc_to_pag,
                AUXslideObj,
                boxWidth = this.boxWidth,
                slideObjs = this.slideObjs,
                prevPaginator = this.prevPaginator,
                nextPaginator = this.nextPaginator,
                lastTileLeft = 0, paginator_length = 0;

            for ( var i = 0, k = slideObjs.length; i < k; i++ ) {
                AUXslideObj = slideObjs[i];

                if ( AUXslideObj.offsetLeft + AUXslideObj.offsetWidth - lastTileLeft > boxWidth ) {
                    paginator_length++;
                    lastTileLeft = AUXslideObj.offsetLeft;
                }
            }

            paginator_length++;

            if ( paginator !== undefined ) {
                paginator.parent().hide();

                for ( i = 0; i < paginator_length; i++ ) {
                    paginator.eq(i).parent().show();
                }
            }

            this.paginator_length = paginator_length;

            if ( paginator_length <= 1 ) {
                if ( paginator !== undefined ) {
                    paginator.fadeOut(500);
                }
                if ( prevPaginator !== undefined ) {
                    prevPaginator.fadeOut(500);
                }
                if ( nextPaginator !== undefined ) {
                    nextPaginator.fadeOut(500);
                }

                this.callback_if_has_little();
            } else {
                if ( paginator !== undefined ) {
                    paginator.fadeOut(500);

                    for ( i = 0; i < paginator_length; i++ ) {
                        paginator.eq(i).stop().fadeIn(500);
                    }
                }
                if ( prevPaginator !== undefined ) {
                    prevPaginator.fadeIn(500);
                }
                if ( nextPaginator !== undefined ) {
                    nextPaginator.fadeIn(500);
                }
            }

        }

        , remakeTimeout : function() {
            var that = this;
            if ( that.do_timeout ) {
                clearInterval( this.timeout_obj );
                this.timeout_obj = setInterval( function(){
                    that.next();
                } , this.timeout );
            }
        }

        , next : function() {
            this.current++;
            if ( this.current >= this.paginator_length ) {
                this.current = 0;
            }
            this.changePaginator();
            this.animate();
            this.remakeTimeout();
        }

        , prev : function() {
            this.current--;
            if ( this.current < 0 ) {
                this.current = this.paginator_length - 1;
            }
            this.changePaginator();
            this.animate();
            this.remakeTimeout();
        }

        , changePaginator : function() {
            var number = this.current;
            if ( this.paginator && this.paginator.length && this.paginator.length > 0 ) {
                this.paginator.removeClass( this.paginatorActive ).
                    eq( number ).addClass( this.paginatorActive );
            }
        }
 
        , set : function( number ) {
            this.current = number;
            this.animate();
            this.remakeTimeout();
            this.changePaginator();
        }

        , update : function() {
            this.slideObjs = this.father.find( this.opt['slideObjs'] );
            this.childCount = this.slideObjs.length;
            this.paginate();
            this.animate();
        }

        , animate : function() {
            var 
                current = this.current,
                boxWidth = this.boxWidth,
                slideObjs = this.slideObjs,
                AUXslideObj,
                newLeft,
                lastTileLeft= 0,
                currentTile = 0;

            if ( current === 0 ) {
                newLeft = 0;
            } else {
                for ( var i = 0, k = slideObjs.length; i < k; i++ ) {
                    AUXslideObj = slideObjs[i];

                    if ( AUXslideObj.offsetLeft + AUXslideObj.offsetWidth - lastTileLeft > boxWidth ) {
                        currentTile++;
                        lastTileLeft = AUXslideObj.offsetLeft;

                        if ( currentTile === current ) {
                            newLeft = -lastTileLeft;
                        }
                    }
                }
            }


            // testa se o novo left é menor do que o permitido
            if ( slideObjs.length === 0 ) {
                return false;
            }
            var AUXminLeftObj = slideObjs[ slideObjs.length - 1 ],
                minLeft =  boxWidth - ( AUXminLeftObj.offsetLeft + AUXminLeftObj.offsetWidth );



            if ( minLeft > 0 ) {

                if ( this.right_if_has_little ) {

                } else if ( this.center_if_has_little ) {
                    // center
                    minLeft /= 2;
                } else {
                    minLeft = 0;
                }
            }

            newLeft = Math.max( minLeft, newLeft );

            if ( newLeft === minLeft ) {
                newLeft -= this.paddingLeft;
            }

            this.slider.stop(true, true).
                animate({
                    left : newLeft + 'px'
                }, this.animation_time);


        } // animate

    };

    var methods = {
        init : function ( options ) {
            return this.each(function(){
                if( $(this).data('responsiveManySlider') ) {
                    delete( $(this).data('responsiveManySlider') ); 
                }
                
                $(this).data('responsiveManySlider', new ResponsiveManySlider(this, options));
            });
        },
        update : function() {
            return this.each(function(){
                if( !$(this).data('responsiveManySlider') ) {
                    $(this).data('responsiveManySlider', new ResponsiveManySlider(this, options));
                }
                
                $(this).data('responsiveManySlider').update();
                
            });
        },
        remakeTimeout : function() {

        }
    }

    $.fn.responsiveManySlider = function( method ) {

        if ( methods[method] ) {
            return methods[ method ].apply( this, Array.prototype.slice.call( arguments, 1 ));
        } else if ( typeof method === 'object' || ! method ) {
            return methods.init.apply( this, arguments );
        } else {
            $.error( 'Method ' +  method + ' does not exist on jQuery.responsiveManySlider' );
        } 

    }

})(window.jQuery);
