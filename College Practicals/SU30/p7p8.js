import express from "express"

const port = 4000
const app = express()
const logger = (req,res, next) =>{
    console.log(`${req.method}${req.url}`)
    next()
}
app.use(express.json())
app.use(logger)

app.get("/", (req,res) =>{
    res.send("Hello world from Express server with middleware")
})

app.listen(port, () =>{
    console.log('Express server started at port number ${port}')
})