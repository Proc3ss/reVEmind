reVEmind
========

EveOnline Combat Log Analyzer - v0.2a

FIXED:
 - Fixed Sqlite crash during import 
 - Updated combat regexp to include single word names and all digit names

ADDED:
 - Ive added two different build wich both do the same thing. The only difference being that one is a single executable and the other contains a bunch of files for you to look at if your into that sort of thing. Both were built at the same time and should work equally well. They are named EXE and Full_Dist.

GET STARTED:
 - Download one of the above mentioned builds.
 - Run reVEmind.exe


First Time Running: <-!!!!!THIS IS IMPORTANT
YOU MUST SELECT THE CORRECT LOG FOLDER!   
    
    File > Select Folder ( the default location is C:\Users\USER\Documents\EVE\logs\Gamelogs )
    
    Actions > Import All Files
    
    wait a while - especially if you have alot of logs, the program has never locked up on me here so if it beomes
    non-responsive.. continue to wait until it allows you to select a date(one that has been imported)
  
  After That:
  
    You will still need to import future logs, however the log folder should be saved. So all you need to do next time
    is just 'Actions > Import'
    
    **Even though the location you select is saved, if you go to 'Select Folder' again it does not default to the location you picked.. if that makes sense. Just trust me, you only have to pick the location once.


built using:
pyinstaller reVEmind\run.py --onefile --distpath=EXE --name="reVEmind" && pyinstaller reVEmind\run.py --distpath=Full_Build --name="reVEmind"

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-49779848-2', 'github.com');
  ga('send', 'pageview');

</script>
