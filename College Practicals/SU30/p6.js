const { write } = require("fs")
const http = require("http")
const app = http.createServer((req,res) =>{
    const  url = req.url

    if("/" === url){
        res.write("This is home page")
        res.end()
    }

    else if("/about" === url){
        res.write("This is about page")
        res.end()
    }

    else if("/login" === url){
        res.write("This is login page")
        res.end()
    }

    else{
        res.write("Page not found")
        res.end()
    }
})

app.listen(4000,() =>{
    console.log("Server has started on port number", 4000)
})