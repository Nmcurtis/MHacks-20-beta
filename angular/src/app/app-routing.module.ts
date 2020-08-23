import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TestPageComponent } from './test-page/test-page.component'
import { LandingPageComponent } from './pages/landing-page/landing-page.component'
import { ClassroomPageComponent } from './pages/classroom-page/classroom-page.component'
import { LecturePageComponent } from './pages/lecture-page/lecture-page.component';

const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'classroom', component: ClassroomPageComponent },
  { path: 'lecture', component: LecturePageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }