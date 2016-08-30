var restify = require("restify");

var server = restify.createServer();

server.get("/nouns", function (request, response, next) {
    response.end("All nouns details are listed");
    return next();
});

server.get("/nouns/:id", function (request, response, next) {
    var id = request.params.id;
    response.end("noun with id " + id + " is listed");
    return next();
});

server.post("/nouns/:id", function (request, response, next) {
    var id = request.params.id;
    response.end("noun details of " +  id  + " is inserted successfully");
    return next();
});

server.put("/nouns/:id", function (request, response, next) {
    var id = request.params.id;
    response.end("noun with id " + id + " is updated");
    return next();
});

server.del("/nouns/:id", function (request, response, next) {
    var id = request.params.id;
    response.end("noun with id " + id + " is deleted");
    return next();
});

server.listen(5000, "0.0.0.0", function() {
    console.log("Listening to the address " + server.url)
});
