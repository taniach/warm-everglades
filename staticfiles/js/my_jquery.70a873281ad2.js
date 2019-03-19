$(document).ready(function() {

        // JQuery code to be added in here.
        $(document).on('click', '.confirm-delete', function(){
		    return confirm('Are you sure you want to delete this?');
		})
});