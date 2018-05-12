import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; 

import { NgModule } from '@angular/core';

import { MatButtonModule, MatButtonToggleModule, MatIconModule, MatSelectModule, MatOptionModule,
   MatSidenavModule, MatCard, MatCardModule, MatOption, MatChipsModule } from '@angular/material';
import { AppComponent } from './app.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard/bass', pathMatch: 'full' },
  { path: 'dashboard/:instrument', component: DashboardComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    SideNavComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    MatButtonModule,
    MatIconModule,
    MatSidenavModule,
    MatButtonToggleModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatSelectModule,
    MatOptionModule,
    MatChipsModule, 
    RouterModule.forRoot(
      routes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
