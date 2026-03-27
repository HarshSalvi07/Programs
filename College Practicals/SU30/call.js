const http = require("http")
const {addNumber} = require("./add")

const app = http.createServer((req,res) =>{
    res.write("This is home page")
    res.end()
})

console.log(addNumber(12,24))

app.listen(4000,() =>{
    console.log("Server started at port number",4000)
})