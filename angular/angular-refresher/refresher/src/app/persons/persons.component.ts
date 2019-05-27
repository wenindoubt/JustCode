import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-persons',
  templateUrl: './persons.component.html',
  styleUrls: ['./persons.component.css']
})
export class PersonsComponent implements OnInit {
  @Input() personList: string[];

  constructor() { }

  ngOnInit() {
  }

}
