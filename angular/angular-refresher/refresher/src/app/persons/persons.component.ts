import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { PersonsService } from './persons.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})
export class PersonsComponent implements OnInit, OnDestroy {
  personList: string[];
  private personListSub: Subscription;

  constructor(private personsService: PersonsService) {

  }

  ngOnInit() {
    this.personList = this.personsService.persons;
    this.personListSub = this.personsService.personsChanged.subscribe(persons => {
      this.personList = persons;
    });
  }

  onRemovePerson(personName: string) {
    this.personsService.removePerson(personName);
  }

  ngOnDestroy() {
    this.personListSub.unsubscribe();
  }

}
