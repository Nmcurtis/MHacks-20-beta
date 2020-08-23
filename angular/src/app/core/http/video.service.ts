import { Injectable } from '@angular/core';
import { throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VideoService {

  public data: Subject<JSON> = new Subject();

  constructor(private http: HttpClient) { }
  public sendSearchTerm(searchTerm: string) {
    const url = `https://localhost:8800/${searchTerm}` ;
    console.log(url);
    
    this.http.get<any>(url, {})
      .pipe(
        catchError((e) => this.handleError(e))
      ).subscribe((response)=> {
        this.data.next(response as (JSON));
        console.log(response as (JSON))
      });
  }

  
  private handleError(error: HttpErrorResponse) {
    console.log('error', error);
    // return an observable with a user-facing error message
    return throwError(
      'Internal Error.');
  };

}
