import mongoose from "mongoose";

export const connectDb = async () => {
  try {
    const conn = await mongoose.connect("mongodb://localhost:27017/Router");
    if (conn.connection) {
      console.log("Database has been successfully created");
    }
  } catch (error) {
    console.log(error.message);
  }
};
