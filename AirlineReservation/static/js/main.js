function formClass(formName){


	$("form").addClass("custom-form-css");
	$("form > p").wrapInner("<div class='col-sm-12 col-md-8 article-card article-form'></div>");
	$("input").addClass("form-control");
	$("input[type='submit']").addClass("col-sm-12 col-md-8 btn article-btn btn-primary");
	$(".helptext").addClass("form-text text-muted");
	$("select").addClass("form-control");
	switch(formName){
		case "Login": 
			$("#id_username").addClass("Username");
			$("#id_password").addClass("Password");
		case "AddFlight":
			$("#id_number").addClass("Number");	
			$("#id_source").addClass("Source");
			$("#id_destination").addClass("Destination");
			$("#id_capacity").addClass("Capacity");	
			$("#id_vacancy").addClass("Vacancy");
			$("#id_departure").addClass("Departure");
			$("#id_reach").addClass("Reach");
			$("#id_price_per_head").addClass("Price");
		case "ticket":
			//$("#id_n_passenger").prev().val("Number of Passengers");
			//console.log($("#id_n_passenger"));
	}

}
