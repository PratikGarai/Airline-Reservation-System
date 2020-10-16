function formClass(formName){
	$("form").addClass("custom-form-css");
	$("form > p").wrapInner("<div class='col-sm-12 col-md-8 article-card article-form'></div>");
	$("input").addClass("form-control");
	$("input[type='submit']").addClass("col-sm-12 col-md-8 btn article-btn btn-primary");
	$(".helptext").addClass("form-text text-muted");
	$("select").addClass("form-control");
	$(".custom-form-css").css({"border-style": "ridge","margin":"0px 100px", "padding":"50px", "border-radius":"10px"});
	switch(formName){
		// case "Login": 
		// 	$("#id_username").addClass("Username");
		// 	$("#id_password").addClass("Password");
		// 	break;
		// case "AddFlight":
		// 	$("#id_number").addClass("Number");	
		// 	$("#id_source").addClass("Source");
		// 	$("#id_destination").addClass("Destination");
		// 	$("#id_capacity").addClass("Capacity");	
		// 	$("#id_vacancy").addClass("Vacancy");
		// 	$("#id_departure").addClass("Departure");
		// 	$("#id_reach").addClass("Reach");
		// 	$("#id_price_per_head").addClass("Price");
		// 	break;
		case "ticket":
			const label = $("#id_n_passenger").prev()[0];
			label.textContent = "Number of Passengers";
	}

}
