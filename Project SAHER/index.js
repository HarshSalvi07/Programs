import express from "express"
import { tdDB } from "./toDoDB.js"


const port = 6969
const app = express()

app.use(express.json())
await tdDB()

app.get("/",(req,res)=>{
    console.log("Welcome to Router")
    res.send("this is home page")
})

app.post("/addTask",(req,res)=>{
    res.send("Your tasks are as follows:")
    let userTask = 
})

app.listen(port,()=>{
    console.log("Server has been started successfully")
})