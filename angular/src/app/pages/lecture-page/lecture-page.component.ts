import { Component, OnInit } from '@angular/core';
import { Lecture } from 'src/app/models/lecture';
import { LectureService } from 'src/app/core/services/lecture.service';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser'
import { FormsModule } from '@angular/forms'
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-lecture-page',
  templateUrl: './lecture-page.component.html',
  styleUrls: ['./lecture-page.component.css']
})
export class LecturePageComponent implements OnInit {

  lecture: Lecture;
  value: string;
  videoLink: SafeResourceUrl;
  timestamps: number[] = ['0'];
  baseUrl: string = "https://www.youtube.com/embed/lrk4oY7UxpQ"
  errorMessage: string = "";

  constructor(private lectureService: LectureService,
              private _sanitizer: DomSanitizer) {
    this.videoLink = this._sanitizer.bypassSecurityTrustResourceUrl(this.baseUrl);
  }

  ngOnInit(): void {
    this.lecture = this.lectureService.currentLecture;
  }

  updateUrl(url: number[]) {
    if (url.length) {
      this.status = "Matches Found!"
      this.timestamps = url;
      this.videoLink = this._sanitizer.bypassSecurityTrustResourceUrl(this.baseUrl + "?start=" + url[0]);
    } else {
      this.status = "No matches found.";
      console.log(this.status)
    }
  }

  updateVideo(url: number) {
    this.videoLink = this._sanitizer.bypassSecurityTrustResourceUrl(this.baseUrl + "?start=" + url);
  }

  onSearch() {
    this.lectureService.search(this, this.value);
  }

}
