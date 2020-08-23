export class Lecture {
    date: Date;
    title: string;
    preview: string;


    constructor(date: Date, title: string, preview: string) {
        this.date = date;
        this.title = title;
        this.preview = preview;
    }
}
