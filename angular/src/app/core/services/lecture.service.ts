import { Injectable } from '@angular/core';
import { Lecture } from 'src/app/models/lecture';
import { VideoService } from 'src/app/core/http/video.service'

@Injectable({
  providedIn: 'root'
})
export class LectureService {

  currentLecture: Lecture;

  constructor(private videoService: VideoService) { }

  search(searchTerm: string) {
    this.videoService.sendSearchTerm(searchTerm);
  }
}
