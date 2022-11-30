$(document).ready(function(){
    $('.header').height($(window).height());
    if(document.getElementById('Tname').innerHTML!=''){
        var comcols=["Name", "Rank", "Country"];
    var battcols=["ID", "Name", "Description", "Armor Lost, Axis", "Aircraft Lost, Axis", "Carriers Lost, Axis", "Battleships Lost, Axis", "Cruisers Lost, Axis", "Destroyers Lost, Axis", "Submarines Lost, Axis", "Casualties, Axis", "Armor Lost, Allies", "Aircraft Lost, Allies", "Carriers Lost, Allies", "Battlehsips Lost, Allies", "Cruisers Lost, Allies", "Destroyers Lost, Allies", "Submarines Lost, Allies", "Casualties, Allies", "Part Of (ID)"];
    var milcols=["Country", "Name", "Type"];
    var shipcols=["Name", "Type", "Country", "Sunk By", "Sunk Date"];
    var countrycols=["Name", "Max Ground Strength", "No. of Carriers", "No. of Battleships", "No. of Cruisers", "No. of Destroyers", "No. of Submarines", "No. of Fighters", "No. of Bombers", "Armor Lost", "Aircraft Lost", "Carriers Lost", "Battleships Lost", "Cruisers Lost", "Destroyers Lost", "Submarines Lost", "Military Casualties", "Civilian Casualties"];
    var surrendercols=["Surrendering country", "Country accepting surrender", "Date of surrender"];
    var warcols=["Country declaring war", "Country being declared war on", "Date of declaration"];
    var eventcols=["ID", "Country 1 involved", "Country 2 involved", "Date", "Description"];
    var placecols=["Place", "Country"];
    var commandmcols=["Commander", "Country", "Military name", "Start Date", "End Date"];
    var hascols=["ID", "Place", "Axis armies ID", "Allied armies ID", "Start Date", "End Date"];
    var hasscols=["Ship", "Country", "Military name", "Start Date", "End Date"];
  
    var comtype=['(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)'];
    var batttype=['(Numeric)', '(Alphanumeric)', '(Alphanumeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)'];
    var miltype=['(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)'];
    var shiptype=['(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)', '(Date)'];
    var countrytype=['(Alphanumeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)', '(Numeric)'];
    var surrendertype=['(Alphanumeric)', '(Alphanumeric)', '(Date)'];
    var wartype=['(Alphanumeric)', '(Alphanumeric)', '(Date)'];
    var eventtype=['(Numeric)', '(Alphanumeric)', '(Alphanumeric)', '(Date)', '(Alphanumeric)'];
    var placetype=['(Alphanumeric)', '(Alphanumeric)'];
    var commandmtype=['(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)', '(Date)', '(Date)'];
    var hastype=['(Numeric)', '(Alphanumeric)', '(Numeric)', '(Numeric)', '(Date)', '(Date)'];
    var hasstype=['(Alphanumeric)', '(Alphanumeric)', '(Alphanumeric)', '(Date)', '(Date)'];
  
    var comPK=comcols.slice(0,1); var comK=comcols.slice(1);
    var battPK=battcols.slice(0,1); var battK=battcols.slice(1);
    var milPK=milcols.slice(0,2); var milK=milcols.slice(2);
    var shipPK=shipcols.slice(0,1); var shipK=shipcols.slice(1);
    var countryPK=countrycols.slice(0,1); var countryK=countrycols.slice(1);
    var surrenderPK=surrendercols.slice(0,1); var surrenderK=surrendercols.slice(1);
    var warPK=warcols.slice(0,2); var warK=warcols.slice(2);
    var eventPK=eventcols.slice(0,1); var eventK=eventcols.slice(1);
    var placePK=placecols.slice(0,1); var placeK=placecols.slice(1);
    var commandmPK=commandmcols.slice(0,3); var commandmK=commandmcols.slice(3);
    var hasPK=hascols.slice(0,4); var hasK=hascols.slice(4);
    var hassPK=hasscols.slice(0,3); var hassK=hasscols.slice(3);
  
    var comvar=['NAME', 'COMRANK', 'CNAME'];
    var battvar=['ID', 'NAME', 'DESCR', 'AXISNUMARMORL', 'AXISNUMAIRCRAFTL', 'AXISNUMCVL', 'AXISNUMBBL', 'AXISNUMCL', 'AXISNUMDDL', 'AXISNUMSSL', 'AXISCASUALTY', 'ALLIEDNUMARMORL', 'ALLIEDNUMAIRCRAFTL', 'ALLIEDNUMCVL', 'ALLIEDNUMBBL', 'ALLIEDNUMCL', 'ALLIEDNUMDDL', 'ALLIEDNUMSSL', 'ALLIEDCASUALTY', 'PARTOF'];
    var milvar=['CNAME', 'NAME', 'TYPE'];
    var shipvar=['NAME', 'TYPE', 'CNAME', 'SUNKBY', 'SUNKDATE'];
    var countryvar=['NAME', 'MAXGSTR', 'NUMCV', 'NUMBB', 'NUMC', 'NUMDD', 'NUMSS', 'NUMFIGHT', 'NUMBOMB', 'NUMARMORL', 'NUMAIRCRAFTL', 'NUMCVL', 'NUMBBL', 'NUMCL', 'NUMDDL', 'NUMSSL', 'MCASUALTY', 'CCASUALTY'];
    var surrendervar=['C1', 'C2', 'DDATE'];
    var warvar=['C1', 'C2', 'DDATE'];
    var eventvar=['ID', 'C1', 'C2', 'SDATE', 'DESCR'];
    var placevar=['NAME', 'CNAME'];
    var commandmvar=['COMNAME', 'MCNAME', 'MNAME', 'SDATE', 'EDATE'];
    var hasvar=['ID', 'PNAME', 'AXISKEY', 'ALLIEDKEY', 'SDATE', 'EDATE'];
    var hassvar=['SHIP', 'MCNAME', 'MNAME', 'SDATE', 'EDATE'];
  
    var aItems = [];
    var aVar=[];
    var aType=[];
    var PK=[];
    var K=[];
    var tablename='';
                  var tname=document.getElementById('Tname').innerHTML;
                  if(tname == "Commander"){
                  aItems = comcols;
                  aVar = comvar;
                  aType=comtype;
                  PK=comPK;
                  K=comK;
                } else if (tname == "Military") {
                  aItems = milcols;
                  aVar = milvar;
                  aType=miltype;
                  PK=milPK;
                  K=milK;
                } else if(tname == "Battle") {
                  aItems = battcols;
                  aVar = battvar;
                  aType=batttype;
                  PK=battPK;
                  K=battK;
                } else if(tname == "Ship") {
                  aItems = shipcols;
                  aVar = shipvar;
                  aType=shiptype;
                  PK=shipPK;
                  K=shipK;
                } else if(tname == "COMMANDM"){
                  aItems = commandmcols;
                  aVar = commandmvar;
                  aType=commandmtype;
                  PK=commandmPK;
                  K=commandmK;
                } else if(tname == "Country"){
                  aItems = countrycols;
                  aVar = countryvar;
                  aType=countrytype;
                  PK=countryPK;
                  K=countryK;
                } else if(tname == "Event"){
                  aItems = eventcols;
                  aVar = eventvar;
                  aType=eventtype;
                  PK=eventPK;
                  K=eventK;
                } else if(tname == "has"){
                  aItems = hascols;
                  aVar = hasvar;
                  aType=hastype;
                  PK=hasPK;
                  K=hasK;
                } else if(tname == "hass"){
                  aItems = hasscols;
                  aVar = hassvar;
                  aType=hasstype;
                  PK=hassPK;
                  K=hassK;
                } else if(tname == "Place"){
                  aItems = placecols;
                  aVar = placevar;
                  aType=placetype;
                  PK=placePK;
                  K=placeK;
                } else if(tname == "Surrender"){
                  aItems = surrendercols;
                  aVar = surrendervar;
                  aType=surrendertype;
                  PK=surrenderPK;
                  K=surrenderK;
                } else if(tname == "War"){
                  aItems = warcols;
                  aVar = warvar;
                  aType=wartype;
                  PK=warPK;
                  K=warK;
                }
                //window.alert(tname);
              }
      $('[data-toggle="tooltip"]').tooltip();
      var actions = $("table td:last-child").html();
      // Append table with add row form on add new button click
        $(".add-new").click(function(){
        $(this).attr("disabled", "disabled");
        var index = $("table tbody tr:last-child").index();
            var row = '<tr>';
            for(i=0; i<aItems.length; i++){
              row = row + '<td><input type="text" class="form-control" name="'+aVar[i]+'" id="'+aVar[i]+'"></td>'
            }
            row = row + '<td>' + '<p id="getaction" style="display: none">0101</p><a class="add" title="Add" data-toggle="tooltip"><i class="material-icons">&#xE03B;</i></a><a class="edit" title="Edit" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a><a class="delete" title="Delete" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a>' + '</td>' + '</tr>';
                
          $("table").append(row);		
        $("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
            $('[data-toggle="tooltip"]').tooltip();
            
        });
      // Add row on add button click
      $(document).on("click", ".add", function(){
        var empty = false;
        var input = $(this).parents("tr").find('input[type="text"]');
            input.each(function(){
          if(!$(this).val()){
            $(this).addClass("error");
            empty = true;
          } else{
                    $(this).removeClass("error");
                }
        });
        
        $(this).parents("tr").find(".error").first().focus();
        if(!empty){
          input.each(function(){
            $(this).parent("td").html($(this).val());
          });			
          $(this).parents("tr").find(".add, .edit").toggle();
          
          $(".add-new").removeAttr("disabled");
        }		
        });
      // Edit row on edit button click
      $(document).on("click", ".edit", function(){		
            $(this).parents("tr").find("td:not(:last-child):not(.PK").each(function(){
          $(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
        });		
        $(this).parents("tr").find(".add, .edit").toggle();
        var rows=$(this).parents("tr");
        var lastele=rows[rows.length-1];
        var actiontype=lastele.getElementsByTagName("p");
        var initialinner=actiontype[0].innerHTML;
        actiontype[0].innerHTML=initialinner.charAt(0)+initialinner.charAt(1)+'1'+initialinner.charAt(3);
        
        $(".add-new").attr("disabled", "disabled");
        });
      // Delete row on delete button click
      $(document).on("click", ".delete", function(){
          var rows=$(this).parents("tr");
          var lastele=rows[rows.length-1];
          var actiontype=lastele.getElementsByTagName("p");
          var initialinner=actiontype[0].innerHTML;
          //window.alert(initialinner);
          for(i=0;i<rows.length;i++){
            if(rows[i].style.background=='red'){
                rows[i].style.background='';
                if(initialinner.charAt(0)=='1'){
                    actiontype[0].innerHTML='0'+initialinner.charAt(1)+initialinner.charAt(2)+initialinner.charAt(3);
                }
            }else{
                rows[i].style.background='red';
                if(initialinner.charAt(0)=='0'){
                    actiontype[0].innerHTML='1'+initialinner.charAt(1)+initialinner.charAt(2)+initialinner.charAt(3);
                }
            }
          }
          
            //$(this).parents("tr").remove();
        //$(".add-new").removeAttr("disabled");
        });
	

	var battle=["Country", "Date", "Description", "Military", "Name", "Place"];
    var command=["Country", "Name", "Rank"];
    var military=["Commander", "Country", "Date", "Name"];
    var ship=["Country", "Name", "Type"];
    var event=['Country', 'Date', 'Description'];
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
	} else if(this.value == "Event"){
        aItems = event;
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

    var visibilityvar=document.getElementById("visibilityvar");
    if(visibilityvar.innerHTML=="True"){
        document.getElementById("visibilitydiv").style.display="block";
    }else {
        document.getElementById("visibilitydiv").style.display="none";
    }
/*
    function searchtab2() {
        // Declare variables
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");
      
        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[0];
          if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          }
        }
      }*/
	
   });

