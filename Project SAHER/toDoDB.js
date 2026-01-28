import mongoose from "mongoose"

export const tdDB = async()=>{
    try{
        const conn = await mongoose.connect("mongodb://localhost:27017/ToDo")
        console.log("Your DB has been connected successfully")
    
    }
    catch(error){
        console.log(error.message)
    }
}