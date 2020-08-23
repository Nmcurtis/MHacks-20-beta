import { Classroom } from './classroom';
import { conditionallyCreateMapObjectLiteral } from '@angular/compiler/src/render3/view/util';

export class User {
    firstName: string;
    lastName: string;
    schoolName: string;
    major: string;
    classes: Classroom[];

    constructor(first: string, last: string, school: string, major: string) {
        this.firstName = first;
        this.lastName = last;
        this.schoolName = school;
        this.major = major;
    }
}
