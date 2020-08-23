import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import { FormsModule } from '@angular/forms'
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import { HttpClientModule } from "@angular/common/http";


import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { NavComponent } from './nav/nav.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { TestPageComponent } from './test-page/test-page.component';
import { TilePreviewComponent } from './shared/tile-preview/tile-preview.component';
import { SideMenuComponent } from './side-menu/side-menu.component';
import { ClassroomPageComponent } from './pages/classroom-page/classroom-page.component';
import { LecturePageComponent } from './pages/lecture-page/lecture-page.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    LandingPageComponent,
    TestPageComponent,
    TilePreviewComponent,
    SideMenuComponent,
    ClassroomPageComponent,
    LecturePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatGridListModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule,
    FormsModule,
    MatButtonModule,
    MatIconModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
