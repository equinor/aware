$(document).ready(function() {

    if ( $(".critical").length ) {
        $("body").css({"background": "red" });
    }
    else if ( $(".warning").length ) {
        $("body").css({"background": "orange" });
    }
    else if ( $(".unknown").length ) {
        $("body").css({"background": "dimgray" });
    }
    else {
        $("body").css({"background": "green" });
   }
});
