import { Injectable } from '@angular/core';
import { Lecture } from 'src/app/models/lecture';
import { VideoService } from 'src/app/core/http/video.service'
import { Observable, of, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LectureService {

  currentLecture: Lecture;

  constructor(private videoService: VideoService) { }

  search(comp: any, searchTerm: string) {
    this.videoService.sendSearchTerm(comp, searchTerm);
  }
}
