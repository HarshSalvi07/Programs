const http = require("http");
const server = http.createServer((req, res) => {
    if(req.url == "/") {
        res.write("Hello, this is root");
        res.end();
    }

    else if (req.url === "/about") {
        res.write("Hello, this is about")
        res.end();
    }

    else{
        res.write("Hello, this is else");
    }
});

server.listen(4000);