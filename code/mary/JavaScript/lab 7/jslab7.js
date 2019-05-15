let text = ['myHostname = window.location.hostname;','var myTLD = "." ',' myHostname.substring(myHostname.indexOf("wupload")', '"wupload.".length).split(".")[0];','function afterLoad() {\n return\n}','ieFixForFileSelectionOnChangeEventTimer = null;', 'function ieFixForFileSelectionOnChangeEvent(a) {',' $("#siteName").toggle();','if ($("#inputFileSelection").val() == "")','{\n ieFixForFileSelectionOnChangeEventTimer = setTimeout','("ieFixForFileSelectionOnChangeEvent(), 200)}',' else {\n $(body)[0].focus()\n}"',
'function urlencode(a) {\n return escape(a.toString().replace(/%/g, "%25").replace(/\+/g, "%2B")).replace(/%25/g, "%")\n}','$(document).ajaxStart(function() {',' $("body").addClass("ajaxLoading")});','$(document).ajaxStop(function() {','$("body".removeClass("ajaxLoading")});','$(document).ajaxError(function(d, c, a, b) {','CMApplication.Widgets.Dialog.close();','CMApplication.Widgets.Dialog.displayMessage','(c.responseTextCMApplication.Widgets.Dialog.Types.exception)});', ' ',
'jQuery.setCookie = function(b, c, a) {',' ','var d = new Date();','d.setDate(d.getDate() + a);','cookieDomain = ".wupload" + myTLD;','document.cookie = b + "=" + escape(c) + ((a == null) ? "" : ";expires=" + ','d.toUTCString() + "; path=/;domain=" + cookieDomain + ";")}']


let click=document.getElementById('textarea');

click.addEventListener("keypress", function(){
    event.preventDefault();
    let pick = Math.floor(Math.random()*text.length);
    let list = document.getElementById("textarea");                
    let new_input = document.createTextNode(text[pick]);  
    list.appendChild(new_input);                           
    })


   

    



