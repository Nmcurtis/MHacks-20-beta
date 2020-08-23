import { Injectable } from '@angular/core';
import { Classroom } from 'src/app/models/classroom';

@Injectable({
  providedIn: 'root'
})
export class ClassroomService {

  currentClassroom: Classroom;

  constructor() { }
}
