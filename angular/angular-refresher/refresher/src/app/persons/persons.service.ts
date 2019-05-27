import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PersonsService {
  personsChanged = new Subject<string[]>();
  persons: string[] = ['Jack', 'Anna', 'George'];

  addPerson(name: string) {
    this.persons.push(name);
    this.personsChanged.next(this.persons);
  }

  removePerson(name: string) {
    this.persons = this.persons.filter(person => {
      return person !== name;
    });
    this.personsChanged.next(this.persons);
    console.log(this.persons);
  }

  constructor() { }
}
