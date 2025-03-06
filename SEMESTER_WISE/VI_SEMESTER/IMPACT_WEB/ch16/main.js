import express from 'express';
const app = express();
const port = 3000;
import route from './routes/route.js';
//ejs setup
app.set("view engine", "ejs");

//route
app.use(route);

app.listen(port, () => {
    console.log(`Server listening on port${port}`)
});