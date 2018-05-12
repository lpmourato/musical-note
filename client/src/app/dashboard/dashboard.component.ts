import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { ActivatedRoute, ParamMap, Router, NavigationEnd, ActivationEnd } from '@angular/router';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, OnChanges {

  instrument = 'guitar';

  mode = 'EASY';
  isEasyMode = true;
  isAutoPlay = false;

  KEYS: any[] = [
    { name: 'C', style: 'key-button'}, { name: 'D', style: 'key-button'},{ name: 'E', style: 'key-button'},
    { name: 'F', style: 'key-button'},{ name: 'G', style: 'key-button'},{ name: 'A', style: 'key-button'},
    { name: 'B', style: 'key-button'},
  ];

  SHARP_KEYS: any[] = [
    { name: 'C#', style: 'key-button'}, { name: 'D#', style: 'key-button'},{ name: 'F#', style: 'key-button'},
    { name: 'G#', style: 'key-button'},{ name: 'A#', style: 'key-button'},
  ];

  CONTROLS: any[] = [
    { name: 'EASY'},{ name: 'HARD'},{ name: 'AUTO PLAY'}, { name: 'STOP'}
  ];

  constructor(private router: Router,
              private activeRoute: ActivatedRoute) { }

  ngOnInit() {
    this.activeRoute.url.subscribe(value => {
      this.instrument = value[1].path;
      console.log('AQUI ', this.instrument);
    });
  }

  ngOnChanges() {
    
  }

  match(keyName): void {
    console.log(keyName);
  }

  switchMode(event): void {
    this.isEasyMode = event.value === 'EASY';
  }

  autoPlay(): void {
    this.isAutoPlay = !this.isAutoPlay;
    console.log('auto play');
  }

  play(): void {
    console.log('auto play');
  }

  stop(): void {
    this.isAutoPlay = false;
    console.log('stop');
  }

  changeInstrument(event): void {
    console.log(event);
  }
}
