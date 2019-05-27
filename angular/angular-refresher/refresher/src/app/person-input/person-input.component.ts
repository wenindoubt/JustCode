import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-person-input',
  templateUrl: './person-input.component.html',
  styleUrls: ['./person-input.component.css']
})
export class PersonInputComponent implements OnInit {

  @Output() createdPersonName = new EventEmitter<string>();
  enteredPersonName = '';

  onCreatePerson() {
    console.log('Created a person: ' + this.enteredPersonName);
    this.createdPersonName.emit(this.enteredPersonName);
    this.enteredPersonName = '';
  }

  constructor() { }

  ngOnInit() {
  }

}
