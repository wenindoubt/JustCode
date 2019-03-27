import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-jwen-test',
  templateUrl: './jwen-test.component.html',
  styleUrls: ['./jwen-test.component.css']
})
export class JwenTestComponent implements OnInit {
  public name = 'Jeffrey';
  public dateOfBirth = '09-29-1991';
  public currentUrl = window.location.href;

  public isDisabled = false;

  constructor() { }

  ngOnInit() {
  }

  greetUser(name, dateOfBirth) {
    return 'Hello ' + this.name;
  }

  greetUserWithDob(name, dateOfBirth) {
    return 'Hello ' + this.name + '. You were born on ' + this.dateOfBirth;
  }

}
