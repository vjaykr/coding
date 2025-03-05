import express from 'express';

const route = express.Router();
import { HomeController } from '../controller/HomeController.js';

route.get('/home', HomeController);

export default route;