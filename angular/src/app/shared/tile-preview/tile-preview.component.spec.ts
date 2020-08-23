import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TilePreviewComponent } from './tile-preview.component';

describe('TilePreviewComponent', () => {
  let component: TilePreviewComponent;
  let fixture: ComponentFixture<TilePreviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TilePreviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TilePreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
