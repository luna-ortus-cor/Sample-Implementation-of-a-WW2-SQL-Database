$(document).ready(function(){
    $('.header').height($(window).height());
    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

    var battle=["Country", "Date", "Description", "Military", "Name", "Place"];
    var command=["Country", "Name", "Rank"];
    var military=["Commander", "Country", "Date", "Name"];
    var ship=["Country", "Name", "Type"];
    document.getElementById("cat").addEventListener("change", function(e){
        var select2 = document.getElementById("by");
        select2.innerHTML = "";
        var aItems = [];
    if(this.value == "Commander"){
        aItems = command;
    } else if (this.value == "Military") {
        aItems = military;
    } else if(this.value == "Battle") {
        aItems = battle;
    } else if(this.value == "Ship") {
        aItems = ship;
    }
    for(var i=0,len=aItems.length; i<len;i++) {
        var option = document.createElement("option");
        option.value= (i+1);
        var textNode = document.createTextNode(aItems[i]);
        option.appendChild(textNode);
        select2.appendChild(option);
    }

    }, false);

    var comcols=["Name", "Rank", "Country"];
    var battcols=["ID", "Name", "Description", "Armor Lost, Axis", "Aircraft Lost, Axis", "Carriers Lost, Axis", "Battleships Lost, Axis", "Cruisers Lost, Axis", "Destroyers Lost, Axis", "Submarines Lost, Axis", "Casualties, Axis", "Armor Lost, Allies", "Aircraft Lost, Allies", "Carriers Lost, Allies", "Battlehsips Lost, Allies", "Cruisers Lost, Allies", "Destroyers Lost, Allies", "Submarines Lost, Allies", "Casualties, Allies", "Part Of (ID)"];
    var milcols=["Country", "Name", "Type"];
    var shipcols=["Name", "Type", "Country", "Sunk By", "Sunk Date"];
    var countrycols=["Name", "Max Ground Strength", "No. of Carriers", "No. of Battleships", "No. of Cruisers", "No. of Destroyers", "No. of Submarines", "No. of Fighters", "No. of Bombers", "Armor Lost", "Aircraft Lost", "Carriers Lost", "Battleships Lost", "Cruisers Lost", "Destroyers Lost", "Submarines Lost", "Military Casualties", "Civilian Casualties"];
    var surrendercols=["Surrendering country", "Country accepting surrender", "Date of surrender"];
    var warcols=["Country declaring war", "Country being declared war on", "Date of declaration"];
    var eventcols=["ID", "Country 1 involved", "Country 2 involved", "Date", "Description"];
    var placecols=["Place name", "Country"];
    var commandmcols=["Commander", "Country", "Military name", "Start Date", "End Date"];
    var hascols=["ID", "Place", "Axis armies ID", "Allied armies ID", "Start Date", "End Date"];
    var hasscols=["Ship", "Country", "Military name", "Start Date", "End Date"];
	document.getElementById("tables").addEventListener("change", function(e){
		var select3 = document.getElementById("sort");
		select3.innerHTML = "";
		var aItems = [];
	if(this.value == "Commander"){
		aItems = comcols;
	} else if (this.value == "Military") {
		aItems = milcols;
	} else if(this.value == "Battle") {
		aItems = battcols;
	} else if(this.value == "Ship") {
		aItems = shipcols;
	} else if(this.value == "COMMANDM"){
		aItems = commandmcols;
	} else if(this.value == "Country"){
		aItems = countrycols;
	} else if(this.value == "Event"){
		aItems = eventcols;
	} else if(this.value == "has"){
		aItems = hascols;
	} else if(this.value == "hass"){
		aItems = hasscols;
	} else if(this.value == "Place"){
		aItems = placecols;
	} else if(this.value == "Surrender"){
		aItems = surrendercols;
	} else if(this.value == "War"){
		aItems = warcols;
	}
	for(var i=0,len=aItems.length; i<len;i++) {
		var option = document.createElement("option");
		option.value= (i+1);
		var textNode = document.createTextNode(aItems[i]);
		option.appendChild(textNode);
		select3.appendChild(option);
	}
	}, false);

	$(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });
    
    $(".zoom").hover(function(){
		
		$(this).addClass('transition');
	}, function(){
        
		$(this).removeClass('transition');
	});
    
   })

