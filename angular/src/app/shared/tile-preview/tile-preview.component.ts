import { Component, OnInit, Inject, Input } from '@angular/core';
import {MatCardModule} from '@angular/material/card';

@Component({
  selector: 'app-tile-preview',
  templateUrl: './tile-preview.component.html',
  styleUrls: ['./tile-preview.component.css']
})
export class TilePreviewComponent implements OnInit {

  @Input() title: string;
  @Input() subtitle: string;
  @Input() preview: string;

  constructor() { }

  ngOnInit(): void {
  }

}
