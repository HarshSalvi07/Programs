import express from "express"
import { tdDB } from "./toDoDB"

const port = 6767
const app = express()

app.use(express.json())
await tdDB()

app.get("/"),(req,res)=>{
   res.send("this is home page")
   console.log("Welcome to Router")
}

app.listen(port,(req,res)=>{
    console.log("Server has been started successfully")
})
