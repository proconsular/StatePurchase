$(document).ready(function() {
  var id = -1;
  var state_id = Number($('.state_id').text());
  var crime_stat = Number($('.crime_stat').text());

  $('.info_panel').hide();
  $('.state-status').hide();

  if (crime_stat >= 50 && crime_stat < 70) {
    $('.state-status').show();
    $('.rebellion').removeClass('hidden');
  }else if (crime_stat >= 70 && crime_stat < 90) {
    $('.state-status').show();
    $('.anarachy').removeClass('hidden');
  }else if (crime_stat >= 90) {
    $('.state-status').show();
    $('.collapse').removeClass('hidden');
  }

  $('.building').click(function() {
    if (id != -1) {
      $('.building_' + id).removeClass('building_selected');
    }
    id = $(this).attr('id');
    $(this).addClass('building_selected');
    $('.info_panel').show();
    $.ajax({
      url: "/data/buildings/" + id,
      method: "GET",
      success: function(data) {
        var obj = JSON.parse(data);
        $('.info_panel h1').text(obj.type);
        var status = "Healthy";
        if (obj.status == 1) {
          status = "Rundown";
        }else if (obj.status == 0){
          status = "Abandoned";
        }
        var cleanliness = "Clean";
        if (obj.cleanliness == 2) {
          cleanliness = "Littered";
        }else if (obj.cleanliness == 1){
          cleanliness = "Dirty";
        }else if (obj.cleanliness == 0){
          cleanliness = "Vandalized";
        }
        var ec = "Highly Efficent";
        if (obj.efficency == 1) {
          ec = "Mediocre";
        }else if (obj.efficency == 0){
          ec = "Poor";
        }
        var sz = "Small";
        if (obj.size >= 3 && obj.size < 7) {
          sz = "Medium";
        }else if (obj.size >= 7){
          sz = "Large";
        }
        var html = ""
        html += "<div>Status: "+ status +"</div>";
        html += "<div>Cleanliness: "+ cleanliness +"</div>";
        html += "<div>Efficency: "+ ec +"</div>";
        html += "<div>Size: "+ obj.size +" / 10</div>";
        if (obj.status != 2) {
          html += "<a class='fix-button' href='/fix/buildings/"+id+"'>Fix (2.5m)</a>"
        }
        $('.info_panel .content').html(html);
      }
    });
  });

  $('.company').click(function() {
    var id = $(this).attr('id');
    $('.info_panel').show();
    $.ajax({
      url: "/data/companies/" + id,
      method: "GET",
      success: function(data) {
        var obj = JSON.parse(data);
        $('.info_panel h1').text("Company");
        var ec = "Highly Efficent";
        if (obj.efficency == 1) {
          ec = "Mediocre";
        }else if (obj.efficency == 0){
          ec = "Poor";
        }
        var html = ""
        html += "<div>Tech Lvl.: "+ obj.tech +"</div>";
        html += "<div>Efficency: "+ ec +"</div>";
        html += "<div>Size: "+ obj.size +" / 10</div>";
        $('.info_panel .content').html(html);
      }
    });
  });

  $('.upgrades_menu_button').click(function() {
    $('.menu_home').hide();
    $('.menu_upgrades').removeClass("hidden");
    return false;
  });

  $('.main_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_home').show();
    return false;
  });

  $('.traffic_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_traffic').removeClass("hidden");
    return false;
  });

  $('.police_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_police').removeClass("hidden");
    return false;
  });

  $('.education_upgrades_button').click(function() {
    $(this).parent().parent().addClass("hidden");
    $('.menu_upgrades_education').removeClass("hidden");
    return false;
  });

  $('.maintenance_menu_button').click(function() {
    $(this).parent().parent().hide();
    $('.menu_maintenance').removeClass("hidden");
    return false;
  });

  $('.strategy_menu_button').click(function() {
    $(this).parent().parent().hide();
    $('.menu_strategy_sel').removeClass("hidden");
    return false;
  });

  var targetedState = -1;
  $('.target_state_sel').change(function() {
    $('.target_state_sel option:selected').each(function() {
      targetedState = $(this).attr("value");
    });
  });

  $('.target_button').click(function() {
    if (targetedState != -1) {
      $(this).parent().parent().addClass("hidden");
      $('.menu_strategy').removeClass("hidden");
    }
    return false;
  });

  $('.stragety_crime').click(function() {
    var url = "/states/" + state_id + "/attack/" + targetedState + "/crime";
    $.get(url).done(function() {
      location.reload();
    });
    return false;
  });

  $('.stragety_road').click(function() {
    var url = "/states/" + state_id + "/attack/" + targetedState + "/road";
    $.get(url).done(function() {
      location.reload();
    });
    return false;
  });

  $('.stragety_pop').click(function() {
    var url = "/states/" + state_id + "/attack/" + targetedState + "/population";
    $.get(url).done(function() {
      location.reload();
    });
    return false;
  });

});
