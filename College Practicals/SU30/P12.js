const express = require("express")
const app = express();

app.use(express.json());

app.get("/",(req,res) => {
    res.send("Welcome to Express error handling")
});

app.get("/error",(req,res) =>{
    throw new Error("Something went wrong on the server")
});

app.use((err,req,res,next) => {
    console.error("Error message: ",err.message)
    res.send({
        status:false,
        message:"Internal server error"
    })
})

app.listen(3000, () =>{
    console.log("The server has started running on the port number: ",3000)
})