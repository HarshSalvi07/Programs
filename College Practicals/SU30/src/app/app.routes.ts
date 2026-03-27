import { Routes } from '@angular/router';
import { About } from './about/about';
import { Home } from './home/home';
import { Login } from './login/login';

export const routes: Routes = [
    {
        path:"",
        component:Home
    },
    {
        path:"about",
        component:About
    },
    {
        path:"login",
        component:Login
    }
];
