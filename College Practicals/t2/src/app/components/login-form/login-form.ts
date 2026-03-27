import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-login-form',
  imports: [ReactiveFormsModule],
  templateUrl: './login-form.html',
  styleUrl: './login-form.css',
})
export class LoginForm {
  loginFrom = new FormGroup({
    firstName : new FormControl(""),
    lastName : new FormControl(""),
    email : new FormControl(""),
    password : new FormControl("")
  })

handleSubmit(){
  console.log(this.loginFrom.value);
  alert(`Hey ${this.loginFrom.value.firstName},Your form is submitted successfully, Details are in console`)
  this.loginFrom.reset()
}
}
