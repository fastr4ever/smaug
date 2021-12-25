# Modules

import time, json, os, sys, random, urllib, webbrowser

try:
    import pystyle, requests
except:
    pystyle.System.Command('pip install pystyle requests')

# Fonctions

def Main():

    def connect():
        try:
            urllib.request.urlopen('https://github.com/fastr4ever')
            return True
        except:
            return False

    if not connect():

        pystyle.Write.Input("Une connexion internet est requise !", pystyle.Colors.red_to_white)

    def Deco():

        pystyle.Cursor.HideCursor()

        pystyle.System.Title("Smaug")

        Title = '''
                          §§§§§#                               
                           !§§§§§§§§*                          
        @  §  §§§§§§!       !§§§§§§§§§§/                       
        §§§§§§§§§§§§§§       §§§§§§§§§§§§§                     
        §§§§§§%   #§§§§      §§§§§§§§§§§§§§§                   
       §§§§§&      §§§§     §§§§§§§§§§§§§§§§§:                 
       §§§§      @§§§§!    §§§§§§§§§§§§§§§§§§§@                
      !§§:      §§§§§§   &§§§§§§§§§§§§§§§§§§§§§:               
              !§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§               
              §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§@              
             §§§§§§§§§§§§§§§%!&§§§§§§§§§§§§§§§§§§              
             §§§§§§§§§§§§§§§:    §§      §§§§§§§§              
              §§§§§§§§§§§§§§§§§&          §§§§§§§              
               §§§§§§§§§§§§§§§§§§@             §§              
                §§§#§§§§§§§§§§§§§§§             §              
                 §§*@§§§§§§§§§§§§§§/            :              
                 §§§ §§§§§§§§§§§§§§§                           
                §§$   §§§§§§§§§§§§§§§§                         
               §§       §§§§§§§§§§§§§§§§§§§§§§§&§§§            
             §§§      §§§#*%§§§§§§§§§§§§§§§§§§      §!         
             :         &      :*     :@&%              !@§§:
        '''

        pystyle.System.Size(150, 50)
        
        pystyle.Anime.Fade(pystyle.Center.Center(Title), pystyle.Colors.red_to_white, pystyle.Colorate.Vertical, enter=True)
        
    Deco()

    def Download():

        Smaug = '''
          #######                                                    
        /       ###                                                  
       /         ##                                                  
       ##        #                                                   
       ###                                                          
       ## ###      ### /### /###     /###   ##   ####      /###      
        ### ###     ##/ ###/ /##  / / ###  / ##    ###  / /  ###  /  
          ### ###    ##  ###/ ###/ /   ###/  ##     ###/ /    ###/   
            ### /##  ##   ##   ## ##    ##   ##      ## ##     ##    
              #/ /## ##   ##   ## ##    ##   ##      ## ##     ##    
               #/ ## ##   ##   ## ##    ##   ##      ## ##     ##    
                # /  ##   ##   ## ##    ##   ##      ## ##     ##    
      /##        /   ##   ##   ## ##    /#   ##      /# ##     ##    
     /  ########/    ###  ###  ### ####/ ##   ######/ ## ########    
    /     #####       ###  ###  ### ###   ##   #####   ##  ### ###   
    |                                                           ###  
     \)                                                   ####   ### 
                                                    /######  /#  
                                                       /     ###/    
        '''
        print(pystyle.Colorate.Diagonal(pystyle.Colors.red_to_white, pystyle.Center.XCenter(Smaug)))
        print()
        time.sleep(1)
        Link = pystyle.Write.Input("Lien => ", pystyle.Colors.red_to_white)
        try:
            requests.get(Link)
        except:
            print()
            pystyle.Write.Input("Lien Invalide !", pystyle.Colors.red_to_white)
            pystyle.System.Clear()
            Download()
    
        Link = f"https://maadhav-ytdl.herokuapp.com/video_info.php?url={Link}"
        
        try:
            requests.get(Link)
        except:
            print()
            pystyle.Write.Input("L'api utilisée dans ce tool à été supprimée ou est indisponible pour le moment.", pystyle.Colors.red_to_white)
            pystyle.System.Clear()
            Download()

        Text = requests.get(Link).text
        Loads = json.loads(Text)
        Link = Loads["links"][0]
        os.system('mkdir Résultat')
        urllib.request.urlretrieve(Link, "Résultat/Vidéo.mp4")
        Smauged = '''
        .M"""bgd                                                           `7MM
        ,MI    "Y                                                             MM
        `MMb.    `7Mfastrb.pMMMb.   ,6"Yb.`7MM  `7MM  .P"Ybmmm .gP"Ya    ,M""bMM
          `YMMNq.  MM    MM    MM  8)   MM  MM    MM :MI  I8  ,M'   Yb ,AP    MM
        .     `MM  MM    MM    MM   ,smaug  MM    MM  WmmmP"  8M"""""" 8MI    MM
        Mb     dM  MM    MM    MM  8M   MM  MM    MM 8M       YM.    , `Mb    MM
        P"Ybmmd" .JMML  JMML  JMML.`Moo9^Yo.`Mbod"YML.YMMMMMb  `Mbmmd'  `Wbmd"MML.
                                                    6'     dP
                                                    Ybmmmd'
        '''

        pystyle.Anime.Fade(pystyle.Center.Center(Smauged), pystyle.Colors.red_to_white, pystyle.Colorate.Vertical, enter=True)
        pystyle.System.Clear()

    Download()

Main()