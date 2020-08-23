import { Lecture } from './lecture';

export class Classroom {
    classCode: string;
    className: string;
    lectures: Lecture[] = [];
    
    constructor(code: string, name: string) {
        this.classCode = code;
        this.className = name;
    }
}
