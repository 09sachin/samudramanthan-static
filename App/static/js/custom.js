/*global $:false, jQuery:false, console:false */
jQuery(document).ready(function($) {
  "use strict";

  // Create the dropdown base
  $("<select />").appendTo("nav");

  // Create default option "Go to..."
  $("<option />", {
    "selected": "selected",
    "value": "",
    "text": "Go to..."
  }).appendTo("nav select");

  // Populate dropdown with menu items
  $("nav a").each(function() {
    var el = $(this);
    $("<option />", {
      "value": el.attr("href"),
      "text": el.text()
    }).appendTo("nav select");
  });
  // To make dropdown actually work
  // To make more unobtrusive: http://css-tricks.com/4064-unobtrusive-page-changer/
  $("nav select").change(function() {
    window.location = $(this).find("option:selected").val();
  });

  //$('.cover').css(top:'100%');
  $('.thumb-wrapp').hover(function() {
    $('.folio-image', this).stop().animate({
      bottom: '20px'
    }, {
      queue: false,
      duration: 300
    });
    $('.folio-caption', this).stop().animate({
      bottom: '-20px'
    }, {
      queue: false,
      duration: 300
    });
  }, function() {
    $('.folio-image', this).stop().animate({
      bottom: '0'
    }, {
      queue: false,
      duration: 300
    });
    $('.folio-caption', this).stop().animate({
      bottom: '0'
    }, {
      queue: false,
      duration: 300
    });
  });
  $('ul.nav li.dropdown').hover(function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
  }, function() {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
  });
 
  $('.navigation').onePageNav({
    begin: function() {
      console.log('start');
    },
    end: function() {
      console.log('stop');
    },
    scrollOffset: 0
  });

});


$(window).scroll(function() {
  "use strict";
  if ($(window).scrollTop() < 10) {

    $('.fade').stop(true, true).fadeTo("slow", 1);
  } else {
    $('.fade').stop(true, true).fadeTo("slow", 0.33);
  }
});

var text = $(".split");

var split = new SplitText(text);

function random(min, max){
	return (Math.random() * (max - min)) + min;
}
