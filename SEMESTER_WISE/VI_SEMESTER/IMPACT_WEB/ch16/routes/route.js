import express from 'express';
const route = express.Router();
import {homeController} from '../Controllers/homeController.js';

route.get('/',homeController);
route.get('/about',aboutController);

export default route;