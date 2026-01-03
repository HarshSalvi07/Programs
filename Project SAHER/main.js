import express from 'express'
const port = 6767
const app = express();
let Books = [];
let nextID = 1;
app.use(express.json())

app.get("/",(req,res)=>{
    return res.send("This is sent via GET request")
})

app.post("/addBooks",(req,res)=>{
    const {title,author} = req.body;

    if (!title || !author){
    return res.json({error:"The title and author are mandatory fields"})
    }

    const newBook = {
        id: nextID++,
        title,
        author,
        available:true
    };

    Books.push(newBook);
    console.log("New book ",newBook.title," has been added successfully")
 
    return res.json(newBook)

})

app.listen(port,(req,res)=>{
    console.log("The server is running")
})