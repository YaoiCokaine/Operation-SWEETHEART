label start:
    $ mcname = renpy.input("What is your name?")
    scene houseday with fade
    play music daysong1 loop
    "Phew! That should be the last of all the boxes!"
    "Who knew moving would be so tiresome?"
    "It'll all be worth it, as i'm finally a homeowner!"
    "Let's see what the inside of this home is like"
    scene houseinside with fade
    "Wooaahh! It's big!"
    "And already fully furnished? Crazy!"
    "I was able to get a spacious home in a nice neighbourhood, woohoo!"
    "Except...this is a completely new area...I don't know anyone here.."
    "I guess that's my new mission! Meet new people and make some friends! Maybe even find a sweetheart..."
    play sound doorbell
    "I should probably start unpacking my stuff, and then-"
    "Hm? Who could that be?"
    scene frontdoorday with fade
    mc "If you're from the IRS, then I told you, I need a little bit more time-"
    show aphnorm with dissolve
    q "Hi! You must be our new neighbour!!" 
    mc "Hm? Oh, yeah! I just moved here!"
    play sound aphperf
    q "I knew it! A little birdy told me we'd be meeting someone new~!"
    mc "What?"
    a "Nevermind that. I'm Aphmau! What's your name?"
    mc "I'm [mcname]"
    a "Cool! Well, i'm your next door neighbour on the right, and I live with two others, Katelyn and Kawaii-chan!"
    hide aphnorm
    show aphsad
    a "They were too busy to come meet you today.."
    mc "Oh, that's fine! I'm sure i'll see them around"
    hide aphsad
    show aphnorm
    a "You're right! You'll probably see the others too!"
    mc "The others?"
    a "We have a lot of friends on this block, I'd love for you to meet them all!"
    menu:
        "That's great":
            mc "That'd be great! I really do need some friends around here.."
            a "Don't worry! I've got you covered!"
            a "That gives me an idea actually..."
        "That's weird":
            mc "I barely know you and you're already trying to introduce me to your friends...? Kinda weird.."
            hide aphnorm
            show aphsad
            a "Well...it's always a good idea to get to know your neighbours..."
            hide aphsad
            show aphnorm
            a "Anyway!"
    a "You should throw a housewarming party and invite everyone! That way you can get to know all of the people here."
    a "I can even help you organize it!"
    "That does sound like a good idea...I really do need to meet everyone"
    menu:
        "Organize with Aphmau":
            $ aphflag += 1
            $ aphparty = True
            $ renpy.notify("Aphmau's looking forward to the party!")
            mc "That sounds fun! And I could really use your help"
            show aphlove 
            hide aphnorm 
            play sound aphperf
            a "Terrific! I'm a pretty great party planner. This is gonna be awesome!"
            hide aphlove 
            show aphnorm
            a "You can get settled in and we can discuss details later. Here! This is my number."
            mc "Thanks so much!"
            a "Anytime! That's what neighbours are for!"
        "Organize on your own":
            $ aphparty = False
            mc "That sounds fun, but I think i'll organize it on my own"
            hide aphnorm
            show aphsad
            play sound aphcry
            a "Aww...okay."
    a "Well, I'll see you around then! Looking forward to the party."
    hide aphnorm with dissolve
    hide aphsad with dissolve
    "She was nice. I should start thinking about that party."
    "But first, I should get all my stuff settled in..."
    scene bedroomday with fade
    "Alright! That's all the important stuff! I can do the rest tomorrow, I've done enough today."
    "I guess I could go outside and get some fresh air"
    scene street with fade
    "A walk will do me good!"
    q "YOU NEED TO TRUST ME!"
    "? what was that?"
    qq "I can't trust you! It's been 4 months!"
    q "Dude, just give me some time"
    qq "You've said that multiple times now!"
    "Sounds like there's some people nearby arguing...should I go meddle with that?"
    menu:
        "Check it out":
            "Let's go have a look-"
            jump choices1_a
        "Leave it be":
            "Not my business."
            jump choices1_b
label choices1_a:
    $ gardan = True
    $ kcconv = False
    scene boyshouse with fade
    show garmad at left with dissolve
    qq "You haven't paid your share of the rent, you can't keep getting away with it!"
    show danmad at right with dissolve
    q "dude. I told you. I got this. I'm working on it."
    qq "I really do not believe you"
    q "TRUUSSTTT!"
    play sound garsigh
    qq "*sigh* Dante, we really need you to be on time with your payments!"
    qq "Laurance and I have been covering your part, but we can't keep doing that for you!"
    d "I hear you, and I appreciate you, but trust me, I got this covered"
    hide garmad
    show garshock at left
    qq "Woah. Who are you?"
    mc "Oh. Uhh..."
    hide danmad
    show dansmirk at right
    d "Heheh. They're kinda cute..."
    mc "My name is [mcname]. I just moved here"
    qq "Ohhh! Are you the one moving next to Aphmau?"
    mc "Yup, that's me"
    hide garshock
    show garnorm at left
    g "It's nice to meet you! I'm Garroth!"
    d "[mcname], would you tell Garroth over here that if he gives me just a little bit more time, i'll be able to pay my rent?"
    menu:
        "Side with Dante":
            $ danflag += 1
            $ renpy.notify("Dante appreciates your support!")
            mc "I think you should trust him, Garroth, sounds like he's really being serious"
            hide garnorm
            show garsad at left
            g "I...well...fine..."
            g "But you need to pay it soon!"
            hide dansmirk
            show dannorm at right
            d "Dude! Don't worry! Have I ever let you down?"
            g "...well,"
        "Side with Garroth":
            $ garflag += 1
            $ renpy.notify("Garroth appreciates your support!")
            mc "This is serious, Dante...you need to be paying your rent on time!"
            g "See? Even [mcname] agrees!"
            hide dansmirk
            show danmad at right
            play sound danfine
            d "Dude. Whatever."
            d "I never said I WONT pay...just...later"
            g "I guess that's good enough for me"
    hide danmad
    show dannorm at right
    d "Anyway! [mcname], tell us a bit about yourself! Come on!"
    mc "Oh, well...i'm hosting a housewarming party! So I can get to know everyone better.."
    mc "Aphmau suggested it"
    hide garsad
    show garnorm at left
    g "Cool! When?"
    mc "Uhh...tomorrow night?"
    d "Sweet! We'll be there!"
    g "I'll make sure to tell the guys about this!"
    mc "Great!"
    "Hopefully that's enough time to organize the party..."
    mc "Well, I should get going, so I'll see you guys tomorrow!"
    scene street with fade
    jump choices1cont
label choices1_b:
    $ kcconv = True
    $ gardan = False
    "I guess I'll just sit out here for a bit..."
    show kcnorm with dissolve
    kc "Hmmm? Kawaii-chan has never seen you around here..are you new?"
    mc "Oh! Uh, yeah, I just moved here"
    play sound kcperfect
    kc "Oohhh! You're the one Aphmau-senpai talked about!"
    kc "My name is Kawaii-chan! It's nice to meet you!"
    mc "Ohhh, Aphmau told me a bit about you"
    kc "Ooo? What did she say??"
    mc "Just that you were busy today..."
    kc "Aphmau-senpai is right! Kawaii-chan is busy!!"
    kc "Kawaii-chan needs your help, I made some cookies while trying out a new recipe, and I need someone to try them out!"
    mc "Is that person....me?"
    kc "Yes! Kawaii-chan needs..."
    hide kcnorm
    show kcconf
    kc "Erm...what is your name..?"
    mc "Uh, [mcname]..."
    hide kcconf
    show kcnorm
    kc "Right! Kawaii-chan needs [mcname]-san to help out! Please try these cookies and tell me what you think!"
    "Should I be trying a stranger's cookies...?"
    menu:
        "Try the cookies":
            $ kcflag += 1
            $ renpy.notify("Kawaii-chan is glad you're helping her out!")
            hide kcnorm
            show kcstar
            play sound kcperfect
            kc "Ohhh, thankyouthankyouthankyouu!!!"
            kc "Here's one, try it and tell Kawaii-chan what you think!"
            "Alright...here it goes...let's hope this isn't laced..."
            play sound crunch
            "..."
            play sound wow
            "...!!!"
            mc "These...these are....GOOD..!!!"
            kc "AAAA! Kawaii-chan is so glad [mcname]-san likes them!"
            mc "Seriously! These are awesome!"
            mc "Say, Kawaii-chan, I'm throwing a housewarming party tomorrow, do you think you could bring these?"
            hide kcstar
            show kcnorm
            kc "Of course! Kawaii-chan would be happy to!"
            mc "That's great!"
        "Don't try them":
            mc "I'm fine, thanks.."
            hide kcnorm
            show kcsad
            kc "Oh...um..okay...."
            kc "Kawaii-chan can maybe ask Aphmau-senpai or Katelyn-sama..."
            mc "Yeah..sorry..."
            kc "It's okay...um."
            mc "You know, I'm having a housewarming party tomorrow night, I'd like for you to come!"
            hide kcsad
            show kcnorm 
            kc "Ooo! That sounds fun! Kawaii-chan would love to!"
            mc "Great!"
    mc "Well, I should probably get back inside now. I'll see you around, Kawaii-chan!"
    kc "See you around!!"
    hide kcnorm with dissolve
    "She was nice. A bit peculiar..."
label choices1cont:
    "I should probably make myself some dinner now. it's getting kinda late"
    scene houseinsidenoon with fade
    stop music
    play music noonsong loop
    "Woah! The sun is already starting to set."
    "I'm kind of too tired to make something for myself...maybe i'll just order something."
    "You know what? I worked hard today, I should reward myself with some pizza!"
    "I'll order it now and start thinking about that party in the mean time"
    if aphparty == True:
        "I guess I should call Aphmau to discuss some stuff...I hope she isn't busy!"
        "It's dialing...."
        a "Hello?"
        mc "Hi Aphmau! I was just calling because I wanted to talk about the party"
        a "Ooo, that's right! You don't have to worry at all about decorations and inviting people, I've got that completely covered! You just think about the food and drinks"
        mc "Oh, alright then! Thanks for everything!"
        a "Anytime! Now, I've gotta get back to what I was doing. I'll pop by tomorrow afternoon to help set up! Bye byeee!"
        "Glad to know she's got all of that taken care of"
        play sound doorbell
        "Food and drinks...I could make some pasta for everyone!"
    if aphparty == False:
        "How do you even organize a housewarming party? I guess I could cook some food for everyone.."
        "Hopefully pasta works..."
        "I can't wait to meet everyone. It seems like Aphmau will tell all her friends to come over, so maybe I can make some new friends too!"
        play sound doorbell
        "Right, I also need to look for a job here...that's gonna be tough..."
    "Oh wow, the pizza is already here!"
    scene frontdoornight with fade
    show tylerpizza with dissolve
    ty "Hey I'm Tyler"
    mc "Hi...Tyler! Are you the pizza delivery guy?"
    ty "No i'm just holding a pizza at your doorstep for no reason"
    mc "Oh, my apologies"
    ty "YES i'm the fucking pizza delivery guy omfg"
    mc "sorry"
    ty "Anyway did you just move here"
    mc "I did yeah. How'd you know?"
    ty "There's only like 9 people who live on this street so"
    mc "Oh wow"
    ty "yeah here's ur pizza. That's $100"
    mc "WHAT"
    ty "Jk lol it's $12. Wouldn't it be crazy tho if it was $100"
    menu:
        "That'd be funny":
            mc "Haha that would be kinda funny I think"
            ty "I know right haha"
            ty "Okay bye bye"
        "Get the fuck out":
            define tylermean = 0
            $ tylermean += 1
            mc "Can you just leave"
            ty "Wow. rude. Just wanted to make a fucking joke but seems like someone's a little grumpy today"
            mc "Just....leave"
            ty "Ok"
    hide tylerpizza with dissolve 
    "What an....interesting delivery guy."
    "And it's already dark out! I guess I should get some sleep now."
    scene bedroomnight with fade
    "Hopefully the party goes well tomorrow..."
    scene black with fade
    scene bedroomday with fade
    stop music
    play music daysong2 loop
    "A new day, a new slay! That's what the cool kids say."
    "I should probably go grocery shopping, I don't have much in the fridge..."
    "I think there should be one within walking distance"
    scene grocerystore with fade
    "Looks like I already got most of what I need..just need some milk"
    "I think it should be in this section-"
    play sound slip 
    "!!!" with vpunch
    "God...how did I not notice that wet floor sign..."
    q "Oh my!"
    scene laur_grocery_cg_1 with fade
    stop music
    play music daydream loop
    pause(2.0)
    q "Are you alright?"
    q "Do you need help getting up?"
    mc "Oh...I...uhh....yeas...."
    scene laur_grocery_cg_2 with dissolve
    q "Ha ha! Here, take my hand"
    scene grocerystore with fade
    show laurnorm with dissolve
    stop music
    play music daysong2 loop
    play sound laurokay
    q "The floor here is slippery, you should be careful"
    mc "Yeah no I got that"
    la "My name is Laurance, by the way."
    mc "I'm [mcname]...thanks for helping me up"
    if gardan == True: 
        mc "Wait a second, Laurance..I live across you!"
        hide laurnorm
        show laurdis
        la "Really? You just moved into that vacant home?"
        mc "Yeah! I did! Sorry, I recognized you because I talked to your roommates yesterday, Garroth and Dante?"
        hide laurdis
        show laurnorm
        la "Ahh, you were the cute person they were talking about"
        mc "haha...yeah..."
    hide laurnorm 
    show laursmile
    la "Oh right! Aphmau was telling me you were having a housewarming party today. I remember now"
    play sound lauruhh
    la "I need to get going, I still have to get you a gift ahaha"
    mc "Oh, you don't need to worry about a gift-"
    play sound laurwhynot
    la "No no, I insist, how else can I welcome you to the neighbourhood?"
    mc "In that case, i'm looking forward to it"
    la "And i'm looking forward to your party. See you around!"
    hide laursmile with dissolve
    "He was nice. Very handsome, too..."
    "Seems like I've gotten all my groceries, I should go home and start working on the party"
    if aphparty == True:
        jump aphpartyplan
    else:
        jump partyplan
    label aphpartyplan:
    scene houseinside with fade
    play sound doorbell
    "Aphmau should be coming soon to help out with the party-"
    "Oop! That's her!"
    scene frontdoorday with fade
    show aphnorm with dissolve
    a "I brought decorations!"
    mc "Woah! That's quite a few!"
    a "Of course! Every great party needs great decorations"
    scene aphmau_party_cg with fade
    pause (2.0)
    a "These balloons will really help give this place some more livelihood!"
    a "Hey, why don't you go put some streamers up?"
    mc "Oh, yeah, I'll do that-"
    mc "And Aphmau, thanks for helping out"
    a "Of course! You're new here, you need a friend to support you!"
    mc "You're...my friend?"
    a "I'd like to be!"
    mc "Well then..I'd also like to support you! As a friend!"
    play sound aphperf
    a "Hehe, great! I love making new friends"
    scene houseinsidedecor with fade
    show aphnorm with dissolve
    a "Alright! This party is gonna be a hoot and a holler!"
    a "People should start coming soon"
    jump partycont
    label partyplan:
    scene houseinside with fade
    "There's really not much I can do, now that I think about it..."
    "I guess I could prepare some pasta for everyone. Will the people like pasta?"
    scene kitchen with fade
    "Alright, just need to finish this up aandd...."
    "Boom! Meal is ready! I should also leave out some snacks as well.."
    "people should be coming soon"
    label partycont:
    play sound doorbell
    "I'm really excited to meet everyone!"
    "Oh, that's them...I'm so nervous!"
    scene frontdoorday with fade
    if aphparty == False:
        show aphnorm with dissolve
        a "Hi [mcname]!! I brought everyone that I could!"
        mc "That's great! Thanks so much"
        a "No problem! I got you this cool scented candle as a gift. I hope you like it!"
        mc "It's lovely, thank you"
        hide aphnorm with dissolve 
    show katnorm at left with dissolve
    show kcnorm at right with dissolve
    if kcconv == True:
        kc "Hey [mcname]-san!! Thanks for inviting us!"
        mc "Of course! I'm so glad you made it!"
        k "Hi, i'm Katelyn. We're both Aphmau's roommates"
        mc "Oh, it's great to meet you! I'm really looking forward to making friends here"
        k "yea yea"
        if kcflag == 1:
            kc "Well, Kawaii-chan knows how much you liked my cookies from yesterday, so I made some more!"
            mc "Oooo, yes! Thanks so much Kawaii-chan!"
            kc "Of course!"
        else:
            k "We brought this nice wine and bought some cool wine glasses to come with"
            mc "Oh wow, that's a lot, thanks so much you guys!"
            hide katnorm 
            show katdis at left
            k "See, Kawaii-chan? I knew this was too much!"
            hide kcnorm
            show kcmad at right
            play sound kchey
            kc "Ohhh, come on! It's not THAT much!!"
    if kcconv == False:
        mc "Hey guys! Welcome to the party!"
        k "Hey. I'm Katelyn, and this is Kawaii-chan"
        mc "It's great to meet the two of you! Your Aphmau's roommates, right?"
        kc "Yup! Kawaii-chan hopes we can all become great friends!"
        menu:
            "We'll see":
                mc "We'll have to see about that..."
            "I agree":
                mc "I'm looking forward to it!"
        k "We brought this nice wine and bought some cool wine glasses to come with"
        mc "Oh wow, that's a lot, thanks so much you guys!"
        hide katnorm 
        show katdis at left
        k "See, Kawaii-chan? I knew this was too much!"
        hide kcnorm
        show kcmad at right
        play sound kchey
        kc "Ohhh, come on! It's not THAT much!!"
    hide kcmad with dissolve
    hide katdis with dissolve       
    hide kcnorm with dissolve
    hide katnorm with dissolve 
    show lucinorm with dissolve
    lu "Hey [mcname], i'm Lucinda. I'm a couple houses down from here, nice to meet you"
    mc "Nice to meet you too! Come in."
    lu "Oh, right, I got you this giftcard for CreamyDreamy Coffee Co. , it's a coffee shop nearby"
    mc "Ohhh, that's cool! Thanks!"
    hide lucinorm with dissolve
    show laursmile with dissolve
    la "Hey again, [mcname]!"
    show garnorm at left with dissolve
    show dannorm at right with dissolve
    if gardan:
        if garflag == 1:
            g "Hiya [mcname]!"
            mc "Hey Garroth! Great to see you! You too, Dante"
            g "We've really been looking forward to this party. It's all I could think about!" 
            d "Ha. Laaaaamee"
            hide garnorm
            show garmad at left
            g "SHUT UP!"
            mc "Woaah, ahah. Lets calm down.."
        if danflag ==1:
            d "Whats poppin, [mcname]?"
            mc "Haha, not much"
            hide laursmile
            show laurdis
            la "What's 'poppin'?"
            hide dannorm
            show danmad at right 
            d "Yea? What's wrong with that, pretty boy?"
            la "Okay whatever"
    else:
        g "Hello! My name's Garroth!"
        d "My name is Dante-"
        hide dannorm
        show dansmirk at right
        play sound danheybaby
        d "You could call me babe if you'd like~"
        hide garnorm
        hide laursmile
        show laurdis 
        show garmad at left
        g "Dude."
        la "Come on man we just got here"
        hide dansmirk
        show danmad at right
        play sound danfine
        d "Sorry I thought i'd give it a try."
    hide laurdis
    hide danmad
    hide garmad
    hide danmad
    show dannorm at right
    show laurnorm
    show garnorm at left
    g "Oh, we also have a 4th buddy, Travis, but he's just running a bit late!"
    la "He said he's doing something important right now?"
    d "I bet he's suckin cock"
    hide laurnorm
    show laurdis
    la "Dude?"
    d "My bad"
    hide laurdis
    show laurnorm
    la "Anyway. Me and the guys all worked together on this. We got you these flowers! We hand-picked them ourselves"
    hide laurnorm
    hide garnorm
    hide dannorm
    show laursad
    show garsad at left
    show danmad at right
    g "They um. They welted a little bit."
    d "Yeah we kinda forgot to put them in soil....and sunlight...and..water...."
    la "And some of these might be weeds..."
    menu:
        "This is awful":
            mc "This....this is awful. These smell disgusting oh my god"
            d "Yeah we probably should've took better care of them"
            mc "Yeah just...please get rid of those before you come in..."
            play sound garaww
            g "I'll go do that..."
        "This is beautiful":
            $ danflag += 1
            $ garflag += 1
            $ laurflag += 1
            mc "It's cute though! It's the thought that counts. Clearly you guys worked hard on these"
            $ renpy.notify ("The boys all liked your gratitude!")
            hide laursad
            hide garsad
            hide danmad
            show laursmile
            show garnorm at left
            show dannorm at right
            play sound garthanks
            g "Right! We did work hard!"
            d "We're glad you like them!"
    hide danmad with dissolve
    hide garsad with dissolve
    hide laursad with dissolve
    hide garnorm with dissolve
    hide laursmile with dissolve
    hide dannorm with dissolve
    show zanenorm with dissolve
    z "Hello...i'm Zane. Aphmau's friend."
    mc "Nice to meet you Zane! I'm [mcname], i'm glad you could make it"
    z "Whatever"
    hide zanenorm with dissolve
    "No gift...?"
    show aarnorm with dissolve
    ar "Hey, i'm Aaron, i'm good friends with Aphmau. It's nice to meet you"
    mc "Great to meet you, Aaron! I'm [mcname]."
    ar "I brought this bowl thing...I don't know, I thought it looked nice, so you could use it for decoration or something"
    mc "Oh, sweet! This is really nice! Thanks so much, Aaron"
    hide aarnorm
    show aarsmile
    ar "Anytime"
    hide aarsmile with dissolve
    "That should be everyone-"
    q "WAIT! I'M HERE!"
    show travnorm with dissolve
    t "I'm here..! I'm here...! I'm Travis!"
    mc "Right! You're with Laurance and those guys!"
    t "Yeah..! Sorry...I ran here..."
    mc "What were you doing before you got here?"
    t "Suckin cock"
    mc "Oh"
    play sound travlaugh
    t "Haha jk. Just had some business"
    mc "..right. Come on in, we've got everyone"
    if aphparty == True:
        scene houseinsidedecor with fade
        show lucismirk with dissolve
        lu "Wow, [mcname], you really decorated this place"
        mc "Haha, that was all Aphmau, but i'm glad you like it!"
        hide lucismirk with dissolve
        show laurnorm with new
    else:
        scene houseinsidedecor with fade
        show laurnorm with dissolve
    la "Mm, this pasta is very good, did you make it yourself, [mcname]?"
    mc "I did, yeah!"
    show katsmile at left with dissolve
    k "This is delicious, you're a great cook"
    mc "Haha, it's nothing, just a family recipe.."
    show zanenorm at right with dissolve
    z "It's alright, I suppose..."
    hide katsmile
    show dansmirk at left with new
    d "Is that why you're already on your third plate, Zane?"
    hide zanenorm
    show zanemad at right
    play sound zanemad
    z "I'M JUST HUNGRY!"
    d "Suuurree"
    z "Whatever..."
    hide laurnorm
    show garmad with new
    g "Zane! Be nice!"
    hide zanemad
    show zanenorm at right
    z "...the pasta is good, [mcname]."
    hide garmad
    show garnorm
    g "That's a good boy, Zuzu!"
    hide zanenorm
    show zanemad at right
    z "WHAT IS WRONG WITH YOU"
    hide zanemad
    hide garnorm
    hide dansmirk
    show lucinorm with new
    lu "Okay enough of that"
    lu "[mcname], why don't you tell us a bit about yourself?"
    mc "Oh, well...there's not much to say..."
    show katnorm at right with dissolve
    k "Well, why'd you move here? Any reason?"
    menu:
        "To escape from my past":
            mc "Well, I guess I just wanted to run away from my past...try to start fresh, y'know?"
            hide lucinorm
            hide katnorm
            show aarsad with new
            $ renpy.notify ("Aaron can relate to you!")
            $ aarflag += 1
            ar "I get that...wanting to leave all your troubles behind...your mistakes..."
            mc "Yeah.."
            show travshock at right with dissolve
            t "Dude, were you a mafia leader or something?"
            mc "What? No..I just-"
            show danlaugh at left with dissolve
            # TODO: DANLAUGH
            d "Haha! I bet they're a hitman! Or an assassin!"
            hide travshock
            show travlaugh at right
            play sound travlaugh
            t "YOOOOO AHAHAHAHAHAH"
            hide travlaugh
            hide danlaugh
            show travshock at right
            show danmad at left
            pause (3.0)
            d "...you didn't come here to kill us, did you?"
            hide aarsad
            show aarmad
            ar "Guys! What's wrong with you!?"
            menu:
                "I am here to kill you":
                    mc "You caught me! I'm here to kill you all!"
                    hide danmad
                    hide travshock
                    show danscare at left
                    show travscare at right
                    define b = Character("Both",color="#FFFFFF")
                    play sound dancry
                    play sound travcry
                    b "AAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!" with hpunch
                    hide aarmad
                    show laurdis with new
                    la "Obviously they're joking guys"
                    hide danscare
                    hide travscare
                    show danmad at left
                    show travshock at right
                    t "yeah.. obviously we knew that"
                    d "totally"
                "What are you talking about":
                    mc "No i'm literally just some guy"
                    d "....we'll believe you"
                    t "for now..."
                    mc "ohkay"
        "To try something new":
            mc "I guess I just wanted to try something new, look for some adventure, maybe?"
            hide lucinorm
            show lucismirk
            $ renpy.notify ("Lucinda thinks you're interesting!")
            lu "Ooo, adventurous, I like it"
            lu "I'll definitely make sure to take you to cool places here"
            mc "I'd love that!"
            k "Where would you guys even go? There's honestly not much to do around here..."
            lu "Wouldn't you like to know?"
            show garnorm at left with dissolve
            g "Sounds fun! Can I join?"
            hide lucismirk 
            show lucinorm
            lu "Absolutely not"
            hide garnorm
            show garsad at left
            play sound garaww
            g "Awww, why not??"
            k "I can't believe Lucinda is gatekeeping the neighbourhood from it's residents"
            lu "If I took you guys to my special places, all you'd do is ruin it"
            hide garsad
            show laurdis at left with new
            la "Wait, you're saying you know about secret areas around here?"
            lu "Yeah? Of course?"
            hide katnorm
            show danmad at right with new
            play sound danhuh
            d "And you just never told anyone?? How long have you known about them???"
            lu "Since we first moved here? Besides, why would I tell anyone?"
            hide lucinorm
            show lucismirk
            play sound lucilaugh
            lu "Then it's not a secret~"
            d "Oh yeah but [mcname] is allowed to know about it"
            lu "Yeah, cuz they're actually cool, unlike you guys"
            mc "Oh wow"
    hide lucismirk
    hide danmad
    hide laurdis
    hide aarmad
    hide travshock
    hide travlaugh
    show aphnorm with new
    a "Either way, [mcname], we're all very glad to have you here now!"
    show kcnorm at left with dissolve
    kc "Kawaii-chan hopes we can all become great friends!"
    mc "I hope so too, Kawaii-chan!"
    if aphparty == True:
        scene houseinsidedecornoon with fade
    else:
        scene houseinsidenoon with fade
    "Seems like everyone's broken off into their own groups...who should I join?"
    menu:
        "Aphmau, Kawaii-chan":
            $ aphchan = True
            $ laurrest = False
            $ aarrest = False
            $ garrest = False
            $ lucikat = False
            $ travzandan = False
            jump aphchanconv
        "Lucinda, Katelyn":
            $ aphchan = False
            $ laurrest = False
            $ aarrest = False
            $ garrest = False
            $ lucikat = True
            $ travzandan = False
            jump lucikatconv
        "Laurance, Garroth, Aaron":
            $ aphchan = False
            $ lucikat = False
            $ travzandan = False
            jump laurgaraarconv
        "Travis, Zane, Dante":
            $ aphchan = False
            $ laurrest = False
            $ aarrest = False
            $ garrest = False
            $ lucikat = False
            $ travzandan = True
            jump travzandanconv
    label aphchanconv:
        $ renpy.notify("Aphmau and Kawaii-chan are glad to talk to you!")
        $ aphflag += 1
        $ kcflag += 1
        "Let's see what Aphmau and Kawaii-chan are up to!"
        if kcflag == 2:
            show aphlove at left with dissolve
            show kcnorm at right with dissolve
            a "Kawaii-chan!! These cookies are absolutely awesome!!!"
            kc "Hehe! Kawaii-chan is so glad Aphmau-senpai loves them!"
        else:
            show aphnorm at left with dissolve
            show kcnorm at right with dissolve
        a "Oh, [mcname]! Hey!"
        kc "This party is great, [mcname]!"
        mc "Haha I didn't do much, but i'm glad you like it, Kawaii-chan!"
        mc "So, what were you guys talking about?"
        a "Kawaii-chan and I were just discussing getting coffee tomorrow and hanging out for a bit"
        hide kcnorm 
        show kcstar at right
        kc "Ooo! [mcname], you should come with us!! We can all hang out and get to know you more!"
        mc "Sure! I'll come with!"
        play sound kcperfect
        kc "YAAY!!"
        a "We'll take you to CreamyDreamy Coffe Co! Its the GREATEST coffee shop ever!"
        mc "Right, Lucinda actually gave me a gift card for that place, perfect!"
        hide kcstar
        show kcnorm at right
        kc "We're gonna have so much fun!!"
        mc "Well, it's just coffee..."
        hide kcnorm
        show kcmad at right
        play sound kchey
        kc "It's more than just coffee! It's a chance to bond!"
        t "EVERYONE! I'D LIKE TO MAKE A TOAST!"
        jump travtoast
    label lucikatconv:
        $ renpy.notify("Lucinda and Katelyn are glad to talk to you!")
        $ luciflag += 1
        $ katflag += 1
        "Let's see what Lucinda and Katelyn are up to!"
        show lucinorm at left with dissolve
        show katnorm at right with dissolve
        lu "You don't know what you're talking about"
        k "Oh yeah? We should put this to the test, then!"
        mc "Hey guys! What are you two talking about?"
        k "Lucinda here thinks she's the better bowler than me-"
        hide lucinorm
        show lucismirk at left
        lu "Cuz I am"
        hide katnorm
        show katdis at right
        k "...right. You know what?"
        hide katdis
        show katsmile at right
        k "Lucinda, I challenge you to a bowling contest tomorrow!"
        k "And [mcname], you'll come along too, to judge us!"
        mc "What? Me??"
        play sound lucilaugh
        lu "Ahaha, yes! You'll have to decide which of us is better at bowling"
        hide katsmile
        show katnorm at right
        k "It's gonna be me, by the way."
        lu "We'll see about that~"
        t "EVERYONE! I'D LIKE TO MAKE A TOAST!"
        jump travtoast
    label laurgaraarconv:
        $ garflag += 1
        $ laurflag += 1
        $ aarflag += 1
        $ renpy.notify("Laurance, Garroth, and Aaron are glad to talk to you!")
        "Let's see with Laurance, Garroth, and Aaron are up to!"
        show aarnorm at left with dissolve
        show laurnorm with dissolve
        show garnorm at right with dissolve 
        g "Hey [mcname]! We're all having a blast at your party!"
        mc "Ahaha, thanks. I'd hardly call this a party, though"
        ar "We're all enjoying ourselves nonetheless, so I'd call that a job well-done"
        mc "That's good to know. What were you guys talking about?"
        la "Well, we were all thinking of what the best restaurant around here is that we could introduce you to"
        la "I was saying it's Piping Hot Pizza Palace, truly undefeated"
        ar "Nuh uh, best restaurant is definitely the Sizzling Sausage Shack. Their food is on a whole 'nother level!"
        hide garnorm
        show garmad at right
        g "Nope! Both of you are wrong! Best restaurant is the Cloud 9 Nice Ice Cream Parlour!"
        hide laurnorm
        show laurdis 
        la "That's an ice cream parlour?"
        g "Yeah?"
        ar "That doesn't count"
        hide garmad
        show garsad at right
        play sound garaww
        g "Aww, why not?"
        menu:
            "Piping Hot Pizza Palace sounds the best":
                $ laurrest = True
                $ aarrest = False
                $ garrest = False
                $ laurflag += 1
                mc "I think Piping Hot Pizza Palace sounds the best, I love me a good pizza!"
                hide laurdis
                show laursmile
                $ renpy.notify("Laurance is glad you like his suggestion!")
                play sound laurexactly
                la "It's so good! You're gonna love it, [mcname]."
                la "We should go tomorrow, you'll see just how great it is."
                mc "Looking forward to it!"
                g "Whatever...who want's piping hot pizza or sizzling sausages in this weather? A nice, cool ice-cream is perfect.."
            "Sizzling Sausage Shack sounds the best":
                $ aarrest = True
                $ garrest = False
                $ laurrest = False
                $ aarflag += 1
                mc "I think Sizzling Sausage Shack sounds the best, I love me a good sausage!"
                hide garsad
                show garnorm at right
                play sound garlaugh
                g "pfft...love me a good sausage..."
                hide aarnorm
                show aarmad at left
                ar "What's so funny, Garroth?"
                hide garnorm
                show garshock at right
                g "Nothing! Nothing, Big Man!"
                ar "Anyway..."
                hide aarmad
                show aarsmile at left
                $ renpy.notify("Aaron is glad you like his suggestion!")
                ar "It is the best! Guess you could say Real Recognizes Real"
                ar "Why don't I take you there tomorrow? It truly is great"
                mc "That sounds fun! I'm in!"
            "Cloud 9 Nice Ice Cream Parlour sounds the best":
                $ garrest = True
                $ laurrest = False
                $ aarrest = False
                $ garflag += 1
                mc "Who said it shouldn't count? I think Cloud 9 Nice Ice Cream Parlour sounds the best. Love me some ice cream!"
                hide garsad
                show garnorm at right
                play sound garawesome
                $ renpy.notify("Garroth is glad you like his suggestion!")
                g "I knew you'd agree with me, [mcname]!"
                la "But that's ice cream...that's not a proper restaurant..."
                g "You're just mad your restaurant isn't as good as Cloud 9 Nice Ice Cream Parlour!"
                la "No I don't think I am"
                g "[mcname], we'll go get ice cream together so you can see just how good it is!"
                mc "That sounds fun, let's do that!"
                g "Yippee!"
                a "Yippee..?"
        t "EVERYONE! I'D LIKE TO MAKE A TOAST!"
        jump travtoast
    label travzandanconv:
        $ travflag += 1
        $ zaneflag += 1
        $ danflag += 1
        $ renpy.notify("Travis, Zane, and Dante are glad to talk to you!")
        mc "Let's go see what Travis, Zane, and Dante are up to!" 
        show travnorm at left with dissolve
        show zanenorm with dissolve
        show dannorm at right with dissolve
        t "-and then I said, that's not a camel, that's my wife!"
        hide dannorm
        hide travnorm
        show travlaugh at left
        show danlaugh at right
        play sound danlaugh
        d "AHAHA!! TOO GOOODD"
        hide zanenorm
        show zanemad
        z "That wasn't funny at all..."
        hide travlaugh
        show travshock at left
        t "No no dude you need to hear it again."
        t "So two guys walk into a bar-"
        mc "Hey guys! What are you all talking about?"
        hide danlaugh
        show dannorm at right
        d "Haha nothing, Travis was just cracking some jokes"
        z "I'd hardly call that a joke, wasn't funny at all,"
        z "I don't even think there was a punchline?"
        t "You just wouldn't get humour, my guy"
        z "BUT IT'S NOT HUMOUR! IT'S NOT FUNNY IF THERE IS NO PUNCHLINE!!"
        t "Nah but it was tho"
        z "Oh my fucking god"
        menu:
            "Joke was funny":
                $ travflag +=1 
                mc "I don't know, I thought it was pretty funny"
                $ renpy.notify("Travis appreciates your support!")
                hide travshock
                show travnorm at left
                t "Knew you were a comedy connoisseur! See, Zane? Majority wins"
                hide dannorm
                show danmad at right
                d "Dude, am I not enough for you?"
                hide travnorm
                show travsad at left
                play sound travsad
                t "Noo it isn't like that...come on man you're more than enough for me"
                hide danmad
                show dannorm at right
                d "Awww...thanks man."
                z "This is what happens when you enable them"
                mc "Right"
            "Joke wasn't funny":
                $ zaneflag += 1
                mc "Yeah no that wasn't funny at all"
                $ renpy.notify("Zane appreciates your support!")
                hide zanemad
                show zanenorm
                play sound zanethanks
                z "Glad to know someone else has common sense as well..."
                t "Duuudee it's funny in like...an ironic way.."
                hide dannorm 
                show danmad at right
                d "Yeah it's like...satire yo"
                mc "Is it?"
                d "...yea no not really I guess"
                t "DUDE?"
                d "Nah they're right I think you can do better"
                play sound travsad
                t "Whatever man you guys don't get real comedy"
        hide zanemad
        show zanenorm
        z "You guys will learn about real comedy tomorrow, I hope"
        mc "What's happening tomorrow?"
        hide danmad
        show dannorm at right
        d "We're gonna watch a movie tomorrow, apparently it's the funniest movie of the year or something"
        hide travshock
        hide travsad
        show travnorm at left
        t "It's called 'Killer Babez VS MICHAEL'"
        mc "...who's Michael?"
        d "I guess we're gonna find out..."
        d "Oh my god! Dude, you should definitely come watch it with us!"
        t "Oh duude! You have to!"
        hide dannorm
        show dansmirk at right
        play sound danheybaby
        d "You'd fit in with all the killer babes, definitely"
        z "You cannot be saying that"
        mc "That sounds very fun! I'd love to come with"
        z "hah, the more the merrier..."
        t "Exactly!"
        z "No I was joking"
        hide travnorm
        show travshock at left
        t "Interesting, I don't recall there being a punchline there?"
        z "Omfg"
        hide dansmirk
        show dannorm at right
        d "Tomorrow's gonna be so much fun. Oh yeah, forgot to mention, this party's been great man"
        hide travshock
        show travnorm at left
        t "Truly! You know what? I'm gonna do a toast!"
        mc "No that's not necessary-"
        t "EVERYONE! I'D LIKE TO MAKE A TOAST!"
    label travtoast:
        scene houseinsidedecornoon with fade
        show travnorm with dissolve
        t "Here's a toast, to our new beloved friend, [mcname]!"
        define e = Character("Everyone",color="#FFFFFF")
        e "WOOOOOO!!"
        t "Here's to welcoming [mcname] to our lovely neighbourhood!!"
        e "YEAAHH!!!!"
        mc "Aww...you guys....stawp it..."
        scene black with dissolve
        "Some partying later..."
scene houseinsidenight with fade
stop music
play music nightsong loop
"Everyone's gone home now."
if aphparty == True:
    "And I finally got all of these decorations down..."
"Man, i'm so tired!"
"But i'm really looking forward to tomorrow!"
if aphchan == True:
    "I can't wait to hang out with Aphmau and Kawaii-Chan. Hopefully I can get to know them better!"
    "Also looking forward to using Lucinda's gift card, apparently the CreamyDreamy coffee is spectacular."
if lucikat == True:
    "I can't wait to go bowling with Katelyn and Lucinda!"
    "Or well...I guess I'm not bowling, i'm just watching them bowl...but that'll probably be fun, too!"
if laurrest == True:
    "I can't wait to go to Piping Hot Pizza Palace with Laurance! It sounds soooo good..."
    "It'll also be great to spend some time with Laurance and get to know him more!"
if aarrest == True:
    "I can't wait to go to Sizzling Sausage Shack with Aaron! It sounds soooo good..."
    "It'll also be great to spend some time with Aaron and get to know him more!"  
if garrest == True:
    "I can't wait to go to Cloud 9 Nice Ice Cream Parlour with Garroth! It sounds soooo good..."
    "It'll also be great to spend some time with Garroth and get to know him more!" 
if travzandan == True :
    "I can't wait to go to the movies with Zane, Travis, and Dante tomorrow!"
    "Sounds like it'll be a really funny movie, and hopefully I can bond with the guys more!"
play sound doorbell
"I should probably go to bed now.."
"? Who's here at this time?"
scene frontdoornight with fade
show tylernorm with dissolve
ty "Hey"
mc "...you?"
ty "You remember me right"
mc "Yeah no you're um. I wanna say Taylor?"
ty "Tyler but yeah"
ty "I know what you're doing"
mc "What?"
ty "I've been here long enough to sense an imbalance"
mc "What are you talking about i'm so lost"
ty "What you're doing is RECKLESS....continue this path and bad things will ensue.."
mc "Okay I'm calling the cops"
ty "NO WAIT sorry I was trying out this new mysterious thing"
ty "Anyway...let me just say, I've been watching your interactions with the people of this street"
mc "Totally not weird at all"
ty "And I can tell that one of the residents here has caught your eye...you're in love"
mc "Wh- How'd you know I like-"
ty "Don't worry, I can tell...you don't have to say it.."
ty "But let me warn you. You need to be careful."
ty "Be careful with how you interact with everyone. You don't want to be too affectionate with everyone, just focus on your little crush."
ty "I'm just saying, if you don't actively target one person, bad things might happen.."
menu:
    "Will keep that in mind":
        mc "Right...definitely. Totally get what you're saying"
    "You're a weirdo":
        $ tylermean += 1
        mc "Okay you're a creep no offence"
ty "I'm just saying, if you really want to be with your one person, then really dedicate yourself to that one person. If you mess around..you might get an ending you're not happy with"
mc "an 'ending'? What is that supposed to mean?"
ty "You will learn as time goes on"
mc "Hey man don't you have pizzas to deliver"
ty "Farewell, [mcname]"
hide tylernorm with dissolve
"Jesus christ that guy is weird"
scene bedroomnight with fade
"I need to go to sleep now"
"That guy was...really creepy...but maybe he's right"
"I can't be fooling around too much...I should be careful with how I progress from here"
scene black with fade
pause (2.0)
scene bedroomday with fade
stop music
play music daysong1 loop
"*yaawn* What a beautiful morning!"
if aphchan == True:
    "I should probably get ready to get coffee with Aphmau and Kawaii-chan."
if lucikat == True:
    "I should probably get ready to go bowling with Lucinda and Katelyn."
if laurrest == True:
    "I should probably get ready to go to Piping Hot Pizza Palace with Laurance."
if aarrest == True:
    "I should probably get ready to go to Sizzling Sausage Shack with Aaron." 
if garrest == True:
    "I should probably get ready to go to Cloud 9 Nice Ice Cream Parlour."
if travzandan == True:
    "I should probably get ready to go watch Killer Babez VS MICHAEL with the guys."
if aphchan == True:
    jump aphchancoffee
if lucikat == True:
    jump lucikatbowl
if laurrest == True:
    jump laurpizza
if aarrest == True:
    jump aarsausage
if garrest == True:
    jump garcream
if travzandan == True:
    jump guymovie
label aphchancoffee:
    scene houseday with fade
    "I guess I should just wait out here"
    show aphnorm at left with dissolve
    show kcnorm at right with dissolve
    a "Hi [mcname]! Hopefully we didn't keep you waiting for too long!"
    mc "Oh, no, not at all!"
    kc "We should get going!"
    scene coffeeshop with fade
    show kcnorm at left with dissolve
    kc "This place is awesome, [mcname]-san will love it for sure!"
    show aphlove at right with dissolve
    a "Aaa! I haven't had coffee here in so long!! I've been really yearning for this.."
    mc "Man...this must be some damn good coffee"
    a "It's more than just coffee...it's divine necter derived from the gods..."
    mc "...right"
    kc "We should probably order now! We're next in line!"
    show tylercoffee with dissolve
    ty "Hey guys welcome to CreamyDreamy Coffee Co. what can I squeeze outta bean for ya"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.."
    hide aphlove
    hide kcnorm
    show kcconf at left
    show aphconf at right 
    a "[mcname]? You know this guy?"
    mc "I- no...sorry...you guys just order..."
    hide kcconf
    show kcnorm at left
    hide aphconf
    show aphnorm at right
    kc "I'd like the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice please!"
    kc "[mcname]-san should get it too!"
    a "-and I'll have the Psychedelic Pop-Rock Espresso!"
    a "Seriously, [mcname], it's the best"
    mc "Jesus those can't be real"
    ty "Okay I have a mega ultra whatever and psychedelic shit-show coming up. What about you?"
    menu:
        "Psychedelic Pop-Rock Espresso":
            $ aphflag += 1
            $ poprock = True
            $ chaoschalice = False
            $ thirdthing = False
            mc "I'll have the Psychedelic Pop-Rock Espresso as well."
            $ renpy.notify("Aphmau's glad you took her suggestion!")
            play sound aphperf
            hide aphnorm
            show aphlove at right
            a "Hahaa! Yayy!!"
            hide kcnorm
            show kcsad at left
            kc "Aww...Kawaii-chan really wanted you to try the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice..."
        "Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice":
            $ kcflag +=  1
            $ chaoschalice = True
            $ poprock = False
            $ thirdthing = False
            mc "I'll have the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice as well."
            $ renpy.notify("Kawaii-chan's glad you took her suggestion!")   
            hide kcnorm
            show kcstar at left
            play sound kcperfect
            kc "Yayy!! Kawaii-chan knows [mcname]-san will love it!"
            hide aphnorm
            show aphsad at right
            a "Aww..I thought you'd try the Psychedelic Pop-Rock Espresso..."
        "A secret third thing":
            $ thirdthing = True
            $ poprock = False
            $ chaoschalice = False
            mc "Um...I'll get something else.."
            ty "Right, one Make-A-Choice Creamer Dreamer special for you"
            mc "What? I didn't even order-"
            ty "It's what we give to our particularly non-decisive customers"
            menu:
                "Fuck you bitch":
                    $ tylermean += 1
                    mc "Okay wow fuck you bitch damn"
                    ty "HEY I can call security on you"
                    mc "Whatever"
                "Thanks":
                    mc "Thanks..."
                    ty "No problem man it's actually a special i've been working on for a while"
                    mc "Right yeah don't care"
    ty "Anyway i'll get all of that squeezed out for ya"
    hide kcnorm with easeoutleft
    hide aphnorm with easeoutleft
    hide kcsad with easeoutleft
    hide aphsad with easeoutleft
    hide kcstar with easeoutleft
    hide aphlove with easeoutleft
    ty "[mcname]- stay back..."
    mc "Wsg gang"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    a "[mcname]! Everything okay over there?"
    mc "I'm coming Aphmau!"
    menu:
        "I don't need your help":
            $ tylermean +=1 
            mc "Listen, Tyler, I don't need your help. Quite frankly, you're freaking me out, so just leave me alone, okay?"
            if tylermean == 4:
                ty "...."
                ty "if that's what you wish for...Tyler will comply..."
                mc "Ohkay. You know what I- goodbye"
            else:
                ty "You don't get it, man! You need this! You need me!"
                mc "Whatever you say man"
        "Thanks for your help":
            mc "Thanks for the help, even if i'm not sure what you're talking about, i'll keep your advice in mind"
            ty "Good...now go get em tiger!"
            mc "Don't ever call me that ever again"
    if chaoschalice == True:
        scene kawaiichan_coffee_cg_1 with fade
        stop music
        play music daydream loop
        pause (2.0)
        play sound wow
        kc "Nyaaaa~ Isn't the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice so good??"
        mc "Woah...it really is!"
        scene kawaiichan_coffee_cg_2 with dissolve
        kc "Kawaii-chan knew [mcname]-san would love it!"
        kc "Isn't Kawaii-chan the best~~"
        mc "Haha, you are pretty great!"
        a "You really should try the Psychedelic Pop-Rock Espresso next time..."
        mc "I'll definitely try it, no worries"
        scene coffeeshop with fade
        stop music
        play music daysong2 loop
        show aphnorm at left with dissolve
        show kcnorm at right with dissolve
    elif poprock == True:
        scene aphmau_coffee_cg_1 with fade
        stop music
        play music daydream loop
        pause (2.0)
        play sound wow
        a "Aaa~! Soo delicious!!"
        mc "Truly!! This is awesome!"
        scene aphmau_coffee_cg_2 with dissolve
        a "So glad you love it! It's the greatest drink ever, right??"
        mc "It's definitely up there!"
        mc "Thanks for recommending this, Aphmau!"
        kc "[mcname]-san would've liked the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice more..."
        mc "Don't worry, Kawaii-chan, i'll try it next time i'm here!"
        scene coffeeshop with fade
        stop music
        play music daysong2 loop
        show aphnorm at left with dissolve
        show kcnorm at right with dissolve
    elif thirdthing == True:
        hide tylercoffee with dissolve
        show aphnorm at left with dissolve
        show kcnorm at right with dissolve
        mc "Hey, this Special is actually quite good, I like it"
        a "I've never had it before, actually"
        kc "Kawaii-chan still thinks the Mega-Ultra-Caramel-Crunchy-Crater-Chaos-Chalice is the best!"
        mc "Haha!"    
    mc "Man, this has been great, you guys weren't kidding when you said this place was awesome!"
    kc "We should come here again in the future!"
    mc "I'd love to! I'm just..so glad i've made some good friends here.."
    mc "Seriously, thank you Kawaii-chan, thank you Aphmau"
    play sound aphperf
    a "Hey, call me Aph!"
    mc "Really? Are you sure?"
    a "Of course, silly! We're friends now, friends give eachother nicknames!"
    hide kcnorm
    show kcstar at right  
    kc "Ooo! We should have a nickname for [mcname]-san too!"
    a "Ooo, yess!! What should we call you?"
    $ nick = renpy.input("What should we call you?")
    a "That's cute! I like it! [nick]. That's what we'll call you!"
    kc "Kawaii-chan really likes it!"
    mc "Haha. I guess that's been established!"
    kc "Kawaii-chan's finished her coffee!"
    a "I finished mine too!"
    mc "Me too, now what?"
    hide aphnorm
    show aphsad at left
    a "Aww, I don't want this to end already!"
    kc "We don't need coffee to hang out, why don't we all go on a walk!"
    hide aphsad 
    show aphnorm at left
    mc "You're right! I'd love to walk around for a bit!"
    scene citynoon with fade
    show aphconf at left with dissolve
    show kcnorm at right with dissolve
    a "Woah! The sun's already setting!"
    mc "You know what they say, time flies by when we're having fun!"
    play sound kclaugh
    kc "Kawaii-chan is having such a blast hanging out with you guys!"
    mc "Me too!"
    scene black with fade
    "We hung out for a while longer.."
    scene citynight with fade
    show aphnorm at left with dissolve
    show kcnorm at right with dissolve
    play sound aphlaugh
    a "Hahah!! You're so funny, [nick]!"
    kc "It's getting late, Kawaii-chan's a bit tired..."
    mc "Yeah...it might be a good idea to call it a night.."
    a "Let's all head home!"
    scene housenight with fade
    stop music
    play music nightsong loop
    show aphnorm at left with dissolve
    show kcnorm at right with dissolve
    kc "We had lot's of fun [nick]-san!"
    a "You should definitely call us if you ever wanna hang out again!"
    mc "Definitely! I'll see you guys later, goodnight!"
    if tylermean == 4:
        jump tylersecretend1
    else:
        jump dayend
label lucikatbowl:
    scene bowlingoutside with fade
    "They should be around here somewhere.."
    lu "[mcname]! Over here!"
    show lucinorm at right with dissolve
    show katnorm at left with dissolve
    lu "Glad you could make it!"
    k "You're about to see two bowling experts go head to head!"
    hide katnorm
    show katsmile at left
    k "One of us is definitely better than the other, of course"
    hide lucinorm
    show lucismirk at right
    lu "That's me, right?"
    k "I guess we'll find out~"
    "There's some tension between two..but I can't tell what kind...."
    lu "Come on, let's go inside"
    scene bowlinginside with fade
    show katnorm at right with dissolve
    show lucinorm at left with dissolve
    k "We're gonna have to get two pairs of bowling shoes"
    mc "I don't suppose I can bowl too, can I..?"
    hide lucinorm
    show lucisad at left
    play sound luciohright
    lu "Ah..well..you see, it's like....a preorder...you get it?"
    mc "Right..."
    k "You can join us next time! Promise"
    mc "I'm fine with that"
    show tylerbowl with dissolve
    ty "Hey guys welcome to the Super-Duper X-treme Bowling Palooza, you guys need shoes?"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.." 
    k "[mcname]? You know this guy?"
    mc "I- no...sorry...you guys just get your shoes..."
    lu "Right...we'd like two Adult Women shoes, size 8, please"
    ty "Only 2? None for your friend here?"
    mc "Oh, i'm not playing ahaha"
    ty "Yea I bet you'd suck at bowling anyway"
    ty "Anyway here are your shoes"
    k "Hey [mcname], you can go grab some food if you want"
    mc "I think i'll do that later"
    lu "Alright, let's go to our lane then!"
    hide lucisad with dissolve
    hide katnorm with dissolve
    ty "[mcname]- stay back..."
    mc "Wsg gang"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    k "[mcname]? You coming?"
    mc "Give me a sec, Katelyn!"
    menu:
        "I don't need your help":
            $ tylermean +=1 
            mc "Listen, Tyler, I don't need your help. Quite frankly, you're freaking me out, so just leave me alone, okay?"
            if tylermean == 4:
                ty "...."
                ty "if that's what you wish for...Tyler will comply..."
                mc "Ohkay. You know what I- goodbye"
            else:
                ty "You don't get it, man! You need this! You need me!"
                mc "Whatever you say man"
        "Thanks for your help":
            mc "Thanks for the help, even if i'm not sure what you're talking about, i'll keep your advice in mind"
            ty "Good...now go get em tiger!"
            mc "Don't ever call me that ever again"
    scene bowlinglane with fade
    show lucievil at left with dissolve
    play sound lucigotthis
    lu "Alright Katelyn, you ready to get your shit rocked?"
    show katdis at right with dissolve
    k "If it helps you sleep at night, sure"
    lu "[mcname], who are you gonna cheer for?"
    menu:
        "Support Lucinda":
            $ luciwin = True
            $ katwin = False
            $ luciflag += 1
            mc "I think Lucinda's gonna win, so Go Lucinda!!!"
            $ renpy.notify("Lucinda appreciates your support!")
            hide lucievil
            show lucismirk at left
            lu "Haha! Thanks so much~!"
            lu "With [mcname] cheering me on, i'm sure to win~"
            k "Yeah yeah, whatever..."
        "Support Katelyn":
            $ katwin = True
            $ luciwin = False
            $ katflag += 1
            mc "I think Katelyn's gonna win, so Go Katelyn!!!"
            $ renpy.notify("Katelyn appreciates your support!")
            hide katdis
            show katsmile at right
            k "Hell yea! See, Lucinda? Even [mcname] thinks i'll win!"
            hide lucievil
            show lucisad at left
            lu "Aww..whatever.."
    stop music
    play music shitgetsserious loop
    k "Let's bowl!!"
    scene bowling_cg with fade
    lu "HYAH!!" with hpunch
    k "WOAH!!" with vpunch
    "Man...these guys are really serious when it comes to bowling..."
    if luciwin == True:
        mc "GO LUCINDA!! YOU GOT THIS!!"
        lu "Haha! Thanks!!"
    else:
        mc "GO KATELYN!! YOU GOT THIS!!"
        k "You know it!!"
    "People are starting to gather around..this is serious!"
    "Annd the winner iis...."
    if luciwin == True:
        scene lucinda_bowling_cg_1 with fade
        pause (2.0)
        lu "HAHAA! I WONN!"
        mc "WOOHOOOO!!"
        play sound katgrr
        k "ARGH! I'll get you next time!!"
        scene lucinda_bowling_cg_2 with dissolve
        lu "Haha, I couldn't have done it without the support from [mcname]~"
        mc "Oh come on, I didn't do anything..."
        lu "No no! It was with your cheering that I was able to win!"
        mc "Well, if you say so..."
        scene bowlinglane with fade
        show lucinorm with dissolve
        lu "Ah, how exhilarating~"
        show katsmile at left with dissolve
        k "I have to give credit where it's due, that was some great gameplay, Luci."
        hide lucinorm
        show lucismirk
        lu "So I guess it's settled? I'm the better bowler?"
        k "Hmmm, I don't know...we might have to revisit this in the future."
        play sound lucilaugh
        lu "Haha, you never change, Katelyn~"
    else:
        scene katelyn_bowling_cg_1 with fade
        pause (2.0)
        play sound katlaugh
        k "YEEEESSSSS!!! SUCK ITT!!!!"
        mc "WOOHOOOO!!!"
        play sound lucisigh
        lu "Oh, bummer.."
        scene katelyn_bowling_cg_2 with dissolve
        k "Thanks for the help, [mcname]! Couldn't have done it without you!"
        mc "What? That's not true"
        k "It is! I needed you to cheer me to victory!"
        mc "Well, in that case, no problem!"
        scene bowlinglane with fade
        show katsmile with dissolve
        k "Man, that was fun!"
        show lucismirk at left with dissolve
        lu "Wow, Katelyn, what a performance!"
        lu "I suppose you won this fair and square."
        hide katsmile
        show katlaugh
        k "Then you finally admit it? I'm the better bowler?"
        lu "Hmm, let's not get ahead of ourselves now.."
        k "Hah! So stubborn!"
    stop music
    play music daysong2 loop
    mc "Now that that's settled... who's hungry???"
    b "WOOOO!!"
    scene bowlfoodcourt with fade
    show lucinorm at left with dissolve
    lu "[mcname], the chilli fries here are SUPERB! You need to try them!"
    show katnorm at right with dissolve
    k "She's lying, [mcname], the Bowler-Burger is the best, you should get that"
    mc "Hmm...I don't know..."
    show tylerbowl with dissolve
    ty "Welcome to the Super-Duper X-treme Bowling Palooza Food Court, what can I get ya"
    mc "Oh you work here too"
    ty "economy's fucked"
    mc "Preeach"
    lu "I'd like the Chilli fries, please"
    k "I'll take the Bowler-Burger"
    ty "What do you want"
    menu:
        "Chilli fries":
            $ luciflag += 1
            $ renpy.notify("Lucinda's glad you took her suggestion!")
            mc "I think I'll have the Chilli fries, please!"
            ty "You think? Or you will?"
            mc "...I will."
            ty "That's what I thought"
        "Bowler-Burger":
            $ katflag += 1
            $ renpy.notify("Katelyn's glad you took her suggestion!")
            mc "I think I'll have the Bowler-Burger, please!"
            ty "You think? Or you will?"
            mc "...I will."
            ty "That's what I thought"
        "A secret third thing":
            mc "Um...I'll get something else.."
            ty "Right, one Make-A-Choice Xtremity for you"
            mc "What? I didn't even order-"
            "It's what we give to our particularly non-decisive customers"
            menu:
                "Fuck you bitch":
                    $ tylermean += 1
                    mc "Okay wow fuck you bitch damn"
                    ty "HEY I can call security on you"
                    mc "Whatever"
                "Thanks":
                    mc "Thanks..."
                    ty "No problem man it's actually a special i've been working on for a while"
                    mc "Right yeah don't care"
    k "Let's feast!"
    scene black with fade
    "We ate our food and conversed for a while..."
    show bowlfoodcourt with fade
    show lucinorm at left with dissolve
    lu "Man! I'm stuffed!"
    show katnorm at right with dissolve
    k "Soooo true"
    mc "Man, today's been a lot of fun! I'm glad I got to hang out with you guys!"
    hide lucinorm
    show lucismirk at left
    lu "I'm glad too, you're really fun to talk to, [mcname]. We should hang more often"
    k "Well obviously [mcname] would rather hang out with me, right?"
    hide lucismirk 
    show lucievil at left
    lu "Wanna bet on that?"
    hide katnorm
    show katdis at right
    k "Bring it."
    mc "Oorrr I can hang out with both of you guys! We don't have to kill eachother!"
    k "For now..."
    mc "Right let's just go home"
    scene housenight with fade
    stop music
    play music nightsong loop
    show lucinorm at right with dissolve
    show katnorm at left with dissolve
    k "Hopefully we can do something like this again"
    lu "Even if its one-on-one~"
    k "Shut the fuck up omg"
    mc "Ahaha i'd love to. I'll see you guys later! Goodnight!"
    if tylermean == 4:
        jump tylersecretend1
    else:
        jump dayend
label laurpizza:
    scene pipinghotpizza with fade
    "This should be the place! I wonder where Laurance is..."
    la "[mcname]! Over here!"
    show laursmile with dissolve
    la "It's great to see you! You're looking good today"
    mc "Thanks, Laurance!"
    la "Let's head on in, shall we?"
    scene pipinghotpizzainside with fade
    stop music 
    play music romance loop
    show laurnorm with dissolve
    play sound wow
    mc "Ohh woow! It smells so good in here!"
    play sound laurexactly
    la "Right? Trust me, the pizzas taste just as great, if not better!"
    la "Here, let's sit down"
    show laurnorm at left with easeinleft
    show tylerwaiter with dissolve
    ty "Hey guys welcome to Piping Hot Pizza Palace. What can I toss in the oven for ya"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.."
    hide laurnorm
    show laurdis at left
    la "Are you two...familiar?"
    mc "I- no...sorry...let's just order..."
    la "Right, I think we're gonna need some time first"
    ty "k"
    hide tylerwaiter with dissolve
    show laurdis at center with ease
    hide laurdis
    show laurnorm
    la "Hmm, any idea what you want?"
    mc "Well, what do you recommend?"
    hide laurnorm
    show laursmile
    la "Oo! They have this really good Everything Pizza. It's got a bunch of different topings, and each slice uses a different type of sauce and cheese. It sounds chaotic, but it's soo good!"
    menu:
        "Sounds Good!":
            $ laurflag += 1
            $ everythingpizza = True
            mc "That sounds good! Let's get it!"
            $ renpy.notify("Laurance is glad you took his suggestion!")
            la "Haha! I knew you'd like it!"
            mc "You think we can get some breadsticks on the side?"
            play sound laurwhynot
            la "Sure! Why not?"
            show laursmile at left with easeinleft
        "Sounds Awful!":
            $ everythingpizza = False
            mc "That sounds awful actually"
            hide laursmile
            show laurshock
            la "Well- no- it's actually-"
            mc "No let's just get cheese pizza"
            hide laurshock
            show laursad
            la "Uh..sure...if that's what you want..."
            show laursad at left with easeinleft
    show tylerwaiter with dissolve
    ty "You guys finally ready to order?"
    if everythingpizza == True:
        mc "Yup! We'll have the Everything Pizza, please!"
        ty "Mm, would you like a side of bitch with that?"
        mc "Excuse me!?"
        ty "You heard me"
        menu:
            "Fuck you bitch":
                $ tylermean += 1
                mc "Man fuck you bitch!"
                ty "HEYY HOSTILITY!! I can call security on you for that!!"
                mc "Whatever.."
                hide laursmile
                show laurnorm at left
                la "For real though can we get some breadsticks on the side"
                ty "Anything for you Laurance"
                la "What"
            "Breadsticks":
                mc "Actually I'd like that with a side of breadsticks, please"
                ty "Okay"
    else:
        mc "Yup! We'll have the Cheese Pizza, please!"
        ty "Mm, would you like a side of bitch with that?"
        mc "Excuse me!?"
        ty "You heard me"
        menu:
            "Fuck you bitch":
                $ tylermean += 1
                mc "Man fuck you bitch!"
                ty "HEYY HOSTILITY!! I can call security on you for that!!"
                mc "Whatever.."
                hide laursad
                show laurnorm at left
                la "For real though can we get some breadsticks on the side"
                ty "Anything for you Laurance"
                la "What"
            "Breadsticks":
                mc "Actually I'd like that with a side of breadsticks, please"
                ty "Okay"
    ty "[mcname], I need you to come with me."
    mc "What?"
    ty "JUST COME"
    mc "Oh, um, Laurance, I'll be right back.."
    hide laurnorm
    hide laursmile
    hide laursad
    show laurdis at left
    play sound lauruhh
    la "Uh huh..."
    scene pizzakitchen with fade
    show tylerwaiter with dissolve
    mc "Is this the pizza kitchen? Am I even allowed in here?"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    menu:
        "I don't need your help":
            $ tylermean +=1 
            mc "Listen, Tyler, I don't need your help. Quite frankly, you're freaking me out, so just leave me alone, okay?"
            if tylermean == 4:
                ty "...."
                ty "if that's what you wish for...Tyler will comply..."
                mc "Ohkay. You know what I- goodbye"
            else:
                ty "You don't get it, man! You need this! You need me!"
                mc "Whatever you say man"
        "Thanks for your help":
            mc "Thanks for the help, even if i'm not sure what you're talking about, i'll keep your advice in mind"
            ty "Good...now go get em tiger!"
            mc "Don't ever call me that ever again"
    scene pipinghotpizzainside with fade
    show laurdis with dissolve
    play sound laurokay
    la "What's up? Everything alright?"
    mc "Yeah, no, don't worry about it, he was just...showing us our pizza....it's coming soon"
    la "Uh huh..."
    hide laurdis
    show laursmile
    la "So, while we wait, let's talk about something!"
    menu:
        "What are your hobbies?":
            mc "Do you have any hobbies? Interests?"
            la "Let's see...I used to play soccer a lot back in highschool, me and the others still play occassionally on weekends."
            la "Oh! I do a lot of cooking! Not to toot my own horn, but if you were to ask anyone, they'd agree that i'm kind of a master cook."
            mc "Haha! I'd love to try some of your food one day!"
            hide laursmile
            show laurnorm
            la "What about you? What are you into?"
            menu:
                "Music":
                    $ laurflag += 1
                    mc "I'm pretty into music!"
                    $ renpy.notify("You two have a common interest!")
                    hide laurnorm
                    show laursmile
                    la "Hey, me too! Do you play?"
                    mc "Ah, not really, I just like listening to tons of different stuff, you know?"
                    la "I get that, I play the guitar sometimes, but I also just like listening to stuff. Have you heard of Trans Siberian Orchestra? They're my favourite band!"
                    mc "I'll have to give them a listen!"
                    show laursmile at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursmile at center with ease
                "Film":
                    $ laurflag += 1
                    mc "I'm pretty into film!"
                    $ renpy.notify("You two have a common interest!")
                    hide laurnorm
                    show laursmile
                    la "Hey, me too! I love watching movies!"
                    la "I guess everyone does, but I don't know, I reallyy just love film."
                    mc "I get what you mean! I just love being able to appreciate different genres"
                    la "Haha, it's nice to meet a fellow film enthusiast, we should definitely watch some movies together! You can show me your favourites, and I can show you mine"
                    mc "That sounds fun! I'd love to" 
                    show laursmile at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursmile at center with ease
                "Video Games":
                    mc "I like playing video games!"
                    la "Ohh, that's cool. I don't really play video games, sometimes with the guys or Aphmau, but that's really it."
                    la "You should play with Aphmau or Aaron sometime! They're both awesome at anything they get their hands on"
                    mc "I'll have to do that..."
                    show laurnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laurnorm at center with ease
                "Art":
                    mc "I'm pretty into art! I like to draw a lot"
                    la "That's cool! I'm not too into art. People have said that i'm pretty good, but i've never had a huge interest in it."
                    la "Hey, you should see some of Kawaii-chans art though! She's a wizard with a pencil. She could honestly go professional if she wanted to!"
                    mc "I'll have to do that..."
                    show laurnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laurnorm at center with ease
                "I hate everything in this awful world":
                    mc "This world is garbage and theres nothing about it that I enjoy"
                    hide laurnorm
                    show laursad
                    la "Oh...that's..a shame..."
                    la "Have you been talking to Zane lately? That sounds like something he'd say..."
                    show laursad at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursad at center with ease
        "What do you think of the other residents?":
            mc "What do you think of the other people in our neighbourhood?"
            la "Well, we're all really good friends! I've known pretty much everyone since high school."
            la "We've all supported eachother through our hardships, i'm glad to have them all in my life"
            la "I would say i'm closest with Garroth. He's my bestest friend in the entire world, I don't know what I'd do without him!"
            la "What about you, what do you think of everyone?"
            menu:
                "I like them all":
                    $ laurflag += 1
                    mc "I know we haven't talked much, but I really like everyone! They all seem so fun and unique, it's refreshing to have such a vibrant friendgroup"
                    $ renpy.notify("Laurance finds you admirable!")
                    la "Wow, you've only been here for a couple days and you already like them! You're right though, they are great"
                    la "I like people who are able to get along quickly! They're always the most fun to be around."
                    mc "Then I guess you'll be having lots of fun with me~"
                    play sound laurlaugh
                    la "Haha, we'll see."
                    show laursmile at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursmile at center with ease    
                "I have no opinion":
                    mc "Hmm...I don't really have any strong opinions. I haven't really talked to anyone that much"
                    hide laursmile
                    show laurnorm
                    la "Yeah..that makes sense. I don't know why I asked, ahah."
                    la "Trust me, though, you're gonna love everyone here"
                    la "...besides Dante, he's kinda weird. And Travis, they're both...yeah..."
                    la "And Zane can be pretty mean sometimes, Katelyn too, and Aaron can be a bit off-putting.."
                    la "And I guess Kawaii-chan can be a bit much sometimes, Garroth too, oh, and be careful of Lucinda! She's kind of a trickster, and-"
                    mc "You know what? I'll just form my own opinion as time goes on"
                    la "That makes sense.."
                    show laurnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laurnorm at center with ease
                "I hate them all":
                    mc "I honestly really don't like anyone here. They're kind of annoying..."
                    hide laursmile
                    show laursad
                    la "Oh....that's....uh.."
                    la "I hope you get to know them better, I guess..."
                    show laursad at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursad at center with ease
        "Are you looking for love?":
            mc "Are you looking for love? Or wait, do you already have someone??"
            hide laursmile
            show laurshock
            play sound lauruhh
            la "Oh! Um...no...or- no, I don't have a partner right now.."
            la "But...I guess i'm looking for love? I don't know, I haven't really been thinking about it.."
            mc "Sorry, that was kind of a personal question.."
            la "No, it's fine. What about you? Are you looking for anyone?"
            menu:
                "Yes":
                    $ laurflag += 1
                    mc "I am! I would like to find somebody"
                    $ renpy.notify("Laurance is glad he has a chance with you!")
                    hide laurshock
                    show laursmile
                    la "Cool! I guess we're both on the search...haha.."
                    mc "Haha looks like you could help me with my OPERATION to find a SWEETHEART"
                    hide laursmile
                    show laurdis
                    la "...what?"
                    mc "Nothing"
                    show laurdis at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laurdis at center with ease
                "No":
                    mc "Not really, honestly. Just wanting to go solo for now"
                    hide laurshock
                    show laursad
                    la "Oh...that's..cool, I guess..."
                    "Am I lying to him or myself right now"
                    show laursad at left with easeinleft
                    show tylerwaiter with dissolve
                    if everythingpizza == True:
                        ty "Here's your Everything Pizza. Bone apple teeth"
                    else:
                        ty "Here's your cheese pizza. Bone apple teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    hide tylerwaiter
                    show laursad at center with ease
    hide laursad
    hide laursmile
    hide laurdis
    show laurnorm
    if everythingpizza == True:
        mc "Woah...this looks awesome..."
        play sound laurexactly
        la "Right? Let's dig in."
        scene laur_pizza_cg_1 with fade
        pause (2.0)
        play sound wow
        la "Deliiciooussss~~...."
        mc "I can't believe it...I didn't know pizza could be this good...."
        scene laur_pizza_cg_2 with dissolve
        la "I told you it'd be good!"
        la "This place truly is the best..."
        mc "Haha, i'm glad I chose to come here with you!"
        la "You made the right decision!"
        scene pipinghotpizzainside with fade
        show laursmile with dissolve
    else:
        mc "This looks good!"
        la "It does! But it's just cheese pizza..."
        la "The Everything Pizza, however..."
        mc "We can get that next time!"
        hide laurnorm
        show laurshock
        la "Is there...a next time?"
        mc "If you want to, I'd like to do this again!"
        hide laurshock
        show laursmile
        la "I would really like that!"
    la "I'm glad that you like the food here. You agree with me now, right? This is the best restaurant around here?"
    mc "Well, I still have to try the others...but this is definitely winning so far!"
    play sound laurlaugh
    la "Knew it! I-"
    hide laursmile
    show laurshock
    la "Uh- [mcname]- Don't look behind you?"
    mc "What? What's behind me?"
    la "It's uh- No they're coming here."
    show garsad at left with easeinbottom
    show aarsad at right with easeinbottom
    play sound garaww
    g "We didn't think we'd get caught..."
    mc "What the- Garroth?? Aaron?? What are you guys doing here??"
    ar "We...wanted to see how this was going.."
    mc "What? Why?"
    hide garsad
    show garmad at left
    g "BECAUSE PIPING HOT PIZZA PALACE ISN'T THE BEST RESTAURANT!! IT'S CLOUD 9 NICE ICE CREAM PARLOUR!!!!"
    mc "Jesus fucking christ"
    mc "Aaron, you don't even like the ice cream place, why are you with Garroth?"
    ar "An enemy of my enemy is my friend"
    mc "Got it"
    hide laurshock
    show laursad
    la "Can you guys leave us alone?? We're just trying to have a nice dinner.."
    g "If you want a nice dinner, then you go to Cloud 9 Nice Ice Cream Parlour!"
    ar "Who has ice cream for dinner?"
    hide garmad
    show garshock at left
    g "..you guys haven't had ice cream for dinner?"
    la "Okay just get out of here!!"
    g "SORRY! Sorry!"
    ar "[mcname], have a great rest of your night!!"
    mc "You too..."
    hide garshock with easeoutbottom
    hide aarsad with easeoutbottom
    la "I'm sorry about that..."
    mc "It's okay, ahaha. Let's just finish our pizza."
    scene black with fade
    "We finished our dinner..."
    show housenight with fade
    stop music
    play music nightsong loop
    show laursmile with dissolve
    la "I hope you had a great time, [mcname]"
    hide laursmile
    show laursad
    la "Even though Garroth and Aaron kinda ruined it at the end..."
    mc "Haha, it wasn't ruined. I had a lot of fun today, Laurance"
    hide laursad
    show laursmile
    la "That's great to hear! I had fun too."
    mc "I'll see you around! Good night!"
    la "Night!"
    if tylermean == 4:
        jump tylersecretend1
    else:
        jump dayend
label aarsausage: 
    scene sizzlingsausageshack with fade
    mc "Aaron should be out here somewhere..."
    ar "[mcname]! Hey!"
    show aarsmile with dissolve
    ar "Did you just get here?"
    mc "Mhm! I hope I didn't keep you waiting?"
    ar "No no, you're good. Let's go inside"
    scene sizzlingsausageshackinside with fade
    stop music
    play music romance loop
    play sound wow 
    mc "Woww! This place smells so good!"
    show aarnorm with dissolve
    ar "One of my favourite things about this place."
    ar "Come on, let's sit down"
    show aarnorm at left with easeinleft
    show tylerwaiter with dissolve
    ty "Hey guys welcome to Piping Hot Pizza Palace. What can I toss in the oven for ya"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.."
    ar "Wait a minute, you two have met before?"
    mc "I- no...sorry...let's just order..."
    ar "Okay...sorry, could we have a couple minutes before we order?"
    ty "k"
    hide tylerwaiter with dissolve
    show aarnorm at center with ease
    ar "Have you gotten a chance to look over the menu?"
    mc "I did...I'm still not sure what I want, do you have any suggestions?"
    hide aarnorm
    show aarsmile
    ar "I do, actually! So, there's this special they have-"
    ar "Imagine a hot dog...."
    ar "Imagine a hot dog.... but circular."
    mc "What?"
    ar "It's like..super long, and bent into a circle, but it's connected seamlessly! I don't know how they make it, but it's so cool!"
    ar "And they put some cheese and nachos on top, they call it their Gourmet Donut"
    mc "How would you even eat that"
    ar "Like a donut!"
    mc "no..but with a hot dog, when you bit it at the end, you get an appropriate ratio of bread and dog, but if you eat it from the side like a donut....it just doesn't work"
    ar "Trust me. Don't knock it 'till you try it."
    menu:
        "Let's get it":
            $ sausagedonut = True
            $ aarflag += 1
            mc "That sounds interesting, now I have to try it!"
            $ renpy.notify("Aaron is glad you took his suggestion!")
            ar "Great! I can't wait to see what you think of it."
            show aarsmile at left with easeinleft
        "Let's not":
            $ sausagedonut = False
            mc "Doesn't sound too appealing...I'll just get a normal hot dog"
            hide aarsmile
            show aarsad
            ar "Oh..I thought you'd like it a lot..."
            show aarsad at left with easeinleft
    show tylerwaiter with dissolve
    ty "You guys finally ready to order?"
    if sausagedonut == True:
        mc "Yup! We'll both have the Gourmet Donut!"
        ty "Oh I hate that one actually"
        mc "Really?"
        ty "Yeah it's fucking impossible to cook but it's all anyone ever orders"
        mc "Wait, are you the chef here too??"
        ty "..."
        hide tylerwaiter with dissolve
        show aarsmile at center with ease
    else:
        aar "I'll have the Gourmet Donut.."
        mc "And I'll just take a normal hot dog"
        ty "Good choice, the Gourmet Donut sucks"
        hide aarsad
        show aarmad at left 
        ar "Dude?"
        mc "Are you even allowed to say that about your own food"
        ty "Yeah cuz it fucking sucks and is so hard to cook but everyone and their mom orders it and I hate it"
        mc "Wait, are you the chef here too??"
        ty "..."
        hide tylerwaiter with dissolve
        show aarmad at center with ease
    hide aarmad
    hide aarsmile
    show aarnorm
    ar "Anyway, I-"
    show tylerwaiter at right with easeinright
    ty "I almost forgot, [mcname] I need you to come with me"
    mc "What"
    ty "Trust me. Just come"
    mc "Right...i'll be back, Aaron.."
    ar "Have fun..?"
    scene pizzakitchen with fade
    show tylerwaiter with dissolve
    mc "Is this the kitchen? Am I even allowed in here?"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    menu:
        "I don't need your help":
            $ tylermean +=1 
            mc "Listen, Tyler, I don't need your help. Quite frankly, you're freaking me out, so just leave me alone, okay?"
            ty "You don't get it, man! You need this! You need me!"
            mc "Whatever you say man"
        "Thanks for your help":
            mc "Thanks for the help, even if i'm not sure what you're talking about, i'll keep your advice in mind"
            ty "Good...now go get em tiger!"
            mc "Don't ever call me that ever again"
    scene sizzlingsausageshackinside with fade
    show aarnorm with dissolve
    ar "Everything alright?"
    mc "Yup! Sorry, he just...don't worry about it"
    ar "Before you left, I was gonna say..let's talk a bit about ourselves and learn about eachother! Y'know, while we wait for our food"
    mc "Sounds good!"
    ar "So..what do you wanna talk about?"
    menu:
        "What are your hobbies?":
            mc "Do you have any hobbies? Interests?"
            ar "I really like video games. I play a lot with the guys, but mainly with Aphmau."
            ar "I've also been playing the guitar recently! I'm still not too good, though. And I'm pretty into manga.."
            ar "How about you? What are you into?"
            menu:
                "Sports":
                    mc "I'm pretty into sports!"
                    ar "That's cool! I like playing sports too sometimes. We all like to get together and play soccer sometimes."
                    ar "You know, Katelyn's probably the most athletic out of all of us, you guys should get together sometime!"
                    mc "I'll do that..."
                    show aarnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "Film":
                    mc "I'm pretty into film!"
                    ar "Oh, that's pretty cool!"
                    ar "I'm not super into movies...I mean, I watch them, obviously, but other than that-"
                    mc "You know, I think Laurence is the movie guy out of all of us. You should hang with him more!"
                    mc "Right..." 
                    show aarnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "Video Games":
                    $ aarflag += 1
                    mc "I like video games!"
                    $ renpy.notify("You and Aaron have a common interest!")
                    hide aarnorm
                    show aarsmile
                    ar "Awesome! I love video games too! I play a lot of Final Fantasy, but I enjoy pretty much everything"
                    mc "We should definitely play together sometime!"
                    play sound aarsure
                    ar "That sounds great!"
                    show aarsmile at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile 
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "Reading":
                    $ aarflag +=1
                    mc "I'm pretty into reading! Especially manga."
                    $ renpy.notify("You and Aaron have a common interest!")
                    hide aarnorm
                    show aarsmile
                    ar "Ahh, cool! I like manga too!"
                    ar "I've always preferred it over anime, not sure why"
                    ar "I could show you some of my favourites and you could show me yours!"
                    mc "I'd love that!"
                    show aarsmile at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "I hate everything in this awful world":
                    mc "This world is garbage and theres nothing about it that I enjoy"
                    hide aarnorm
                    show aarsad
                    ar "Oh...uh....I'm not too sure what to say about that..."
                    ar "Maybe you should hang out with Zane more often, you guys sound similar..."
                    show aarsad at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarsad at center with ease
                            hide aarsad
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarsad at center with ease
                            hide aarsad
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
        "What do you think of the other residents?":
            mc "What do you think of the other people in our neighbourhood?"
            ar "Ah, well, we're all great friends. I've known them all for a while now"
            hide aarnorm
            show aarsad
            ar "Although, it took a while for us to get along.."
            mc "Really? How come?"
            ar "Just, uhh...drama.."
            hide aarsad
            show aarnorm
            ar "I've always been good friends with Aphmau, though. We're great friends. She's probably the one im closest with. I'm also pretty close with Dante"
            mc "Really? Dante? I didn't expect that."
            ar "Haha, I know, we seem different, but I don't know...something about Dante draws me into him."
            ar "Uhh..what about you? What do you think of everyone?"
            menu:
                "I like them all":
                    $ aarflag += 1
                    mc "I know we haven't talked much, but I really like everyone! They all seem so fun and unique, it's refreshing to have such a vibrant friendgroup"
                    $ renpy.notify("Aaron finds you admirable!")
                    hide aarnorm
                    show aarsmile
                    ar "That's great! I'm glad you're getting along with everyone!"
                    ar "I can tell everyone already really likes you too, it's kinda incredible.."
                    mc "Really? You can tell?"
                    play sound aarlaugh
                    ar "Yeah! Dante was telling me he thought you were really cool. I have to agree wit him, you are pretty awesome"
                    mc "Ohhh...stawp it..."
                    play sound aartease
                    ar "Haha, I'm just teasing"
                    show aarsmile at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "I have no opinion":
                    mc "Hmm...I don't really have any strong opinions. I haven't really talked to anyone that much"
                    ar "Oh yeah, you're right, I guess it'll take some time before you really get settled in with everyone"
                    show aarnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "I hate them all":
                    mc "I honestly really don't like anyone here. They're kind of annoying..."
                    hide aarnorm
                    show aarmad
                    ar "....alright"
                    show aarmad at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarmad at center with ease
                            hide aarmad
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarmad at center with ease
                            hide aarmad
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
        "Are you looking for love?":
            mc "Are you looking for love? Or wait, do you already have someone??"
            hide aarnorm
            show aarshock
            ar "d-do you think I have someone?"
            mc "I mean...I don't know...that's why i'm asking"
            ar "No, I don't have anyone...and I don't know if i'm actively looking, I guess I'm just waiting to meet the right person"
            hide aarshock
            show aarnorm
            ar "What about you?"
            menu:
                "Yes":
                    $ aarflag += 1
                    mc "I am! I would like to find somebody"
                    $ renpy.notify("Aaron is glad he has a chance with you!")
                    hide aarnorm
                    show aarsmile
                    ar "I'm sure someone like you is able to have anyone they wanted"
                    mc "W-what!?"
                    play sound aartease
                    ar "Haha, too much..?"
                    show aarsmile at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarsmile at center with ease
                            hide aarsmile
                            show aarnorm
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
                "No":
                    mc "Not really, honestly. Just wanting to go solo for now"
                    ar "Hmm....I can respect that. Independence can be good"
                    show aarnorm at left with easeinleft
                    show tylerwaiter with dissolve
                    ty "here are your dogs. Bone Apple Teeth"
                    mc "Don't you mean...Bon Apetit?"
                    ty "I'm not fucking perfect Okay!!!!"
                    menu:
                        "You a bitch":
                            mc "YOU A BITCH!"
                            $ tylermean += 1
                            ty "WHAT'S WRONG WITH YOU"
                            mc "WHAT'S WRONG WITH YOU??? YOU SHOULD BE FIRED RIGHT NOW"
                            if tylermean == 4:
                                ty "You're gonna fucking regret this mark my words"
                            else:
                                ty "YOU'RE SO MEAN I HATE YOU"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            mc "I hate that guy so much...."
                            ar "Uh huh..."
                        "It's okay":
                            mc "It's okay. We all make mistakes"
                            ty "Really..? You understand...?"
                            mc "Yea man this job is hard"
                            ty "Thanks so much...you know, it's really tough out here..in the waitressing business...I-"
                            mc "Yeah yeah thats great let's talk about this later"
                            hide tylerwaiter with dissolve
                            show aarnorm at center with ease
                            ar "He's a weird one, isn't he?"
                            mc "Yeah..."
    ar "Hey, at least our food is here! Let's dig in!"
    scene aaron_sausage_cg_1 with fade
    pause (2.0)
    play sound wow
    ar "It's too good!"
    if sausagedonut == True:
        mc "It's...so good......"
        ar "I told you!"
    else:
        ar "I wish you gave it a try.."
        mc "It does look pretty good..."
    scene aaron_sausage_cg_2 with dissolve
    ar "Nothing like a good Gourmet Donut. Seriously, this is probably the best thing i've ever ate in my life."
    mc "Better than my pasta?"
    play sound aarlaugh
    ar "Maybe if your pasta was circular!"
    scene sizzlingsausageshackinside with fade
    show aarsmile with dissolve
    ar "So? What do you think?"
    mc "I'll admit...this place is pretty awesome..."
    ar "Told you! I'm glad you agreed to come here with me, or else you wouldn't know about the greatness that is...the Sizzling Sausage Shack..."
    mc "I'm sure this place blows those other restaurants out of the water!"
    ar "Oh, most definitely!"
    mc "Speaking of, I wonder what Laurance and Garroth are up to right now..."
    hide aarsmile
    show aarshock
    ar "Uhhh....I think I might have a pretty good idea..."
    mc "Hm? What do you mean?"
    ar "Well-"
    show garmad at left with easeinbottom
    show laurdis at right with easeinbottom
    g "STOP RIGHT THERE! YOU'RE INDOCTRINATING THEM!"
    mc "OH MY GOD! Laurance? Garroth?? What're you guys doing here??"
    g "We had to make sure Aaron wasn't succeeding with his propaganda!"
    hide aarshock
    show aarmad
    ar "What...are you talking about..."
    g "THE SIZZLING SAUSAGE SHACK ISN'T THE BEST RESTAURANT!! IT'S CLOUD 9 NICE ICE CREAM PARLOUR!!!!"
    mc "Jesus fucking christ"
    mc "Laurance, you don't even like the ice cream place, why are you with Garroth?"
    la "Didn't have anything else to do. Also I don't like Aaron"
    ar "What?"
    la "Nothing"
    ar "Seriously, can you guys leave us alone..."
    la "Come on, Garroth, let's go do something else"
    hide garmad
    show garsad at left
    g "Like...like what..."
    la "Let's go get some ice cream...my treat..."
    g "Okayy...."
    g "Goodnight, Aaron and [mcname]..."
    hide garsad with easeoutbottom
    hide laurdis with easeoutbottom
    ar "...I'm sorry about them, those guys are..."
    mc "Haha, don't worry about it, I thought it was kinda funny."
    mc "Let's just enjoy the rest of our night"
    scene black with fade
    "We finished our dinner..."
    show housenight with fade
    stop music
    play music nightsong loop
    show aarsmile with dissolve
    ar "That was super fun, [mcname]. I'm glad we got to do this!"
    hide aarsmile
    show aarmad
    ar "Although, I could've done without that interruption..."
    mc "Don't get too worked up over it, it wasn't so bad. I still really enjoyed our night"
    hide aarmad
    show aarsmile
    ar "That's good, then. As long as you enjoyed yourself"
    mc "I'll see you around! Good night!"
    ar "Goodnight!"
    if tylermean == 4:
        jump tylersecretend1
    else:
        jump dayend
    





return
