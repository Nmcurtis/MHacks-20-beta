import { Component, OnInit } from '@angular/core';
import { Classroom } from 'src/app/models/classroom';
import { ClassroomService } from 'src/app/core/services/classroom.service';
import { LectureService } from 'src/app/core/services/lecture.service';
import { Router } from '@angular/router';
import { Lecture } from 'src/app/models/lecture';

@Component({
  selector: 'app-classroom-page',
  templateUrl: './classroom-page.component.html',
  styleUrls: ['./classroom-page.component.css']
})
export class ClassroomPageComponent implements OnInit {

  classroom: Classroom;

  constructor(private classroomService: ClassroomService,
    private lectureService: LectureService,
    private router: Router) { }

  ngOnInit(): void {
    this.classroom = this.classroomService.currentClassroom;
  }

  openLecture(lecture: Lecture) {
    this.lectureService.currentLecture = lecture;
    this.router.navigate(['/lecture'])
  }
}
