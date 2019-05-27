import { Component } from '@angular/core';
import { PersonsComponent } from './persons/persons.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  persons: string[] = ['Jack', 'Anna', 'George'];
  onCreatedPerson(name: string) {
    this.persons.push(name);
  }
}
