$( document ).ready(function() {
	//alert('modal')
	$(document).on('click','#btn-card-1', function(){
		$('.card').hide();
	
		//$('#modal-card-1').modal('show');
	})

	$(document).on('click','.close', function(){
		$('.card').show();
	})

	
});