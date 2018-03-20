/*

 Request body:
    {
        "to": "to@email.com",
        "from": "sender@email.com",
        "subject": "Subject line for email",
        "message": "Your emails content"
    }

Integration required:
    Outputs: SendGrid (message)
    https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-sendgrid

*/

module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    context.res = {
        status: 200,
        body: "Boom!"
    };

    context.bindings.message = {
         "personalizations": [ { "to": [ { "email": req.body.to } ] } ],
        from: { email: req.body.from },        
        subject: req.body.subject,
        content: [{
            type: 'text/plain',
            value: req.body.message
        }]
    };

    context.done();
    
};