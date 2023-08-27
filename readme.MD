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

Terms
=====

**AOS**: Acquisition of Signal (or Satellite). AOS is the time that a satellite rises above the horizon of an observer.

**TCA**: Time of Closest Approach. This is the time when the satellite is closest to the observer and when Doppler shift is zero. This usually corresponds to the time that the satellite reaches maximum elevation above the horizon.

**LOS**: Loss of Signal (or Satellite). LOS is the time that a satellite passes below the observer’s horizon.

Credits
=======

Heavily used source code from https://github.com/Mephiro/ARTSystem/ but made it more generic.
For example: Using the json module instead of manually processing the json file as text and returning a list of aos en los tuples instead
of 2 lists, one with all aos times of a sattellite, and the other with all the los times.




.