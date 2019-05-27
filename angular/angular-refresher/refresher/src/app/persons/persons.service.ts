import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PersonsService {
  persons: string[] = ['Jack', 'Anna', 'George'];

  addPerson(name: string) {
    this.persons.push(name);
  }

  removePerson(name: string) {
    this.persons = this.persons.filter(person => {
      return person !== name;
    });
    console.log(this.persons);
  }

  constructor() { }
}
