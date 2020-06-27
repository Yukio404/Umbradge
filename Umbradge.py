import os, sys, random
import subprocess
from tools import *

class colors:
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    WHITE = '\033[37m'
    RANDOM = random.choice([BLUE, GREEN, WHITE])


logo1 = colors.RANDOM + '''
     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777
'''

logo2 = colors.RANDOM + '''
                            ,.--------._
                           /            ''.
                         ,'                \     |"\                /\          /\
                /"|     /                   \    |__"              ( \\        // )
               "_"|    /           z#####z   \  //                  \ \\      // /
                 \\  #####        ##------".  \//                    \_\\||||//_/
                  \\/-----\     /          ".  \                      \/ _  _ \
                   \|      \   |   ,,--..       \                    \/|(O)(O)|
                   | ,.--._ \  (  | ##   \)      \                  \/ |      |
                   |(  ##  )/   \ `-....-//       |///////////////_\/  \      /
                     '--'."      \                \              //     |____|
                  /'    /         ) --.            \            ||     /      \
               ,..|     \.________/    `-..         \   \       \|     \ 0  0 /
            _,##/ |   ,/   /   \           \         \   \       U    / \_//_/
          :###.-  |  ,/   /     \        /' ""\      .\        (     /
         /####|   |   (.___________,---',/    |       |\=._____|  |_/
        /#####|   |     \__|__|__|__|_,/             |####\    |  ||
       /######\   \      \__________/                /#####|   \  ||
      /|#######`. `\                                /#######\   | ||
     /++\#########\  \                      _,'    _/#########\ | ||
    /++++|#########|  \      .---..       ,/      ,'##########.\|_||
   //++++|#########\.  \.              ,-/      ,'########,+++++\\_\\
  /++++++|##########\.   '._        _,/       ,'######,''++++++++\
 |+++++++|###########|       -----."        _'#######' +++++++++++\
|+++++++|############\.     \\     //      /#######/++++ S@yaN +++\
     ________________________\\___//______________________________________
'''

#marche pas
logo3 = colors.RANDOM + '''
                          ,_   ,-"-._
                    .___   \\'-._\  \`~,_
                    _'. `~-,\ ~-.|     \\',
                  .'   \    |    \  '  /  \\
                 / ~-.  |   '    | .' ;  ; \\
                 |.--    \ . '   /    |  . |\\
                 / ., `\ |     `___  /  .  ||
                 |/  \  \/\__.-'   `\;    / /
                      \ /      .--.  |   / /
                       /,     /    \ / .' /
                      / \\\   /."".  |;  '(__,
                    ,_|/_\ ._/___.\_|'   .-.;_,
                   "==;_o_\ /_o__,==" \ / )) .'__,
                  ,="/    |      "=,   ; _/   _.'
                  %/\__..)_,)`-.__     /\%\%\.`.__,
                .%/%/` .-._ _..-. `      `"%\%.--'
                   ;   `;-.:..-'/|          |./
               _.--|     ).___.-||          ;  `'--._
             .'    |  o /|     / ;          /        `,
            /      |   ( `----' /          /           \\
           /       |    '------'         /`             \\
          /         \  (     ,        .'`                \\
         /           '._`---'     _.-'                    ;
        /      /     `._`""""""""`                         ;
       /     .'      ,__/`~|~`\                            |
      /    ooooo,    \  \ '`)- |            ,              |
    .'   d888888888ooo\ /'-'\ /o8888888o,    \             |
  .'    888888888888888'._|_.'888888888888b   \            |
.'      888888888888888888888888888888888888, |            ;
         Y88888888888888888888888888888888888b;            /
'''
#marche pas
logo4 = colors.RANDOM + '''
                       ---
                    -        --
                --( /     \ )XXXXXXXXXXXXX
            --XXX(   O   O  )XXXXXXXXXXXXXXX-
           /XXX(       U     )        XXXXXXX\
         /XXXXX(              )--   XXXXXXXXXXX\
        /XXXXX/ (      O     )   XXXXXX   \XXXXX\\
        XXXXX/   /            XXXXXX   \   \XXXXX----
        XXXXXX  /          XXXXXX         \  ----  -
---     XXX  /          XXXXXX      \           ---
  --  --  /      /\  XXXXXX            /     ---=
    -        /    XXXXXX              '--- XXXXXX
      --\/XXX\ XXXXXX                      /XXXXX
        \XXXXXXXXX                        /XXXXX/
         \XXXXXX                         /XXXXX/
           \XXXXX--  /                -- XXXX/
            --XXXXXXX---------------  XXXXX--
               \XXXXXXXXXXXXXXXXXXXXXXXX-
                 --XXXXXXXXXXXXXXXXXX-
'''

logo5 = colors.RANDOM + '''
                        .-.
                _.--"""".o/         .-.-._
             __'   ."""; {        _J ,__  `.
            ; o\.-.`._.'J;       ; /  `- /  ;
            `--i`". `" .';       `._ __.'   |
                \  `"""   \         `;      :
                 `."-.     ;     ____/     /
                   `-.`     `-.-'    `"-..'
     ___              `;__.-'"           `.
  .-{_  `--._         /.-"                 `-.
 /    ""T    ""---...'  _.-""   """-.         `.
;       /                 __.-"".    `.         `,             _..
 \     /            __.-""       '.    \          `.,__      .'L' }
  `---"`-.__    __."    .-.       j     `.         :   `.  .' ,' /
            """"       /   \     :        `.       |     F' \   ;
                      ;     `-._,L_,-""-.   `-,    ;     `   ; /
                       `.       7        `-._  `.__/_        \/
                         \     _;            \  _.'  `-.     /
                          `---" `.___,,      ;""        \  .'
                                    _/       ;           `"
                                 .-"     _,-'
                                {       "";
                                 ;-.____.'`.
                                  `.  \ '.  :
                                    \  : : /
                                     `':/ `
'''

#marche pas
logo6 = colors.RANDOM + '''
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \\
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /
                 "-.t-._:'
'''

#marche pas
logo7 = colors.RANDOM + '''
                                 ._
                              ,-'_ `-.
                              ::".^-. `.
                              ||<    >. \
                              |: _, _| \ \
                              : .'| '|  ;\`.
                              _\ .`  '  | \ \
                            .' `\ *-'   ;  . \
                           '\ `. `.    /\   . \
                         _/  `. \  \  :  `.  `.;
                       _/ \  \ `-._  /|  `  ._/
                      / `. `. `.   /  :    ) \
                      `;._.  \  _.'/   \ .' .';
                      /     .'`._.* /    .-' (
                    .'`._  /    ; .' .-'     ;
                    ; `._.:     |(    ._   _.'|
                    `._   ;     ; `.-'        |
                     |   / .-'./ .'  \ .     /:
                     |  +.'  \ `-.   .\ *--*' ;\
                     ;.' `. \ `.    /` `.    /  .
                    /.L-'\_: L__..-*     \   ".  \
                   :/ / .' `' ;   `-.     `.   \  .
                   / /_/     /              \   ;  \
              |  _/ /       /          \     `./    .
            `   .  ;       /    .'      `-.   ;      \
           --  /  /  --   ,    /           `"' \      .
          .   .  '       /   .'                 `.     \
             /  /    `  /   /                  |  `-.   .
        --  .  '   \   /                         `.  `-._\
       .   /  /       : `*.                    :   `.    `-.
          .  '    `   |    \                    \    `-._   `-._
     --  /  /   \     :     ;                    \              |
   .    .  '           ;                          `.  \      :  ;
       /  /   `       : \    \                      `. `._  /  /
  --  .  '  \         |  `.   `.                      `-. `'  /\
     /  .             ;         `-.              \       `-..'  ;
 `  .  '   `          |__                     |   `.         `-._.
_  :  /  \              ;`-.                  :     `-.           ;
    `"  `               |   `.                 \       `*-.__.-*"' \\
' /  . \                ;_.  :`-._              `._                /
                       /   `  . ; `"*-._                       _.-`
                     .'"'    _;  `-.__                     _.-`
                     `-.__.-"         `""---...___...--**"' |
                                                  `.____..--'
'''

#marche pas
logo8 = colors.RANDOM + '''
                     ______
                   <((((((\\\\
                   /      . }\\
                   ;--..--._|}
(\                 '--/\--'  )
 \\\                | '-'  :'|
  \\\               . -==- .-|
   \\\               \.__.'   \--._
   [\\\          __.--|       //  _/'--.
   \ \\\       .'-._ ('-----'/ __/      \\
    \ \\\     /   __>|      | '--.       |
     \ \\\   |   \   |     /    /       /
      \ '\ /     \  |     |  _/       /
       \  \       \ |     | /        /
        \  \      \        /
'''

logo9 = colors.RANDOM + """
                               ...,,,,,...
                           ,%%%%%%%%%%%%%%%Ss,
                          %%%%%%%%%%%%,,,%%%%SSs,.
                      .,;;;;;;,%%%%%%,%%%%%,%%SSs%%
                  ..;;;;;;;;;;;;;;,%%%%,,,,%%%SSS%'
                 .;;;;;;;;;;;;;;;;;;%%,a@;;;%%%SS'
               .,;;;;;;;;;;;;;;;;;;;%,a@;;  `%%SSS,.
             ,;;;;;;;;;;;;;;;;;;;;;'%,@@;;,,,%%%SSSSSSSS'''.
            ;;;;;;;;;;;;;;;;;;;;;;;,%%@@@aaaa%%%SSSSSSS,   ;
          ,;;;;;;;;;;;;;;;;;;;;;;;;;,%%@@@@@%%%SSSSSSSSSs,,'
         ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%%%%%%%SSSSSSSSSSSS'
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%%%%%%%SSSSSSSSSSS'
       ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'%%%%%%%%SSSSSSSS'
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,%%%%%%'
      ;;;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;,%%%%%
      ;;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,%;%;%.
      `;;,;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;,sSSSSSSs%,
        `,;;;;,;;;;;;;;;;;;;;;;;;;,;;;;'sSSSSSSSSSSS.
          ;;;,;;;;;;;;;;;;;,;;;;;,;;;;'SSSSSSSSSSSSSSs
           `;';;;;;;;;;;;;;,;;;;,;;;'sSSSSSSSSSSSSSsSSs.
              `;;;;;;;;;;;,;;;;'%%%%;SSSSSSSSSSSSSSSSsSs
             .,%%;;;;;;;;'%%%%%%%%%;sSSSSSSSSSSsSSSSSSsS
          .,%%%%%`;;;'%%%%%%%%%%%%%;SSSSSSSSSSSSSsSSSSs'
       .,%%%%%%%%%'%%%%%%%%%%%%%%%;sSSSSSSSSSSSSSSsSSS'
   .,%%%%%%%%%%%%%%%%%%%%%%%%%%%%;sSSSSSSSSSSSSSSSsS'
 ,%%%%%%%%%%%%%%%%%%%%;%%%%%%%%%%;SSSSSSSSSSSSSSSs'
%%%%%%%%%%%%%;%%%%%%%;%%%%%%%%%%;sSSSSSSSSSSSSSS'
%%%%%%%%%%%%%%%;%%%%;%%%%%%%%%%%;SSSSSSSSSSSS'%%
%%%%%%%%%%%%%%%%%;%;%%%%%%%%%%%;sSSSSSSSS'%%%%%%%
%%%%%%%%%%%%%%%%%%;%%%%%%%%%%%;sSSSS'ssssSSSS%%%%%
%%%%%%%%%%%%%%%%%%;%%%%%%%%%%%'      `SSSSSSSSS%%%%
%%%%%%%%%%%%%%%%%;%%%%%%%%%%%'         `SSsSSSSSS%%%
%%%%%%%%%%%%%%%%% %%%%%%%%%%'            S'`SSsSSSSSSs.
%%%%%%%%%%%%%%%%' '%%%%%%%%'                 S'`SSssssSS.
%%%%%%%%%%%%;sSSs   `SSSSSSs.                    `SSSS%SS
%%%%%%%%%;sSSSSSS    `SSSSSSS
"""

#marche pas
logo10 = colors.RANDOM + """
                   ___
	       .-'`   `'-.
	   _,.'.===   ===.'.,_
	  / /  .___. .___.  \ \\
	 / /   ( o ) ( o )   \ \                                            _
	: /|    '-'___'-'    |\ ;                                          (_)
	| |`\_,.-'`   `"-.,_/'| |                                          /|
	| |  \             /  | |                                         /\;
	| |   \           /   | | _                              ___     /\/
	| |    \   __    /\   | |' `\-.-.-.-.-.-.-.-.-.-.-.-.-./`   `"-,/\/
	| |     \ (__)  /\ `-'| |    `\ \ \ \ \ \ \ \ \ \ \ \ \`\       \/
	| |      \-...-/  `-,_| |      \`\ \ \ \ \ \ \ \ \ \ \ \ \       \\
	| |       '---'    /  | |       | | | | | | | | | | | | | |       |
	| |               |   | |       | | | | | | | | | | | | | |       |
	\_/               |   \_/       | | | | | | | | | | | | | | .--.  ;
	                  |       .--.  | | | | | | | | | | | | | | |  | /
	                   \      |  | / / / / / / / / / / / / / /  |  |/
	                   |`-.___|  |/-'-'-'-'-'-'-'-'-'-'-'-'-'`--|  |
	            ,.-----'~~;   |  |                  (_(_(______)|  |
	           (_(_(_______)  |  |                        ,-----`~~~\\
	                    ,-----`~~~\                      (_(_(_______)
	                   (_(_(_______)
"""

logo11 = colors.RANDOM + '''
                       _..gggggppppp.._
                  _.gd$$$$$$$$$$$$$$$$$$bp._
               .g$$$$$$P^^""j$$b""""^^T$$$$$$p.
            .g$$$P^T$$b    d$P T;       ""^^T$$$p.
          .d$$P^"  :$; `  :$;                "^T$$b.
        .d$$P'      T$b.   T$b                  `T$$b.
       d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b
      d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b
     d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b
    d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P            T$$b
   d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b
  :$$$      .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.g.     $$$;
  $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$
 :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$;
 $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$
:$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
:$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
$$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
$$$;      $$$$$$$$$$$$$$$                        Tb    _  :$$$
:$$$     d$$$$$$$$$$$$$$$.                        $b.__Tb $$$;
:$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
 $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$
 :$$$       T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$;
  $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$
  :$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;     $$$;
   T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P
    T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P
     T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P
      T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P
       T$$b.      '       $$$$$$$$$$$$$$$$$$$$$$$$$$$$P
        `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'
          `T$$$$p..__..g$$$$$$$$$$$$$$$$$$$$$$$$$$P'
            "^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^"
               "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"
                   """^^^T$$$$$$$$$$P^^^"""
'''

logo12 = colors.RANDOM + '''
                            __          .gp.__/
                       .ssSSSSSs.__    d$P^^^"
                    .sSSSSSSS$$$$$$$p.dP
                  .SSSSSS$$$$$SSSSSSSS$bs+._
                .SSSS$$$$$SSSSS$$$$$$$SS$$$$b__                       /"-.
                SSS$$$SSSSS$$$$$$$$SSSS$$$SSSS$b                   _/"-. /
               :S$$$SSSSS$$$$$$$SSSSS$$$SSSS$$SSb                 //   /"-.
               $$SSSSS$$$$$$SSSSS$$$$$$S$$$$S$$$Sb.               ;   /   /
               SSSSS$$$$$SSSSS$$$$$$$SS'P   SS$$S`^b._.'         /:  :   /
               :S$$$$$SSSSS$$$$$$$SSSP      :$SS$b              / ;  +-./
                $$$$SSSS$$$$$$$SSSSSP        S$SS$;            / /  / / ;
               d$$SSS$$$$$SSSSSSSSS' ,=._    :S':S$           / /  / / /
              :$SSS$$$$SSSSSSSSS^"  '  _ ";  ;   S$          / /  / / /
              SSS$$$SSSP.-TSS^"     .="$;   /    S;         / /  / / /
             :SS$$$SSS$$ (;            "    \    P         / /  / : :
             :S$$$SS$$$$b :                  \ .'         / /  /  :  \
              T$$SS$$$$$j`-,    .          ,  \         /"-(  /   ;_-.\
               `TSS$$$$P   ;    `.         `.-'        /  /\\\/   .'/_ ;;
                 TS$$$P    :             _.-;         /  /\\\(   / /-" ;;
                  SSS'      \           :-t"         : .-\\\/ "-/":   //
                .SS$$        `.          `-;         )Y   y   /  ;  J/
               :S$$$;          "-.        (          '"; j_.-/-./.-" \_
               $S$SS              "j.     :            :/  ':    `-..' \
              d$$SS;     :        /  "-._.'             `.  ;       `-./;
            _S$$$SP       \      :                        \: :"-.      \;
          ,$$$SSSj       , `.    ;                         : ;   "-,   /
          S$$SS'"^-...___       : "-.                      ;/      ;  t
      __.-`SS'---. `T$$$$$$q._       "-.                  / `.    /   ;
  .-""__ `.'      `. `T$$$$$$$$b.       `.               :    "--"   /
 /.-""  \/          `. T$$$$$$$$$$p.     .`._            /"-.  _   .'
::      /             \ T$$$$$SS$$$$$b._  `.T$p.        /    "" ;-'
;;     :               \ T$$$S$$$$$$$$$$$p._L$$$$p.    /       ,
;;     ;                \ $$$$$$$$$$$$$$$$$$$SS$$$$$. /
::     ;                 ;:$$$$$$$$$$$$$$SSSSSSSSS$$$y        '
 ;;    :                  "^$$$$$$$$$$$$$$$$$SSSS$$$P        /
 ;;     b.                   "^$$$$$$$$$$$$$$$$$S$$'        /
 ::     :$$p.  -._              "^$$$$$$$$$$$$$$$'         /
  ;;     $$$$$p.                   "^$$$$$$$$$$P          /
  ::     :$$$$$$p.                    "^$$$$$$P          ,
   ;;     T$$$$$$$$p.                    "^$$P
   ::      T$$$$$$$P "-.                    "           '
   s;;      $$$$$$P   d$$p._                     /     /
  S$$:      $$$$$t   d$$$$$$$p._          "-.  .'     /
  SS$;;     :P^"\ \.d$$$$$$$$$$$$p._         ""      /
   TS::      \   d$$$$$$$$$$$$$$$$$$$p._            /
    SS.\     .jq$$$$$$$$$$$$$$$$$$^^^^^""-._      .';
   $$$$.tsssj' `T$$$$$$$^^^^^"""            "-._.'  ;
   $$$SSS         \                 /            \ :
   '^SSS_          \               :          :    :
     $$$SS.         \              ;          :    ;
     '$$$SS          \            :           ;   :
       "^S$.          \           ;          :    :
         S$$b.         \                     ;    ;
         S$$$$          ;                   :    :
         'TSS$$$s.      :                   ;    ;
             TS$$Ss_    ;                   ;   :
              `SSS$$$p./                   :    ;
                  TS$$'            ;       ;    :
                   "S              :       ;     ;
                   /                ;      :     :
                  /                 :            :
                 /"-.                          .' ;
                /    ""--..__          __..--""   :
                             """"""""""
'''

#marche pas
logo13 = colors.RANDOM + '''
             ________________________________________________
            /                                                \\
           |    _________________________________________     |
           |   |                                         |    |
           |   | root ~$                                 |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
'''

logo14 = colors.RANDOM + '''
      .____.
   xuu$``$$$uuu.
 . $``$  $$$`$$$
dP*$  $  $$$ $$$
?k $  $  $$$ $$$
 $ $  $  $$$ $$$
 ":$  $  $$$ $$$
  N$  $  $$$ $$$
  $$  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $$#$  $$$ $$$
   $$'$  $$$ $$$
   $$`R  $$$ $$$
   $$$&  $$$ $$$
   $#*$  $$$ $$$
   $  $  $$$ @$$
   $  $  $$$ $$$
   $  $  $$$ $$$
   $  $  $B$ $$&.
   $  $  $D$ $$$$$muL.
   $  $  $Q$ $$$$$  `"**mu..
   $  $  $R$ $$$$$    k  `$$*t
   $  @  $$$ $$$$$    k   $$!4
   $ x$uu@B8u$NB@$uuuu6...$$X?
   $ $(`RF`$`````R$ $$5`"""#"R
   $ $" M$ $     $$ $$$      ?
   $ $  ?$ $     T$ $$$      $
   $ $F H$ $     M$ $$K      $  ..
   $ $L $$ $     $$ $$R.     "d$$$$Ns.
   $ $~ $$ $     N$ $$X      ."    "%2h
   $ 4k f  $     *$ $$&      R       "iN
   $ $$ %uz!     tuuR$$:     Buu      ?`:
   $ $F          $??$8B      | '*Ned*$~L$
   $ $k          $'@$$$      |$.suu+!' !$
   $ ?N          $'$$@$      $*`      d:"
   $ dL..........M.$&$$      5       d"P
 ..$.^"*I$RR*$C""??77*?      "nu...n*L*
'$C"R   ``""!$*@#""` .uor    bu8BUU+!`
'*@m@.       *d"     *$Rouxxd"```$
     R*@mu.           "#$R *$    !
     *%x. "*L               $     %.
        "N  `%.      ...u.d!` ..ue$$$o..
         @    ".    $*"""" .u$$$$$$$$$$$$beu...
        8  .mL %  :R`     x$$$$$$$$$$$$$$$$$$$$$$$$$$WmeemeeWc
       |$e!" "s:k 4      d$N"`"#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
       $$      "N @      $?$    F$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
       $@       ^%Uu..   R#8buu$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                  ```""*u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                         #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                          "5$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                            `*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                              ^#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>
                                 "*$$$$$$$$$$$$$$$$$$$$$$$$$$>
                                   `"*$$$$$$$$$$$$$$$$$$$$$$$>
                                       ^!$$$$$$$$$$$$$$$$$$$$>
                                           `"#+$$$$$$$$$$$$$$>
                                                 ""**$$$$$$$$>
                                                        ```""
'''

logo15 = colors.RANDOM + '''
  _____________________________________                        ________
 /     ________________________________| KLINGON COMBAT BLADE |________)
|     |
|     |                               /\
|     |                              / |\\
|     |                             / /\ \\
|     |                            / /  \ \\
|     |                           / /    \ \\
|     |                          /_/      \_\\
|     |                          \    '`    /
|     |                           )   ||   (
|_____|___________________________|_  ||   |
|     | TEMPERED DYRILLIUM BLADE  |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |                           |   ||   |
|     |               /           |   ||   |           \\
|     |              /(           |   ||   |           )\\
|     |              |`\_         |   ||   |         _/'|
|     |              |`. `-._     |   ||   |     _,-' ,'|
|     |              (   ` . `-._ |  _--_  | _,-' , '   )
|     |               `|._   ` . `-./.__.\.-' , '   _,-'
|_____|________________|  `-._   ` | /  \ | '   _,-'
|     | RETRACTABLE BLADES    `-._/ |_()_| \_,-'
|     |                    ___.-'   ______   `-,
|     |                   '-----.  |______|   /
|     |                          \  ______   /
|_____|__________________________|__\>__  |>
|     | MACE HEAD                <|   <   >|
|     |                            `.____.'
|     |                              V   V
|     |
|     |_____________________________________________________   ________
 \__________________________________________________________| |________)
'''
os.system('cls')

random = random.choice([logo1,
                        logo2,
                        logo3,
                        logo4,
                        logo5,
                        logo6,
                        logo7,
                        logo8,
                        logo9,
                        logo10,
                        logo11,
                        logo12,
                        logo13,
                        logo14,
                        logo15])
print(random)

Loop = 1
while True:
    prompt = colors.WHITE + 'Umbradge: ~ $ '
    tools = colors.RED + '''
    {1}-- Social Engineering
    {2}-- ShellCode
    {3}-- Sniffing & Spoofing
    {4}-- Buffer Overflow
    {5}-- Web Hacking
    {6}-- Post Exploitation
    {7}-- BruteForce
    {8}-- Osint
    {9}-- Wireless Attacks
    {10}-- Anonymize
    {0}-- Install & Update
    {99}-- Exit
    '''
    print(tools)

    choice = int(input(prompt))
    while 1:
        if choice == 1:
            os.system('cls')
            logo = colors.RANDOM + '''
              _____            _       _ ______             _                      _
             / ____|          (_)     | |  ____|           (_)                    (_)
            | (___   ___   ___ _  __ _| | |__   _ __   __ _ _ _ __   ___  ___ _ __ _ _ __   __ _
             \___ \ / _ \ / __| |/ _` | |  __| | '_ \ / _` | | '_ \ / _ \/ _ \ '__| | '_ \ / _` |
             ____) | (_) | (__| | (_| | | |____| | | | (_| | | | | |  __/  __/ |  | | | | | (_| |
            |_____/ \___/ \___|_|\__,_|_|______|_| |_|\__, |_|_| |_|\___|\___|_|  |_|_| |_|\__, |
                                                       __/ |                                __/ |
                                                      |___/                                |___/
            '''
            print(logo)
            tools = colors.RED + '''
            {1}-- Phishing
            {2}-- Spear-phishing
            {3}-- Profil Generator
            '''
            print(tools)
            choice = int(input(prompt))

            if choice == 1:
                logo = colors.RANDOM + '''
                 _____  _     _     _     _
                |  __ \| |   (_)   | |   (_)
                | |__) | |__  _ ___| |__  _ _ __   __ _
                |  ___/| '_ \| / __| '_ \| | '_ \ / _` |
                | |    | | | | \__ \ | | | | | | | (_| |
                |_|    |_| |_|_|___/_| |_|_|_| |_|\__, |
                                                   __/ |
                                                  |___/
                '''

        elif choice == 2:
          os.system('cls')
          logo = colors.RANDOM + '''
             _____ _          _ _  _____          _
            / ____| |        | | |/ ____|        | |
           | (___ | |__   ___| | | |     ___   __| | ___
            \___ \| '_ \ / _ \ | | |    / _ \ / _` |/ _ \\
            ____) | | | |  __/ | | |___| (_) | (_| |  __/
           |_____/|_| |_|\___|_|_|\_____\___/ \__,_|\___|
          '''

          print(logo)
          tools = colors.RED + '''
          {1}-- Local
          {2}-- Distant
          '''
          print(tools)
          choice = int(input(prompt))

        elif choice == 3:
          os.system('cls')
          logo = colors.RANDOM + '''
             _____       _  __  __ _                         _____                    __ _
            / ____|     (_)/ _|/ _(_)               ___     / ____|                  / _(_)
           | (___  _ __  _| |_| |_ _ _ __   __ _   ( _ )   | (___  _ __   ___   ___ | |_ _ _ __   __ _
            \___ \| '_ \| |  _|  _| | '_ \ / _` |  / _ \/\  \___ \| '_ \ / _ \ / _ \|  _| | '_ \ / _` |
            ____) | | | | | | | | | | | | | (_| | | (_>  <  ____) | |_) | (_) | (_) | | | | | | | (_| |
           |_____/|_| |_|_|_| |_| |_|_| |_|\__, |  \___/\/ |_____/| .__/ \___/ \___/|_| |_|_| |_|\__, |
                                            __/ |                 | |                             __/ |
                                           |___/                  |_|                            |___/
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- Sniffing
          {2}-- Spoofing
          '''
          print(tools)
          choice = int(input(prompt))

          if choice == 1:
            os.system('cls')
            logo = colors.RANDOM + '''
               _____       _  __  __ _
              / ____|     (_)/ _|/ _(_)
             | (___  _ __  _| |_| |_ _ _ __   __ _
              \___ \| '_ \| |  _|  _| | '_ \ / _` |
              ____) | | | | | | | | | | | | | (_| |
             |_____/|_| |_|_|_| |_| |_|_| |_|\__, |
                                              __/ |
                                             |___/
            '''
            print(logo)
            tools = colors.RED + '''
            {1}-- Email Traffic
            {2}-- FTP Passwords
            {3}-- Web Traffics
            {4}-- Telnet Passwords
            {5}-- Router Configuration
            {6}-- DNS Traffic
            {7}-- TCP/IP Sniffing
            '''

            print(tools)
            choice = int(input(prompt))

          if choice == 2:
            os.system('cls')
            logo = colors.RANDOM + '''
               _____                    __ _
              / ____|                  / _(_)
             | (___  _ __   ___   ___ | |_ _ _ __   __ _
              \___ \| '_ \ / _ \ / _ \|  _| | '_ \ / _` |
              ____) | |_) | (_) | (_) | | | | | | | (_| |
             |_____/| .__/ \___/ \___/|_| |_|_| |_|\__, |
                    | |                             __/ |
                    |_|                            |___/
            '''
            print(logo)
            tools = colors.RED + '''
            {1}-- MAC Flooding
            {2}-- DHCP Attacks
            {3}-- ARP Poisoning
            {4}-- VoIP / SIP Spoofing
            '''
            print(tools)
            choice = int(input(prompt))

        elif choice == 4:
          while Loop:
            Loop = 0
            os.system('cls')
            logo = colors.RANDOM + '''
             ____         __  __             ____                  __ _
            |  _ \       / _|/ _|           / __ \                / _| |
            | |_) |_   _| |_| |_ ___ _ __  | |  | |_   _____ _ __| |_| | _____      __
            |  _ <| | | |  _|  _/ _ \ '__| | |  | \ \ / / _ \ '__|  _| |/ _ \ \ /\ / /
            | |_) | |_| | | | ||  __/ |    | |__| |\ V /  __/ |  | | | | (_) \ V  V /
            |____/ \__,_|_| |_| \___|_|     \____/  \_/ \___|_|  |_| |_|\___/ \_/\_/
            '''
            print(logo)
            tools = colors.RED + '''
            {1}-- Windows 32bits
            {2}-- Linux 32bits
            '''
            print(tools)
            choice = int(input(prompt))

        elif choice == 5:
          os.system('cls')
          logo = colors.RANDOM + '''
           __          __  _       _    _            _    _
           \ \        / / | |     | |  | |          | |  (_)
            \ \  /\  / /__| |__   | |__| | __ _  ___| | ___ _ __   __ _
             \ \/  \/ / _ \ '_ \  |  __  |/ _` |/ __| |/ / | '_ \ / _` |
              \  /\  /  __/ |_) | | |  | | (_| | (__|   <| | | | | (_| |
               \/  \/ \___|_.__/  |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |
                                                                   __/ |
                                                                  |___/
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- XSS Scanner & Exploit
          {2}-- SQLi Scanner & Exploit
          {3}-- LFI / RFI Scanner
          {3}-- Enumeration
          {4}-- WordPress Scanner & Bruteforcer
          {5}-- DoS Attacks
          {6}-- DDoS Attacks
          {7}-- CSRF Scanner & Exploit
          '''
          print(tools)
          choice = int(input(prompt))

        elif choice == 6:
          os.system('cls')
          logo = colors.RANDOM + '''
            _____          _     ______            _       _ _        _   _
           |  __ \        | |   |  ____|          | |     (_) |      | | (_)
           | |__) |__  ___| |_  | |__  __  ___ __ | | ___  _| |_ __ _| |_ _  ___  _ __
           |  ___/ _ \/ __| __| |  __| \ \/ / '_ \| |/ _ \| | __/ _` | __| |/ _ \| '_ \
           | |  | (_) \__ \ |_  | |____ >  <| |_) | | (_) | | || (_| | |_| | (_) | | | |
           |_|   \___/|___/\__| |______/_/\_\ .__/|_|\___/|_|\__\__,_|\__|_|\___/|_| |_|
                                            | |
                                            |_|
          '''

        elif choice == 7:
          os.system('cls')
          logo = colors.RANDOM + '''
           ____             _       ______
          |  _ \           | |     |  ____|
          | |_) |_ __ _   _| |_ ___| |__ ___  _ __ ___ ___
          |  _ <| '__| | | | __/ _ \  __/ _ \| '__/ __/ _ \\
          | |_) | |  | |_| | ||  __/ | | (_) | | | (_|  __/
          |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- SSH
          {2}-- FTP
          {3}-- WordPress
          {4}-- G-Mail
          {5}-- Facebook
          {6}-- Zip File
          {7}-- Instagram
          {8}-- Twitter
          '''
          print(tools)
          choice = int(input(prompt))

        elif choice == 8:
          os.system('cls')
          logo = colors.RANDOM + '''
            ____      _       _
          /  __ \    (_)     | |
          | |  | |___ _ _ __ | |_
          | |  | / __| | '_ \| __|
          | |__| \__ \ | | | | |_
           \____/|___/_|_| |_|\__|
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- Instagram Info
          {2}-- Twitter Info
          {3}-- Person LookUp
          {4}-- Username LookUp
          {5}-- IP LookUp
          {6}-- Employee Search
          {7}-- Phone LookUp
          {8}-- Facial Recognition
          {9}-- LinkedIn LookUp
          {10}-- Geolocation
          '''
          print(tools)
          choice = int(input(prompt))

        elif choice == 9:
          os.system('cls')
          logo = colors.RANDOM + '''
          __          ___          _                         _   _             _
          \ \        / (_)        | |                   /\  | | | |           | |
           \ \  /\  / / _ _ __ ___| | ___  ___ ___     /  \ | |_| |_ __ _  ___| | _____
            \ \/  \/ / | | '__/ _ \ |/ _ \/ __/ __|   / /\ \| __| __/ _` |/ __| |/ / __|
             \  /\  /  | | | |  __/ |  __/\__ \__ \  / ____ \ |_| || (_| | (__|   <\__ \\
              \/  \/   |_|_|  \___|_|\___||___/___/ /_/    \_\__|\__\__,_|\___|_|\_\___/
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- Wireless Hijacking
          {2}-- DoS Attacks
          {3}-- Monitoring
          '''
          print(tools)
          choice = int(input(prompt))

        elif choice == 10:
          os.system('cls')
          logo = colors.RANDOM + '''
                                                       _
               /\                                     (_)
              /  \   _ __   ___  _ __  _   _ _ __ ___  _ _______
             / /\ \ | '_ \ / _ \| '_ \| | | | '_ ` _ \| |_  / _ \\
            / ____ \| | | | (_) | | | | |_| | | | | | | |/ /  __/
           /_/    \_\_| |_|\___/|_| |_|\__, |_| |_| |_|_/___\___|
                                        __/ |
                                       |___/
          '''
          print(logo)
          tools = colors.RED + '''
          {1}-- Set HTTP Proxy
          {2}-- Set HTTPS Proxy
          {3}-- Change MAC Adress
          {4}-- VPN (Personnal, ProtonVPN)
          '''
          print(tools)
          choice = int(input(prompt))
