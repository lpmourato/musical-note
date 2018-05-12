import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.scss']
})
export class SideNavComponent implements OnInit {

  @Output() onInstrumentChange: EventEmitter<string> = new EventEmitter<string>();

  INSTRUMENTS : any[] = [
    { name: 'Bass', selected: true, img: '../assets/img/button_bass.png' },
    { name: 'Guitar', selected: false, img: '../assets/img/button_guitar.png' },
    { name: 'Piano', selected: false, img: '../assets/img/button_piano.png' },
    { name: 'All', selected: false, img: '../assets/img/button_all.png'  },
  ];

  constructor(private router: Router) { }

  ngOnInit() {
  }

  switchInstrument(instrument): void {
    console.log(instrument);
  }

  isSelected(instrument): boolean {
    return this.INSTRUMENTS.some(inst => inst.name === instrument && inst.selected);
  }

  changeRoute(value): void {
    this.router.navigate([`dashboard/${value}`]);
  }

}
