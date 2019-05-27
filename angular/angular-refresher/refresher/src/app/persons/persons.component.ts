import { Component, OnInit, Input } from '@angular/core';
import { PersonsService } from '../persons.service';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})
export class PersonsComponent implements OnInit {
  personList: string[];

  constructor(private personsService: PersonsService) {
    this.personList = personsService.persons;
  }

  ngOnInit() {
  }

}
