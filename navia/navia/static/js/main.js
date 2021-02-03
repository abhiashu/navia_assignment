var user_input = $("#search")
var search_cat = $("#search_category")
var submit_btn = $("#submit-btn")
var search_icon = $('#search-icon')
var artists_div = $('#replaceable-content')
var endpoint = '/medicine/search/'
var delay_by_in_ms = 700
var scheduled_function = false

var ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			artists_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div.html(response['html_from_view'])
				// fade-in the div with new contents
				artists_div.fadeTo('slow', 1)
				// stop animating search icon
				search_icon.removeClass('blink')
			})
		})
}


user_input.on('keyup', function () {
//    alert("hello")
	var request_parameters = {
		q1: $(this).val(), // value of user_input: the HTML element with ID user-input
		q2: search_cat.val()
	}
//	alert(request_parameters)

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})


submit_btn.on('click', function () {
//    alert("hello")
	var request_parameters = {
		q1: user_input.val(), // value of user_input: the HTML element with ID user-input
		q2: search_cat.val()
	}
//	alert(request_parameters)

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
