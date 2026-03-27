import { Routes } from '@angular/router';
import { Home } from './home/home';
import { Login } from './login/login';
import { Contact } from './contact/contact';

export const routes: Routes = [
    {
        path: "",
        component:Home
    },
    {
        path: "login",
        component:Login
    },
    {
        path: "contact",
        component:Contact
    }
];
