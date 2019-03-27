import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { JwenTestComponent } from './jwen-test.component';

describe('JwenTestComponent', () => {
  let component: JwenTestComponent;
  let fixture: ComponentFixture<JwenTestComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ JwenTestComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(JwenTestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
