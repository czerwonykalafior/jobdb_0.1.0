//$('#').keyup(function(){
//        var query;
//        query = $(this).val();
//        $.get('/addjob/suggest_pl_job/', {suggestion: query}, function(data){
//         $('#cats').html(data);
//        });
//});

$(function() {
            $( "#pl_job" ).autocomplete({
               source: "/addjob/suggest_pl_job/",
               minLength: 2
            });
         });

$(function() {
            $( "#eng_job" ).autocomplete({
               source: "/addjob/suggest_eng_job/",
               minLength: 2
            });
         });