#characters

define mc = Character("[mcname]")
define a = Character("Aphmau")
define ar = Character("Aaron")
define kc = Character("Kawaii-chan")
define k = Character("Katelyn")
define lu = Character("Lucinda")
define la = Character("Laurence")
define g = Character("Garroth")
define d = Character("Dante")
define t = Character("Travis")
define z = Character("Zane")
define q = Character("?")
define qq = Character("??")
define ty = Character("Tyler")

define new = Dissolve(0.3)

#flags

define aphflag = 0
define aarflag = 0
define katflag = 0
define kcflag = 0
define luciflag = 0
define laurflag = 0
define garflag = 0
define danflag = 0
define zaneflag = 0
define travflag = 0
define aphparty = 0
define gardanflag = 0
define kcconvflag = 0

#audio

define track1 = "audio/dream/vntrack01.mp3"
define track4 = "audio/dream/vntrack04.mp3"
define track6 = "audio/dream/vntrack06.mp3"
define track19 = "audio/dream/vntrack19.mp3"
#noon music ^
define aarlaugh = "audio/voice/AaronV/aarlaugh.mp3"
define aartease = "audio/voice/AaronV/aartease.mp3"

define aphperf = "audio/voice/AphmauV/aphperf.mp3"
define aphwhat = "audio/voice/AphmauV/aphwhat.mp3"
define aphlaugh = "audio/voice/AphmauV/aphlaugh.mp3"
define aphcry = "audio/voice/AphmauV/aphcry.mp3"

define danfine = "audio/voice/DanteV/danfine.mp3"
define danheybaby = "audio/voice/DanteV/danheybaby.mp3"
define danhuh = "audio/voice/DanteV/danhuh.mp3"

define garawesome = "audio/voice/GarrothV/garawesome.mp3"
define garaww = "audio/voice/GarrothV/garawesome.mp3"
define garsigh = "audio/voice/GarrothV/garsigh.mp3"
define garthanks = "audio/voice/GarrothV/garthanks.mp3"
define garlaugh = "audio/voice/GarrothV/garlaugh.mp3"

define katlaugh = "audio/voice/KatelynV/katlaugh.mp3"
define katmad = "audio/voice/KatelynV/katgrr.mp3"

define kchey = "audio/voice/Kawaii-ChanV/kchey.mp3"
define kcperfect = "audio/voice/Kawaii-ChanV/kcperfect.mp3"
define kcsad = "audio/voice/Kawaii-chanV/kccry.mp3"

define laurokay = "audio/voice/LaurenceV/laurokay.mp3"
define laurwhynot = "audio/voice/LaurenceV/laurwhynot.mp3"
define lauruhh = "audio/voice/LaurenceV/lauruhh.mp3"
define laurexactly = "audio/voice/LaurenceV/laurexactly.mp3"
define laurlaugh = "audio/voice/LaurenceV/laurlaugh.mp3"

define lucigotthis = "audio/voice/LucindaV/lucigotthis.mp3"
define lucilaugh = "audio/voice/LucindaV/lucilaugh.mp3"
define lucisigh = "audio/voice/LucindaV/lucisigh.mp3"
define luciohright = "audio/voice/LucindaV/lucioohright.mp3"

define travlaugh = "audio/voice/TravisV/travlaugh.mp3"
define travgroan = "audio/voice/TravisV/travgroan.mp3"
define travsad = "audio/voice/TravisV/travsad.mp3"

define zanethanks = "audio/voice/ZaneV/zanethanks.mp3"

define crunch = "audio/sound/crunch.mp3"
define wow = "audio/sound/wow.mp3"
define slip = "audio/sound/slip.mp3"
define doorbell = "audio/sound/doorbell.mp3" 

#CGs

init: 
    image laur_grocery_cg_1:
        "images/CGs/laur_grocery_cg_1.png"
init:
    image laur_grocery_cg_2:
        "images/CGs/laur_grocery_cg_2.png"


#sprites
init:
    image aarmad:
        "images/aaron/aarmad.png"
        zoom 0.4
init:
    image aarsad:
        "images/aaron/aarsad.png"
        zoom 0.4
init:
    image aarshock:
        "images/aaron/aarshock.png"
        zoom 0.4
init:
    image aarnorm:
        "images/aaron/aarnorm.png"
        zoom 0.4
init:
    image aarsmile:
        "images/aaron/aarsmile.png"
        zoom 0.4
init:
    image aphnorm:
        "images/aphmau/aphnorm.png"
        zoom 0.4
init:
    image aphsad:
        "images/aphmau/aphsad.png"
        zoom 0.4
init:
    image aphscare:
        "images/aphmau/aphscare.png"
        zoom 0.4
init:
    image aphlove:
        "images/aphmau/aphlove.png"
        zoom 0.4
init:
    image aphconf:
        "images/aphmau/aphconf.png"
        zoom 0.4
init:
    image dannorm: 
        "images/dante/dannorm.png"
        zoom 0.4
init:
    image dansmirk:
        "images/dante/dansmirk.png"
        zoom 0.4
init:
    image danmad:
        "images/dante/danmad.png"
        zoom 0.4
init:
    image danlaugh:
        "images/dante/danlaugh.png"
        zoom 0.4
init:
    image danscare:
        "images/dante/danscare.png"
        zoom 0.4
init:
    image garnorm:
        "images/garroth/garnorm.png"
        zoom 0.4
init:
    image garsad:
        "images/garroth/garsad.png"
        zoom 0.4
init:
    image garmad:
        "images/garroth/garmad.png"
        zoom 0.4
init:
    image garshock:
        "images/garroth/garshock.png"
        zoom 0.4
init:
    image katnorm: 
        "images/katelyn/katnorm.png"
        zoom 0.4
init:
    image katsmile:
        "images/katelyn/katsmile.png"
        zoom 0.4
init:
    image katdis:
        "images/katelyn/katdis.png"
        zoom 0.4
init:
    image katmad:
        "images/katelyn/katmad.png"
        zoom 0.4
init:
    image katlaugh:
        "images/katelyn/katlaugh.png"
        zoom 0.4
init:
    image kcnorm:  
        "images/kawaii-chan/kcnorm.png"
        zoom 0.4
init:
    image kcmad:
        "images/kawaii-chan/kcmad.png"
        zoom 0.4
init:
    image kcsad:
        "images/kawaii-chan/kcsad.png"
        zoom 0.4
init:
    image kcstar:
        "images/kawaii-chan/kcstar.png"
        zoom 0.4
init:
    image kcconf:
        "images/kawaii-chan/kcconf.png"
        zoom 0.4
init:
    image laurnorm:
        "images/laurence/laurnorm.png"
        zoom 0.4
init:
    image laurshock:
        "images/laurence/laurshock.png"
init:
    image laursad:
        "images/laurence/laursad.png"
        zoom 0.4
init:
    image laursmile:
        "images/laurence/laursmile.png"
        zoom 0.4
init:
    image laurdis:
        "images/laurence/laurdis.png"
        zoom 0.4
init:
    image lucinorm:
        "images/lucinda/lucinorm.png"
        zoom 0.4
init:
    image lucisad:
        "images/lucinda/lucisad.png"
        zoom 0.4
init:
    image lucismirk:
        "images/lucinda/lucismirk.png"
        zoom 0.4
init:
    image lucievil:
        "images/lucinda/lucievil.png"
        zoom 0.4
init:
    image zanenorm:
        "images/zane/zanenorm.png"
        zoom 0.4
init:
    image zanemad:
        "images/zane/zanemad.png"
        zoom 0.4
init:
    image zaneshock:
        "images/zane/zaneshock1.png"
        zoom 0.4
init:
    image travnorm:
        "images/travis/travnorm.png"
        zoom 0.4
init:
    image travshock:
        "images/travis/travshock.png"
        zoom 0.4
init:
    image travflirt:
        "images/travis/travflirt.png"
        zoom 0.4
init:
    image travlaugh:
        "images/travis/travlaugh.png"
        zoom 0.4
init:
    image travsad:
        "images/travis/travsad.png"
        zoom 0.4
init:
    image travscare:
        "images/travis/travscare.png"
        zoom 0.4


#backgrounds

init:
    image kitchen:
        "images/Backgrounds/Kitchen_day.png"
init:
    image boyshouse:
        "images/Backgrounds/Old_Outside.png"
init:
    image grocerystore:
        "images/Backgrounds/grocery_store.png"
init:
    image street:
        "images/Backgrounds/Street_Summer_Day.png"
init:
    image houseday:
        "images/Backgrounds/houseday.png"
init:
    image housenoon:
        "images/Backgrounds/housenoon.png"
init:
    image housenight:
        "images/Backgrounds/housenight.png"
init:
    image houseinside:
        "images/Backgrounds/houseinside.png"
init:
    image houseinsidedecor:
        "images/Backgrounds/houseinsidedecor.png"
init:
    image houseinsidedecornoon:
        "images/Backgrounds/houseinsidedecornoon.png"
init:
    image houseinsidenoon:
        "images/Backgrounds/houseinsidenoon.png"
init:
    image houseinsidenight:
        "images/Backgrounds/houseinsidenight.png"