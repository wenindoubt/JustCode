import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PersonsService {
  persons: string[] = ['Jack', 'Anna', 'George'];

  addPerson(name: string) {
    this.persons.push(name);
  }

  constructor() { }
}
