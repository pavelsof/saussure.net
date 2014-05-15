/* =================================== */
/*  Project Saussure                   */
/* =================================== */

// the god object
var S = {
	
	// constructor
	init: function() {
		S.problems.init();
	},
	
	// app: problems
	problems: {
		dom: {
			get_challenge_button: false,
			challenge_container: false
		},
		init: function() {
			if($('button[data-problem]').length > 0) {
				S.problems.dom.get_challenge_button = $('button[data-problem]');
				S.problems.dom.challenge_container = $('#challenge_container');
				S.problems.dom.get_challenge_button.click(function(e) {
					e.preventDefault();
					S.problems.dom.challenge_container.load(
						'/problems/'+ S.problems.dom.get_challenge_button.data('problem') +'/challenge'
					);
				});
			}
		}
	}
	
};

// brrmm, brrrrm!
$(document).ready(S.init);
