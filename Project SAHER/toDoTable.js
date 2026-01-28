import express from "express"
import mongoose from "mongoose"
import { Component } from "react"

const User = mongoose.Schema({
    Name :{
        type: String,
        require: true,
    } ,
    ID :{
        type: String,
        require: true,
    },
    Task : {
        type: String,
        require: true,
    },
    Date : {
        Date: String,
        require: true,
    }
})

const TODO = mongoose.model("TodoList", User)
export default TODO