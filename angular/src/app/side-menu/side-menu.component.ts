import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { MatButtonModule } from '@angular/material/button'

@Component({
  selector: 'app-side-menu',
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.css']
})
export class SideMenuComponent implements OnInit {

  user: User = new User("Sean", "Kennedy", "Michigan State University", "Computer Science");
  
  constructor() { }

  ngOnInit(): void {
  }

}
