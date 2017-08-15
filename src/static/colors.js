$(document).ready(function() {

    /* For each critical, warning or unknown table row, see if they have table column
     * with a class named 'checkSilenced' which contains a text different from 'No'
     * Then, if that is true, add the silenced class giving a green color to the row */
    $(".critical, .warning, .unknown").each(function() {
       $(this).find(".checkSilenced:not(:contains('No'))").parent().addClass("silenced");
    });

    /* After the code above have 'cleaned' up the classes,
     * set the background color to the most severe unsilenced event */
    if ( $(".critical:not(.silenced)").length ) {
        $("body").css({"background": "red" });
    }
    else if ( $(".warning:not(.silenced)").length ) {
        $("body").css({"background": "orange" });
    }
    else if ( $(".unknown:not(.silenced)").length ) {
        $("body").css({"background": "dimgray" });
    }
    else {
        $("body").css({"background": "green" });
   }

});
