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
  public successClass = 'text-success';
  public hasError = true;
  public isSpecial = true;
  public greetingMessage = ''; // initialize
  public usernameInput = '';
  public someOtherInput = '';
  public toggleSentence = true;
  public displayName = true;
  public selectColor = 'green';
  public purpleColor = '#8A2BE2';
  public blueColor = 'blue';
  public greenColor = 'green';
  public colors = ['red', 'green', 'blue', 'yellow'];

  public warningMessage = {
    color: 'red',
    fontStyle: 'bold'
  };

  public messageClasses = {
    'text-success': !this.hasError,
    'text-danger': this.hasError,
    'text-special': this.isSpecial
  };
  public multipleStyles = {
    color: 'blue',
    fontStyle: 'italic'
  };


  constructor() { }

  ngOnInit() {
  }

  greetUser(name, dateOfBirth) {
    return 'Hello ' + this.name;
  }

  greetUserWithDob(name, dateOfBirth) {
    return 'Hello ' + this.name + '. You were born on ' + this.dateOfBirth;
  }

  myClick(event) {
    this.greetingMessage = 'You just clicked me! The event type is ' + event.type;
    console.log(event);
  }

  submitText(value) {
    console.log(value);
  }

}
