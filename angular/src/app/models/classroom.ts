import { Lecture } from './lecture';

export class Classroom {
    classCode: string;
    className: string;
    preview: string;
    lectures: Lecture[] = [];
    
    constructor(code: string, name: string, preview: string) {
        this.classCode = code;
        this.className = name;
        this.preview = preview;
    }
}
