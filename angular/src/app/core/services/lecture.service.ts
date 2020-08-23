import { Injectable } from '@angular/core';
import { Lecture } from 'src/app/models/lecture';

@Injectable({
  providedIn: 'root'
})
export class LectureService {

  currentLecture: Lecture;

  constructor() { }
}
