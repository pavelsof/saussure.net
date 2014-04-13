/* =================================== */
/*  Project: Dragon Derzhanski         */
/* =================================== */

// the god object
var D = {
	
	// constructor
	init: function() {
		D.problems.init();
	},
	
	// app: problems
	problems: {
		dom: {
			get_challenge_button: false,
			challenge_container: false
		},
		init: function() {
			if($('button[data-problem]').length > 0) {
				D.problems.dom.get_challenge_button = $('button[data-problem]');
				D.problems.dom.challenge_container = $('#challenge_container');
				D.problems.dom.get_challenge_button.click(function(e) {
					e.preventDefault();
					D.problems.dom.challenge_container.load(
						'/problems/'+ D.problems.dom.get_challenge_button.data('problem') +'/challenge'
					);
				});
			}
		}
	}
	
}

// brrmm, brrrrm!
$(document).ready(D.init);
