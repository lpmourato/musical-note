import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss']
})
export class SideNavComponent implements OnInit {

  @Output() onInstrumentChange: EventEmitter<string> = new EventEmitter<string>();

  INSTRUMENTS : any[] = [
    { name: 'BASS'},{ name: 'GUITAR'},
    { name: 'PIANO'},{ name: 'ALL'},
  ];

  constructor() { }

  ngOnInit() {
  }

  switchInstrument(instrument): void {
    console.log(instrument);
    // this.onInstrumentChange.emit(instrument);
  }

}
