import express from "express"

const port = 4000
const app = express()

app.get("/",(req,res) =>{
    res.send("Hello World from server!")
})

app.get("/home",(req,res) =>{
    res.send("This is home page")
})

app.get("/login",(req,res) =>{
    res.send("This is login page")
})

app.get("/about",(req,res) =>{
    res.send("This is about page")
})

app.listen(port,() =>{
    console.log("Server has started at port:",port)
})