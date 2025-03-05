import express from 'express';


const app = express();
const port = 4000;
import route from "./routes/route.js";

app.set("view engine", "ejs");


//routes
app.use(route);
app.listen(port, () => {
    console.log(`Server is running at
        http://localhost:${port}`);
    });