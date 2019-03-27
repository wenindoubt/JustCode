import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { JwenTestComponent } from './jwen-test/jwen-test.component';

@NgModule({
  declarations: [
    AppComponent,
    JwenTestComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
