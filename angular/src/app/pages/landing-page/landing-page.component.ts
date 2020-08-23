import { Component, OnInit, ViewChild, Output, EventEmitter } from '@angular/core';
import { MatGridListModule } from '@angular/material/grid-list';
import { User } from 'src/app/models/user'
import { Classroom } from 'src/app/models/classroom';
import { CLASSES } from 'src/app/configs/classes'
import { ClassroomPageComponent } from '../classroom-page/classroom-page.component';
import { Router } from '@angular/router';
import { ClassroomService } from 'src/app/core/services/classroom.service'
import { Lecture } from 'src/app/models/lecture';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {

  classes: Classroom[] = [];

  constructor(private router: Router,
    private classroomService: ClassroomService) { }

  ngOnInit(): void {
    for (let i=0; i < CLASSES.length; ++i) {
      this.classes.push(new Classroom(CLASSES[i]["classCode"], CLASSES[i]["className"]))
      this.classes[i].lectures.push(new Lecture(new Date(), "Lecture 1"))
    }
  }

  openClass(classroom: Classroom) {
    this.classroomService.currentClassroom = classroom;
    this.router.navigate(['/classroom'])
  }

}
