NOAA Sattellite passes and GUI
==============================

Idea
----

Build a gui which shows NOAA sattellite passes.
It shows with colored buttons if a satellite is visible (and thus audible).
By clicking that button, it will tune a connected radio to the downlink frequency.

Connnect radio's:
* RTLSDR USB dongle
* SDRPlay radio

How:
* Will get information from n2yo.com by means of REST API
* Display that passes.
* Process the time intervals.

https://www.n2yo.com/login/


* See https://www.n2yo.com/api/ for the available API's 
* For a good usage description: https://john-smith-889.github.io/blog/space%20industry/satellites-tracking.html