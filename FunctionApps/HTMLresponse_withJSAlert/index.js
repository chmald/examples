module.exports = function (context, req) {

    context.res = {
        // status: 200, /* Defaults to 200 */
        body: page(),
        headers: {
            'Content-Type': 'text/html; charset=utf-8'
        }
    };

    context.done();
};

function page() {
    var my_page = "<html>"
    + "<head><title>Function App Popup</title></head>"
    + "<body style=\"background-color:#ccc;\"><script type=\"text/javascript\">alert(\"Hello!\");</script>"
    + "<div><h1>Welcome to Azure Functions!</h1></div></body>"
    + "</html>";

    return my_page;
}