import { Injectable } from '@angular/core';
import { throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VideoService {

  public data: Subject<JSON> = new Subject();

  constructor(private http: HttpClient) {}
  public sendSearchTerm(comp: any, searchTerm: string) {
    const url = `http://localhost:8080/classrooms/political_science_227/${searchTerm}` ;
    console.log(url);

    // const rawResponse = await fetch(url, {
    //     method: 'POST',
    //     headers: {
    //         'Accept': 'text/plain',
    //         'Content-Type': 'text/plain'
    //         },
    //     body: searchTerm,
    //     mode: "no-cors"
    // });
    //
    // $.get(url, function(data){
    //   console.log(data)
    // });
    const headerDict = {
      'Content-Type': 'text',
      'Accept': 'text',
      'Access-Control-Allow-Origin': 'http://localhost:8080/',
    }

    const requestOptions = {
      headers: new HttpHeaders(headerDict),
      mode: 'no-cors'
    };

    this.http.get<any>(url, {})
      .pipe(
        catchError((e) => this.handleError(e))
      ).subscribe((response)=> {
        this.data.next(response as (JSON));
        comp.updateUrl(response["url"]);
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
