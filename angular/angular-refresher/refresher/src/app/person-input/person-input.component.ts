import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-person-input',
  templateUrl: './person-input.component.html',
  styleUrls: ['./person-input.component.css']
})
export class PersonInputComponent implements OnInit {

  onCreatePerson(personName: string) {
    console.log('Created a person: ' + personName);
  }

  constructor() { }

  ngOnInit() {
  }

}
