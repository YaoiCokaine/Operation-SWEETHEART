label start:
    $ persistent.ending_karma = False
    $ persistent.ending_nobody = False
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
    "I should probably start unpacking my stuff, and then-"
    play sound doorbell
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
            a "Perfect! I'm a pretty great party planner. This is gonna be awesome!"
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
    scene streetday with fade
    "A walk will do me good!"
    q "YOU NEED TO TRUST ME!"
    "? what was that?"
    qq "I can't trust you! It's been 4 months!"
    q "Dude, just give me some time"
    qq "You've said that multiple times now!"
    "Sounds like there's some people nearby arguing...should I go meddle with that?"
    $ kcconv = False
    $ gardan = False
    menu:
        "Check it out":
            "Let's go have a look-"
            jump choices1_a
        "Leave it be":
            "Not my business."
            jump choices1_b
label choices1_a:
    scene boyshouse with fade
    show garmad at left with dissolve
    qq "You haven't paid your share of the rent, you can't keep getting away with it!"
    show danmad at right with dissolve
    q "dude. I told you. I got this. I'm working on it."
    qq "I really do not believe you"
    q "TRUUSSTTT!"
    "Looks like they're arguing...do I wanna stay for this?"
    menu:
        "Stay":
            jump gardancont
        "Leave":
            "I should go..."
            scene streetday with fade
            jump choices1_b
    label gardancont:
    $ gardan = True
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
    "I guess I'll just sit out here for a bit..."
    show kcnorm with dissolve
    kc "Hmmm? Kawaii-chan has never seen you around here..are you new?"
    mc "Oh! Uh, yeah, I just moved here"
    "Do I want to stay for this conversation? Or follow those voices?"
    menu:
        "Stay":
            jump kcconvcont
        "Leave":
            mc "Sorry! Gotta dash!"
            scene boyshouse with fade
            jump choices1_a
    label kcconvcont:
    $ kcconv = True
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
        show aphphonecall with easeinleft
        a "Hello?"
        mc "Hi Aphmau! I was just calling because I wanted to talk about the party"
        a "Ooo, that's right! You don't have to worry at all about decorations and inviting people, I've got that completely covered! You just think about the food and drinks"
        mc "Oh, alright then! Thanks for everything!"
        a "Anytime! Now, I've gotta get back to what I was doing. I'll pop by tomorrow afternoon to help set up! Bye byeee!"
        hide aphphonecall with easeoutleft
        play sound hangup
        "Glad to know she's got all of that taken care of"
        "Food and drinks...I could make some pasta for everyone!"
    if aphparty == False:
        "How do you even organize a housewarming party? I guess I could cook some food for everyone.."
        "Hopefully pasta works..."
        "I can't wait to meet everyone. It seems like Aphmau will tell all her friends to come over, so maybe I can make some new friends too!"
        "Right, I also need to look for a job here...that's gonna be tough..."
    play sound doorbell
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
    q "You okay? The floor here is slippery, you should be careful"
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
    "Aphmau should be coming soon to help out with the party-"
    play sound doorbell
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
    a "Hehe, perfect! I love making new friends"
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
    "I'm really excited to meet everyone!"
    play sound doorbell
    "Oh, that's them...I'm so nervous!"
    scene frontdoorday with fade
    if aphparty == False:
        show aphnorm with dissolve
        a "Hi [mcname]!! I brought everyone that I could!"
        mc "That's great! Thanks so much"
        a "No problem! I got you this cool scented candle as a gift. I hope you like it!"
        mc "It's lovely, thank you"
        hide aphnorm with dissolve 
    show katnorm at left
    show kcnorm at right
    with dissolve
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
    hide kcmad
    hide katdis     
    hide kcnorm
    hide katnorm
    with dissolve
    show lucinorm with dissolve
    lu "Hey [mcname], i'm Lucinda. I'm a couple houses down from here, nice to meet you"
    mc "Nice to meet you too! Come in."
    lu "Oh, right, I got you this giftcard for CreamyDreamy Coffee Co. , it's a coffee shop nearby"
    mc "Ohhh, that's cool! Thanks!"
    hide lucinorm with dissolve
    show laursmile with dissolve
    la "Hey again, [mcname]!"
    show garnorm at left
    show dannorm at right
    with dissolve
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
    d "I bet he's suckin dick"
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
    hide danmad
    hide garsad
    hide laursad
    hide garnorm
    hide laursmile
    hide dannorm
    with dissolve
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
    t "Suckin dick"
    mc "Oh"
    play sound travlaugh
    t "Haha jk. Was working on a fanfic"
    mc "Oh?"
    t "Yup! I'm an aspiring author~"
    mc "Really? Cool!"
    t "My penname is DaddyValkrum on Wattpad. I'm definitely not going to regret telling you that information"
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
                    play sound dancry
                    define b = Character("Both",color="#FFFFFF")
                    b "AAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!" with hpunch
                    hide aarmad
                    show laurdis with new
                    la "Obviously they're joking guys"
                    hide danscare
                    hide travscare
                    show danmad at left
                    show travshock at right
                    t "yeah.. obviously we knew that...haha..."
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
            $ luciflag +=1
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
            show aphlove at left
            show kcnorm at right
            with dissolve
            a "Kawaii-chan!! These cookies are absolutely awesome!!!"
            kc "Hehe! Kawaii-chan is so glad Aphmau-senpai loves them!"
        else:
            show aphnorm at left
            show kcnorm at right
            with dissolve
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
        show lucinorm at left
        show katnorm at right
        with dissolve
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
        show aarnorm at left
        show laurnorm 
        show garnorm at right
        with dissolve
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
                show aarmad at center 
                show laurdis at left
                with ease
                hide aarmad
                show aarsmile
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
                show garsad at center
                show laurdis at right 
                with ease
                hide garsad
                show garnorm
                play sound garawesome
                $ renpy.notify("Garroth is glad you like his suggestion!")
                g "I knew you'd agree with me, [mcname]!"
                la "But that's ice cream...that's not a proper restaurant..."
                g "You're just mad your restaurant isn't as good as Cloud 9 Nice Ice Cream Parlour!"
                la "No I don't think I am"
                g "[mcname], we'll go get ice cream together so you can see just how good it is!"
                mc "That sounds fun, let's do that!"
                g "Yippee!"
                ar "Yippee..?"
        t "EVERYONE! I'D LIKE TO MAKE A TOAST!"
        jump travtoast
    label travzandanconv:
        $ travflag += 1
        $ zaneflag += 1
        $ danflag += 1
        $ renpy.notify("Travis, Zane, and Dante are glad to talk to you!")
        mc "Let's go see what Travis, Zane, and Dante are up to!" 
        show travnorm at left
        show zanenorm
        show dannorm at right
        with dissolve
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
        if aphparty == True:
            scene houseinsidedecornoon with fade
        else:
            scene houseinsidenoon with fade
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
"I should probably go to bed now.."
play sound doorbell
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
        jump tylersecretend
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
    "There's some tension between these two..but I can't tell what kind...."
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
    hide lucisad
    hide katnorm 
    with dissolve
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
        jump tylersecretend
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
    show garsad at left
    show aarsad at right
    with easeinbottom
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
    hide garshock
    hide aarsad
    with easeoutbottom
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
        jump tylersecretend
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
    ty "Hey guys welcome to the Sizzling Sausage Shack. What can I put in a bun for ya"
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
    show garmad at left
    show laurdis at right
    with easeinbottom
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
    hide garsad
    hide laurdis
    with easeoutbottom
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
        jump tylersecretend
    else:
        jump dayend
label garcream:
    scene houseday with fade
    "I wonder if Garroth's been waiting for me?"
    show garnorm with dissolve
    g "[mcname]! There you are!"
    g "Ready to go?"
    mc "Haha, I was born ready!"
    g "Loving the spirit!"
    scene cloud9 with fade
    show garnorm with dissolve
    mc "Woah..This place has tons of flavours!"
    g "Uh huh! It's got something for everyone! I guarantee you'll love at least ONE flavour"
    mc "We'll have to see"
    show garnorm at left with easeinleft
    show tylercream with dissolve
    ty "Hey guys welcome to Cloud 9 Nice Ice Cream Parlour. What can I scoop up for ya"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.."
    hide garnorm
    show garshock at left
    g "Woah! You guys have met??"
    mc "I- no...sorry...let's just order..."
    hide garshock
    show garnorm at left
    g "Alright! Sorry, Tyler is it? We're gonna need a couple minutes to look at this menu!"
    ty "Then don't come up to the fucking counter how about that"
    hide tylercream with dissolve
    show garnorm at center with ease
    g "Got any idea what you want?"
    mc "I don't know...there's so much to choose from....what do you suggest?"
    g "Oo! You see, they have this super cool special, it's called the Empire State Creamy Supreme. It's one scoop of every flavour, so it's 30 scoops tall!"
    mc "Genuinely how would you even eat that"
    g "Trust me....you just do"
    menu:
        "Too delicious":
            $ empirestate = True
            $ garflag += 1
            mc "That sounds crazy. Let's get it!"
            $ renpy.notify("Garroth is glad you took his suggestion!")
            g "Woohoo! Trust me, when you try this, you'll never want to get normal ice cream again!"
            show garnorm at left with easeinleft
        "Too inconvenient":
            $ empirestate = False
            mc "Sounds too inconvenient...I'll just get Vanilla."
            hide garnorm
            show garsad
            play sound garaww
            g "Aww shucks..."
            show garsad at left with easeinleft
    show tylercream with easeinright
    ty "You guys finally ready to order?"
    if empirestate == True:
        g "Two Empire State Creamy Supremes pleeeaaaaseee"
        ty "I'm quitting my job tonight"
        hide tylercream with easeoutright
        show garnorm at center with ease
    else:
        g "One Empire State Creamy Supreme! And one Vanilla...single scoop.."
        ty "god. Okay"
        hide tylercream with easeoutright
        show garsad at center with ease
    mc "While he does that, why don't we-"
    if empirestate == True:
        show garnorm at left with easeinleft
    else:
        show garsad at left with easeinleft
    show tylercream with easeinright
    ty "Here's your ice cream"
    mc "Woah! That was...a little too fast"
    hide garsad
    show garnorm at left
    g "That's the best thing about this place! The service is super fast!"
    mc "Right.."
    ty "Oh yeah, I spit in yours, btw"
    mc "WHA- Why would you do that!?"
    ty "Idk"
    menu:
        "Yell at him":
            $ tylermean +=1
            mc "YOU FUCKING LOSER!! I HATE YOU. I HOPE YOU ARE CURSED FOR A THOUSAND YEARS YOU DICK"
            ty "CALM DOWN OH MY GOD I WAS FUCKING JOKING"
        "Call his bluff":
            mc "Are you lying"
            ty "Ya"
    g "Come on [mcname], let's go sit!"
    hide garnorm with easeoutleft
    ty "[mcname]- stay back..."
    mc "Wsg gang"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    g "[mcname]! I found a seat!"
    mc "I'm coming Garroth, one second!"
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
    scene garroth_ice_cream_cg_1 with fade
    stop music
    play music daydream loop
    pause (2.0)
    play sound wow
    mc "It's so......tall...."
    g "AND SO GOOD!!! >~<"
    mc "How did you do that"
    g "Hm?"
    mc "Nothing..."
    if empirestate == True:
        mc "This really is awesome, though!"
        g "Told youuu!"
    else:
        g "You would understand if you also got the Empire State Creamy Supreme!"
        mc "Maybe next time.."
    scene garroth_ice_cream_cg_2 with dissolve
    g "God, I love this place!!"
    mc "Haha, I can tell!"
    scene cloud9 with fade
    stop music
    play music daysong2 loop
    show garsad with dissolve
    g "Well, it's gonna take me a minute to finish this...we're gonna be here for a while..."
    mc "Don't worry! Let's talk a bit about ourselves while we wait!"
    hide garsad
    show garnorm
    g "Ooo, I like that! What do you wanna know about me?"
    label garcreamconv:
    define garconv = 0
    menu:
        "What are your hobbies?":
            define hobby = 0
            mc "Do you have any hobbies? Interests?"
            if hobby == 1:
                g "Didn't you already ask me that?"
                jump garcreamconv
            else:
                $ hobby += 1
                g "Let's see...i'm pretty good at cooking! I've been getting into it a lot more recently, I think because lots of my friends cook too, and they look like they're having so much fun!"
                g "I also enjoy fanfiction, it's just so fun to see what passionate people can create!"
                g "I personally believe the most dedicated people in the world are fans. They can do crazy things! Like making Dating Simulators, for example"
                mc "Oddly specific example"
                g "What about you?"
                menu:
                    "Art":
                        $ garconv += 1
                        mc "I really like to draw!"
                        hide garnorm
                        show garsad
                        g "Yeesh...I suck at drawing....I can't even make a circle..."
                        hide garsad
                        show garnorm
                        g "It's cool that you like to draw, though!"
                        g "You know, Kawaii-chan's pretty great at drawing! I should get her to teach me, maybe..."
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "Music":
                        $ garconv += 1
                        mc "I really like music!"
                        g "That's fun! I don't really listen to music all that much, just whatever's playing on the radio"
                        g "My brother Zane know lots more about music than I do, he's a complete nerd for that kind of stuff!"
                        g "I think Laurance and Aaron both play the guitar, too? I'm not too sure."
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "Video Games":
                        $ garconv += 1
                        mc "I really like video games!"
                        g "Ohh, really?? What do you think of Legend of Zelda?"
                        menu:
                            "Love it":
                                mc "I love it!"
                                $ garflag += 1
                                $ renpy.notify("You and Garroth have a common interest!")
                                play sound garawesome
                                g "YIPPEE! That's my favourite video game! It's just so fun! I love everything about it, really!"
                                mc "You kind of look like Link, y'know!"
                                g "Haha, I've cosplayed him a couple times, actually!"
                            "Hate it":
                                mc "I hate it.."
                                hide garnorm
                                show garmad
                                g "WHAT!? WHAT DO YOU HATE ABOUT IT!?"
                                g "Is it the puzzling yet innovative gameplay? The intriguing narrative and compelling storytelling? The beautiful and stellar artwork? The originality that sets it apart from other franchises? The attention to detail that can only be done by the best of game creators?"
                                mc "Sorry, didn't realize that was a soft spot for you..."
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "Writing":
                        $ garconv += 1
                        mc "I really like to write stories!"
                        $ garflag += 1
                        $ renpy.notify("You and Garroth have a common interest!")
                        g "Woah! That's so awesome! I'd love to read your work one day!"
                        g "I've always appreciated authors, they do such a great service for us"
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "I hate everything in this awful world":
                        $ garconv += 1
                        mc "This world is garbage and theres nothing about it that I enjoy"
                        hide garnorm
                        show garshock
                        g "Oh! Um....yea! Totally!"
                        g "Unrelated question, what has Zane been telling you?"
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
        "What do you think of the other residents?":
            mc "What do you think of the other people in our neighbourhood?"
            define resident = 0
            if resident == 1:
                g "Didn't you already ask me that?"
                jump garcreamconv
            else:
                $ resident += 1
                g "Ahh, well, they're all my greatest friends!"
                g "I've known them all for so long...it's kinda crazy to think about, actually! I've seen everyone at their best and worst..."
                g "Haha, don't tell him I told you, but Travis once wrote a Katemau fanfic on Wattpad, his name is DaddyValkrum"
                mc "...Katemau?"
                g "You know, Katelyn and Aphmau!"
                g "He made me read it for feedback and it was...yeesh! Not his best work."
                g "It wasn't anything crazy, but in the end, Aphmau dies and Katelyn runs to Travis. Just a heap of self-projection, really"
                mc "Interesting..."
                define travkatemau = 0
                $ travkatemau +=1
                g "Did you know Laurance used to have bright orange hair back in highschool?"
                mc "Really?"
                g "Yeah! It was only for a year..but his sister dyed his hair so that they could look more alike. He looked sooo funny."
                g "And, same year, he was SOOO obsessed with Twilight! He was convinced he was Edward! He even bought fangs at some point"
                mc "No way! That doesn't sound like him"
                g "Everyone's different in highschool!"
                g "You know, next time you see him, ask him what he thinks about Twilight, and watch the colour drop out of his face!"
                mc "Man, sounds like you and Laurance are close"
                g "The closest! We're best buddies! I don't know what I'd do without him."
                g "He has this power where when you talk to him, you can't help but feel all warm inside...and your heart starts racing..."
                "That might just be you..."
                g "But what do you think of everyone?"
                menu:   
                    "I like them all":
                        $ garconv += 1
                        mc "I know we haven't talked much, but I really like everyone! They all seem so fun and unique, it's refreshing to have such a vibrant friendgroup"
                        $ garflag += 1
                        $ renpy.notify("Garroth finds you admirable!")
                        hide garnorm
                        show garshock
                        g "Wow! I didn't expect you to like everyone already."
                        hide garshock
                        show garnorm
                        play sound garawesome
                        g "That's awesome though! That you're already settling in with everyone!"
                        g "I find it great that you're able to bond with everyone so quickly"
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "I have no opinion":
                        $ garconv += 1
                        mc "Hmm...I don't really have any strong opinions. I haven't really talked to anyone that much"
                        g "That's true....I guess it'll take some time before you really get to know everyone and become friends"
                        g "They're all great people, though! So don't be shy to talk to them."
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "I hate them all":
                        $ garconv += 1
                        mc "I honestly really don't like anyone here. They're kind of annoying..."
                        hide garnorm
                        show garsad
                        play sound garaww
                        g "Awww...that sucks..."
                        g "I hope you change your mind about everyone"
                        hide garsad
                        show garshock
                        g "Wait...do you think i'm annoying too..?"
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
        "Are you looking for love?":
            define love = 0
            $ garconv += 1
            mc "Are you looking for love? Or wait, do you already have someone??"
            if love == 1:
                g "Didn't you already ask me that?"
                jump garcreamconv
            else:
                $ love += 1
                hide garnorm
                show garshock
                g "Am I looking for love?? Geez, I don't know..."
                g "I suppose I am! I would like to have someone I can care about, who can care about me..."
                g "Err...what about you?"
                menu:
                    "Yes":
                        $ garflag += 1
                        mc "I am! I would like to find somebody"
                        $ renpy.notify("Garroth is glad he has a chance with you!")
                        hide garshock
                        show garnorm
                        play sound garawesome
                        g "Sweet! Or, I mean, you know...cool"
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
                    "No":
                        mc "Not really, honestly. Just wanting to go solo for now"
                        hide garshock
                        show garsad
                        g "Aww...alright"
                        hide garsad
                        show garshock
                        g "Uhh...not that it matters to me...you know.."
                        if garconv == 3:
                            jump garcreamcont
                        else:
                            jump garcreamconv
    label garcreamcont:
        hide garsad
        hide garshock
        hide garmad
        show garnorm
        g "Oop! And wouldn't you know it, I'm done my ice cream!"
        g "You have to admit, pretty delicious, right?"
        mc "Oh, absolutely!"
        mc "I'm so glad I came here instead of the pizza or sausage place"
        g "Haha, you understand now!"
        hide garnorm
        show garshock
        g "Uh oh...speak of the devil..."
        mc "What?"
        g "Don't look behind y- No they're over here now"
        show aarsad at left
        show laursad at right
        with easeinbottom
        la "Look's like we got caught.."
        mc "What th- Laurance? Aaron? Why are you two here?"
        ar "We just- well-"
        la "We were spying on you guys..."
        mc "Oh my god..were you listening to what we were talking about..?"
        hide laursad
        show laurdis at right
        la "Yeah, actually. And Garroth, why the fuck would you tell [mcname] about the Twilight thing!?"
        hide garshock
        show garnorm
        g "You have to admit, it was REALLY funny"
        la "You promised that was gonna stay between us two.."
        play sound garlaugh
        g "hehehe"
        ar "We just wanted to make sure you didn't like the ice cream place TOO much."
        mc "But, you two don't even like the same restaurants?"
        la "Yeah but we both agree that Cloud 9 Nice Ice Cream Parlour shouldn't even be part of the conversation"
        ar "Exactly"
        mc "Whatever, you guys! Just...leave!!"
        la "Sorry"
        ar "Have a great rest of your night guys"
        hide aarsad
        hide lardis
        with easeoutbottom
        mc "Those guys..."
        mc "Wait, it's already night?"
        g "Huh. Time sure flies when you're having fun!"
        g "Come on, I can walk you home"
        scene housenight with fade
        stop music
        play music nightsong loop
        show garnorm with dissolve
        g "Today was so great, [mcname]! Let's do this again!"
        mc "Definitely! I'll see you around, goodnight!"
        if tylermean == 4:
            jump tylersecretend
        else:
            jump dayend
label guymovie:
    scene movietheatreoutside with fade
    "Where are the guys? They should be here..."
    d "YOOHOO! [mcname!u]! OVER HERE!"
    show dannorm with dissolve
    show travnorm at left with dissolve
    show zanenorm at right with dissolve
    t "Heyyy! You made it!"
    hide dannorm
    show dansmirk
    play sound danheybaby
    d "Looking fine as ever, of course"
    z "Stop harrassing [mcname]."
    z "Anyway, we're glad you made it on time"
    z "Come on, let's go get our snacks"
    scene movietheatreinside with fade
    show dannorm with dissolve
    d "I'll go get our food! Everyone's fine with a large popcorn and soda, right?"
    show zanenorm at left with dissolve
    z "That sounds good"
    show travnorm at right with dissolve
    t "Yup!"
    mc "Dante, are you sure you wanna grab everything on your own? Want me to come?"
    d "Thanks for the offer, but don't worry! I am EXTREMELY efficent and quick. They don't call me two-minute Dante for nothin!"
    hide travnorm
    show travlaugh at right
    play sound travlaugh
    t "Pfft....two-minute..."
    play sound zanelaugh
    z "I wonder what else he can do in two minutes?"
    hide dannorm
    show danmad
    d "Haha. Very funny guys."
    d "I'll be back"
    hide danmad with easeoutleft
    z "I made sure to get us the best seats. We're right in the middle"
    hide travlaugh
    show travnorm at right
    t "Duuude, awesome! Knew we could count on you!"
    z "Only because last time we tried watching a movie together, you forgot to even buy the tickets..."
    hide travnorm
    show travshock at right
    t "Dude. That was one time"
    hide zanenorm
    show zanemad at left
    z "YOU DID IT THREE TIMES!"
    mc "No way.."
    z "We had to sneak into the projector room to watch the movie, because of this guy"
    t "You have to admit, that was really fun"
    hide zanemad
    show zanesad at left
    z "... Maybe a little..."
    show danlaugh with easeinleft
    d "Oo yeah! I'm back baby! In two minutes!"
    mc "Wow! That's impressive!"
    hide danlaugh
    show dannorm
    d "Hah, thanks. I've been practicing"
    d "Right, should we go in now?"
    z "First- [mcname], who do you wanna sit next to during the movie?"
    menu:
        "Dante":
            $ next_dante = True
            $ next_zane = False
            $ next_travis = False
            $ danflag += 1
            mc "I'll sit next to Dante!"
            $ renpy.notify("Dante's glad you wanna sit with him!")
            d "Oh yeah baby! You see that? [mcname] want's to sit with me! Oh yeah"
            hide zanesad
            show zanenorm at left
            z "Genuinely no one cares"
            hide travshock
            show travsad at right
            t "Yeah. Yeah like who would even care. Cuz we don't. Definitely not."
            z "Oh you're pathetic"
        "Zane":
            $ next_dante = False
            $ next_zane = True
            $ next_travis = False
            $ zaneflag += 1
            mc "I'll sit next to Zane!"
            $ renpy.notify("Zane's glad you wanna sit with him!")
            hide zanesad
            show zaneshock at left
            z "Oh...really? Uh..yeah I don't mind..."
            hide dannorm
            show danmad
            d "Dude. He is like the worst guy to sit next to during a movie"
            t "Mid movie bro's gonna start talking about how the Killer Babez are representative of extensionalism or some stupid shit like that LMFAOO"
            z "Did you...did you mean existentialism?"
            t "See he's already doing it"
        "Travis":
            $ next_dante = False
            $ next_zane = False
            $ next_travis = True
            mc "I'll sit next to Travis!"
            $ travflag += 1
            $ renpy.notify("Travis is glad you wanna sit with him!")
            hide travshock
            show travnorm at right
            t "REALLY??? HELL YEAH!!"
            hide zaneshock
            show zanenorm at left
            z "It's not that serious"
            t "It is that serious! I get to sit next to [mcname]! Woohoooo!!"
    z "Alright let's just go in"
    t "Dude you gotta show the guy our tickets first"
    z "I WAS DOING THAT.."
    if next_dante==True:
        hide travsad
        hide dannorm
        with dissolve
    elif next_zane==True:
        hide danmad
        hide travsad
        with dissolve
        show zaneshock at left with ease
        hide zaneshock
        show zanenorm at left
    elif next_travis==True:
        hide dannorm
        hide travnorm
        with dissolve
    z "Anyway..sir?"
    show tylermovie with dissolve
    ty "Oh right hey welcome. You 4 together?"
    mc "..you again?"
    ty "Pardon? Idk you"
    mc "You...last night...we.."
    z "You know him?"
    mc "I...no..just show the tickets.."
    z "Here they are.."
    ty "Alright, scanned, you guys head on in and enjoy your movie"
    hide zanenorm with dissolve
    hide zanesad with dissolve
    ty "[mcname]- stay back..."
    mc "Wsg gang"
    ty "Remember what I told you last night..."
    mc "Wait! So you do acknowledge yesterday!"
    ty "Just don't fumble this, bad things will happen"
    mc "Why...why are you helping me like this"
    ty "Let's just say...I lost someone close to me who was just like you..."
    mc "..right"
    d "Yo! What's the holdup?"
    mc "Just give me a sec!"
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
    scene theatreinside with fade
    if next_dante == True:
        show zanenorm at left with dissolve
        show travnorm at right with dissolve
        show dannorm with dissolve
    if next_zane == True:
        show travnorm at right with dissolve
        show dannorm at left with dissolve
        show zanenorm with dissolve
    if next_travis == True:
        show dannorm at left with dissolve
        show zanenorm at right with dissolve
        show travnorm with dissolve
    z "Looks like we made it just on time, movie should start soon"
    d "Ohh man, I'm so excited!"
    mc "I'm still a bit confused as to what this movie's about?"
    t "Well, it's a sequel to the movie Rise of the Killer Babez, and in this movie, the Killer Babez fight MICHAEL and..."
    hide travnorm
    if next_travis == True:
        show travshock
    else:
        show travshock at right
    t "Yeah I have no idea what this movie is about"
    stop music
    play music killerbabez loop
    z "Shhh! The movie's starting!"
    scene killerbabez_1 with fade
    define kb = Character("Killer Babez",color="#FFFFFF")
    define michael = Character("MICHAEL",color="#FFFFFF")
    kb "YOU'LL NEVER DEFEAT US! WE'RE BABEZ....AND WE'RE KILLER!"
    scene killerbabez_2
    michael "...and i'm MICHAEL"
    if next_dante == True:
        scene dante_movie_cg_1 with fade
        pause (2.0)
        d "[mcname]!! The babez!! The babez are killer!"
        d "[mcname], this movie is awesome!!"
        mc "Haha! Yeah! This is epic!"
        scene dante_movie_cg_2 with dissolve
        d "Are you enjoying the movie so far?"
        mc "Oh yeah, definitely! This is amazing!"
        d "Right! And the babez....GOD!"
        t "SHHH! I can't hear what they're saying!!!!"
        d "Jesus christ"
    if next_zane == True:
        scene zane_movie_cg_1 with fade
        pause(2.0)
        z "This movie....is so..."
        mc "You don't like it?"
        z "No...it's...awful!"
        kb "Heh, he's right behind me, isn't he?"
        z "The dialogue is so awful! No one talks like that!"
        z "This movie isn't even funny!"
        scene zane_movie_cg_2 with dissolve
        z "...but, i'm glad i'm able to watch it with you..."
        z "A-and the guys! All of us! Of course.."
        mc "Haha, i'm glad too! Nothing beats the theatre experience, no matter how bad the movie is"
        d "Oh so if Zane talks during the movie it's fine but if I talk then i'm the bad guy"
        z "..."
    if next_travis == True:
        scene travis_movie_cg_1 with fade
        pause (2.0)
        t "...."
        mc "Wow, you're really entranced by the movie"
        t "This is....this is cinema...."
        kb "What if i'm just a babe...without the killer?"
        kb "NO! KILLER BABE #3. You are....the most killer of all"
        scene travis_movie_cg_2 with dissolve
        play sound travcry
        t "Oh my god! This is so beautiful!!"
        t "I'm so glad we're watching this together, [mcname]. This is an experience I can't imagine having without you"
        z "SHHH! SOME OF US ARE TRYING TO WATCH A MOVIE!"
        t "ugh. this guy."
    scene black with fade
    "An hour later..."
    stop music
    play music noonsong loop
    scene movietheatreinside with fade
    if next_dante == True:
        show zanemad at left with dissolve
        show travsad at right with dissolve
        show dannorm with dissolve
    if next_zane == True:
        show travsad at right with dissolve
        show dannorm at left with dissolve
        show zanemad with dissolve
    if next_travis == True:
        show dannorm at left with dissolve
        show zanemad at right with dissolve
        show travsad with dissolve
    mc "Well. What a movie!"
    d "What'd you think of it?"
    menu:
        "Loved it!":
            mc "I loved the movie! It was beautiful!"
            if next_dante == True:
                show travsad at center
                show dannorm at right
                with ease
            if next_zane == True:
                show travsad at center
                show zanemad at right
                with ease
            $ travflag += 1
            $ renpy.notify("Travis agrees with you!")
            t "Wasn't it?? Oh my god! It was so beautiful!"
            t "Truly a thinkpiece!"
            t "The ending? Where it turns out the Killer Babez were in a dream, and MICHAEL wasn't a villain, but rather, the hero trying to wake them up!"
            t "And the character arcs....Killer Babe #3 learning that everyone is killer in their own way..."
            t "Brings a man to tears.."
            z "Hey, you were making fun of me for digging deep into movies!"
            t "Uh, yeah, cuz your movies are stupid and this one is awesome"
            t "I bet you Laurance would agree with me, he's a fellow movie connoisseur like moi"
            d "You've watched like 4 movies total"
            t "Yeah? I'm selective"
            mc "I still think it was perfect"
            t "Oh most definitely"
        "Hated it":
            mc "Oh, I really hated it. It was a lazy excuse of a movie"
            $ zaneflag += 1
            $ renpy.notify("Zane agrees with you!")
            if next_dante==True:
                show zanemad at center
                show dannorm at left
                with ease
            if next_travis==True:
                show zanemad at center
                show travsad at right
                with ease
            z "Oh, absolutely! It had a lousy plotline with bland characters, none of it made sense,"
            z "And worst of all, it promised us comedy, but it was painfully unfunny!"
            z "Seriously, the part where MICHAEL goes on a 10-minute monologue about how he wishes he was a Killer Babe too? It was so unneccessary."
            t "Why? What's wrong with MICHAEL wanting to be a Killer Babe?"
            z "It made no sense with the story!! There wasn't any setup or foreshadowing, it was completely random!"
            mc "Definitely, I am not satisfied."
            d "Zane, why must a movie make sense? Can we not simply enjoy ourselves without worry?"
            z "I can't enjoy a movie as stupid as this one.."
            d "Look's like someone's allergic to fun..."
            z "I wish you were allergic to like. Air."
        "Babez were hot":
            mc "I just thought the babez were hot"
            $ danflag += 1
            $ renpy.notify("Dante agrees with you!")
            d "Oh, thank you! The babez were so hot!"
            mc "Truly!"
            t "Is that all you care about?? LOOKS??"
            z "How artificial..."
            t "I can't believe you two...this movie was the best philosophical contribution since Socrates, and all you care about are BOOBS!?"
            d "Yeah?"
            t "...I mean I get that but-"
    d "Anyway! I think we can all agree that we had a fun time, regardless of how we felt about the movie?"
    mc "Definitely!"
    z "I guess.."
    t "I don't think I could ever watch a movie ever again."
    mc "Uh huh"
    if next_dante == True:
        show zanemad:
            xalign 0.0
            linear 0.3 xpos 0.2
        show dannorm:
            xalign 0.5
            linear 0.3 xpos 0.6
        show tylermovie at left with easeinleft
    if next_zane == True:
        show dannorm:
            xalign 0.0
            linear 0.3 xpos 0.2
        show zanemad:
            xalign 0.5
            linear 0.3 xpos 0.6
        show tylermovie at left with easeinleft
    if next_travis == True:
        show dannorm:
            xalign 0.0
            linear 0.3 xpos 0.2
        show travsad:
            xalign 0.5
            linear 0.3 xpos 0.6
        show tylermovie at left with easeinleft
    ty "Hey guys. I have to do this survey to see how satisfactory everyone's experience was"
    ty "So would you say you had a good time or not"
    menu:
        "Good time":
            mc "I think it's safe to say we all had a pretty good time!"
            ty "Alright that's all I needed to know. Thanks or whateva"
        "Awful time":
            $ tylermean +=1
            mc "Genuinely awful. Actually abhorrent. How do you still work here? You need to be fired."
            ty "oh WOW i see how it is. You don't want to stand for the working class, huh? You think I make a liveable wage here?"
            if tylermean ==4:
                ty "You're gonna rue this day.....RUE!!"
            else:
                ty "I hope you have an AWFUL day!!"
    if next_dante == True:
        show zanemad:
            xalign 0.0
            linear 0.3 xpos 0.0
        show dannorm:
            xalign 0.5
            linear 0.3 xpos 0.5
        show tylermovie at offscreenleft
        with ease
    if next_zane == True:
        show dannorm:
            xalign 0.0
            linear 0.3 xpos 0.0
        show zanemad:
            xalign 0.5
            linear 0.3 xpos 0.5
        show tylermovie at offscreenleft
        with ease
    if next_travis == True:
        show dannorm:
            xalign 0.0
            linear 0.3 xpos 0.0
        show travsad:
            xalign 0.5
            linear 0.3 xpos 0.5
        show tylermovie at offscreenleft
        with ease
    hide tylermovie
    d "Hm. I guess we should all go home now.."
    scene housenight with fade
    stop music
    play music nightsong loop
    show dannorm at left
    show zanenorm 
    show travnorm at right
    with dissolve
    d "Massive fun tonight, [mcname]! So glad we invited you!"
    t "Heh, looks like even Zane had fun today!"
    z "Whatever...it was..fine..."
    mc "Haha, I had lots of fun too, guys. We should hang out more!"
    d "Definitely! Goodnight, [mcname]!"
    hide dannorm
    hide zanenorm
    hide travnorm
    with dissolve
    if tylermean == 4:
        jump tylersecretend
    else:
        jump dayend
label tylersecretend:
    stop music
    play music scarysong loop
    scene houseinsidenight
    "Aahh, what a long day wi- wait, the door was unlocked?"
    "That's weird, I must have forgotten to lock it when I left..."
    play sound doorshut
    "!!!" with hpunch
    "The door just shut behind me! What's going on..."
    q "I tried to help you..."
    "That voice..."
    show tylernorm with dissolve
    mc "Tyler!? What are you doing in my house !?!"
    ty "I tried to help you...I warned you of the dangers!"
    mc "Wh- yeah, I remember..."
    ty "But you've been mean to me. Really Really mean to me. I don't like that"         
    mc "What? Dude, you're creeping me out"
    ty "I hope I am!"
    hide tylernorm
    show tylergun
    ty "I hope I am! Because I'm about to kill you right now."
    mc "WHAT!?"
    ty "Yeah"
    mc "Look! Wait! Please! Im sorry!"
    ty "Really??"
    mc "Yes! I'm sorry..."
    menu:
        "-I truly am":
            mc "I'm sorry..I truly am!"
            ty "..."
            ty "like im still gonna kill you"
        "-that you're a BITCH":
            mc "I'm sorry...that you're a little BITCH!!"
            ty "THIS IS WHAT I'M TALKING ABOUT"
    play sound gunshot
    "YEEOOOWWCH!!!" with hpunch
    scene black with fade
    play sound thud
    "..."
    "if only....I was nicer to him..."
    "maybe this wouldn't have happened..."
    $ persistent.ending_karma = True
    centered "{color=#fff}Secret Ending 1: Karma's Embrace{/color}" with dissolve
    return
label dayend:
scene houseinsidenight with fade
if aphchan == 1:
    $ aph = ("Aph")
    $ lol = (nick)
else:
    $ aph = ("Aphmau")
    $ lol = (mcname)
"Ahh...what a long day."
if aphchan == True:
    "Hanging out with [aph] and Kawaii-chan was so much fun!"
if lucikat == True:
    "Hanging out with Lucinda and Katelyn was so much fun!"
if laurrest == True:
    "Hanging out with Laurance was so much fun!"
if aarrest == True:
    "Hanging out with Aaron was so much fun!"
if garrest == True:
    "Hanging out with Garroth was so much fun!"
if travzandan == True:
    "Hanging out with Dante, Travis, and Zane was so much fun!"
"Super tired now, though...I should really go to bed."
scene bedroomnight with fade
scene black with fade
pause (2.0)
scene bedroomday with fade
stop music
play music daysong2 loop
"Woohoo! A new day!"
"I'm not too sure what to do right now..."
"I would like some fresh air, I think.."
scene houseday with fade
"Should I go on a walk around the neighbourhood or to the park?"
menu:
    "Neighbourhood":
        "A simple walk will do!"
        $ neighbourhood =True
        $ park =False
        $ travdrink = False
        $ mcdrink=False
    "Park":
        "To the park we go!"
        $ park =True
        $ neighbourhood =False
        $ travdrink = False
        $ mcdrink=False
show aphsad with dissolve
a "[lol], Do you have a moment??"
mc "Huh?? What's up?"
a "I need your help. I can't find anyone else. It has to be you."
menu:
    "Help her":
        $ aphhelp = True
        jump aphhelp
    "Leave her":
        $ aphhelp = False
        if park==True:
            mc "I'm really sorry, Aphmau. I'm kind of in a rush right now..."
            play sound aphcry
            a "Oh..right..yeah, I get it"
            jump parkevent
        else:
            mc "I'm really sorry, Aphmau. I'm kind of in a rush right now..."
            play sound aphcry
            a "Oh..right..yeah, I get it"
            jump neighevent
label aphhelp:
    $ aphflag += 1
    hide aphsad
    show aphnorm
    mc "Of course I'll help! What's up?"
    $ renpy.notify("Aphmau appreciates your help!")
    play sound aphperf
    a "Aaaa, thank you soooo much!!"
    a "Okay, so I'm working on a cosplay for the convention coming up-"
    mc "Ooo! Who are you cosplaying?"
    a "An OC of mine! Or well, kind of like, a fantasy persona?"
    a "Haha, I have this little..fantasy world, that I like to think about and build upon in my free time"
    a "I won't bore you with all the details, but I sketched up this design for the costume, and I needed some opinions before I went in and started making it!"
    mc "Of course!"
    show aphcostume with dissolve
    a "I've been working on it for a while, but this is the most recent design I came up with"
    show aphnorm at left with ease
    a "So?? What do you think?? Is it awesome? Is it awful?? PLEAASEE"
    mc "Oh my god calm down"
    menu:
        "It's great":
            $ aphflag +=1
            mc "But [aph], seriously, this is so cool! I love this!"
            $ renpy.notify("Aphmau's happy you like it!")
            hide aphnorm
            show aphsad at left
            a "Really? You love it??"
            mc "Yes, really! I honestly can't think of any feedback, this is just...so awesome!"
            hide aphsad
            show aphlove at left
            a "AAA!! Thank you so so soo much!!"
            hide aphlove
            show aphnorm at left
            a "I'm so glad you think it's cool, I really wanted to get a second opinion before I got to work"
            hide aphcostume with dissolve
            show aphnorm at center with ease
            a "I'll see you around! Hopefully I didn't hold you up?"
            mc "Oh, no! Of course not!"
            a "Alright! See ya then! Thanks again, seriously!!"
            hide aphnorm with dissolve
        "It's cringe":
            mc "This is...um...it's definitely something..."
            hide aphnorm
            show aphsad at left
            a "What does...what does that mean..?"
            mc "It's just...cringe? I guess...do you really think you're a fantasy character?"
            mc "Besides...this design looks pretty basic..."
            hide aphsad
            show aphshock at left
            play sound aphwhat
            a "WHAATT???"
            hide aphshock 
            show aphsad at left
            a "I...I spent so much time on it...researched and everything.."
            mc "..better luck next time?"
            hide aphcostume with dissolve
            show aphsad at center with ease
            a "Well...I guess I'll try working on the design, thanks for the help.."
            a "I'll see you around, sorry for holding you up.."
            hide aphsad with dissolve
    if park ==True:
        jump parkevent
    else:
        jump neighevent
label parkevent:
    scene park with fade
    "Wow, this is a gorgeous park! I should definitely try to visit this place more often"
    "Hey, who's that I see in the distance?"
    show travsad at right
    show lucievil at left
    with dissolve
    t "I'M NOT DOING IT!!" with hpunch
    lu "Come on, it won't hurt!"
    lu "...probably"
    t "THAT'S NOT HELPINNGGG" with hpunch
    menu:
        "Talk to Travis and Lucinda":
            jump parkcont
        "Go around neighbourhood instead":
            "On second thought, maybe I'll just walk around the street.."
            jump neighevent
label parkcont:
    $ zaneagree=False
    $ kcagree=False
    $ travdrink=False
    $ mcdrink=False
    mc "Travis! Lucinda! Hey guys!"
    hide lucievil
    show lucismirk at left
    lu "Hey [mcname], me and Travis were just-"
    hide travsad
    show travscare at right
    play sound travcry
    t "THIS BITCH IS TRYING TO KILLL MEEEEEE" with hpunch
    hide lucismirk
    show lucinorm at left
    lu "Okay first off stop screaming pussy"
    lu "Second, it's not even that serious"
    mc "What's going on?"
    lu "I'm working on this potion that's supposed to temporarily heighten all of your senses"
    lu "Just kind of like, a hyper-focus thing, I suppose"
    lu "And I was asking sweet Travis here to test it out for me.."
    t "THAT THING IS LETHAL!!!!!"
    mc "Is it?"
    play sound lucisigh
    lu "...that's what I wanted to find out.."
    t "NOOOO" 
    lu "Travis, it's not a big deal, I just wanna see if it works, I doubt it'll have any side-effects"
    t "you DOUBT?? This is my LIFE we're talking about!"
    lu "You say that like it's precious anyway.."
    menu:
        "Tell Travis to drink the potion":
            $ luciflag +=1
            $ eventful = True
            $ nice = False
            mc "Travis, just drink the potion..nothing's gonna happen!"
            $ renpy.notify("Lucinda appreciates you taking her side!")
            hide lucinorm
            show lucismirk at left
            lu "See, Travis? Even [mcname] says it'll be fine"
            hide travscare
            show travsad at right
            t "..."
            t "Nope. Still not doing it."
            hide lucismirk
            show lucisad at left
            play sound lucisigh
            lu "Ugh, bummer...I really need to test this potion..."
            menu:
                "Threaten Travis":
                    $ travdrink = True
                    mc "Travis. Drink the fucking potion."
                    t "W-what...?"
                    mc "Drink it or else."
                    t "Or else..what??"
                    if travkatemau == 1:
                        mc "A little birdy told me about a certain fanfic of yours?"
                        t "...no..."
                        mc "Would be a shame if Aphmau or Katelyn knew about it..."
                        lu "Huh?"
                        hide travsad
                        show travscare at right with hpunch
                        play sound travcry
                        t "NO! PLEASE! I'LL DO ANYTHING I'LL DRINK IT I'LL PAY YOU JUST PLEASE DON'T TELL THEM"
                        lu "Woah?"
                        hide travscare
                        show travsad at right
                        hide lucisad
                        show lucinorm at left
                        t "Just..just give me the fucking potion.."
                        lu "Alright!"
                    else:
                        mc "Or else...Lucinda here and everyone else might learn about DaddyValkrum.."
                        hide travsad
                        show travscare at right with hpunch
                        play sound travcry
                        t "NOOOOOOOOOOOOOOOOOOOOOOOOOOOO" with hpunch
                        lu "What? The fuck?"
                        t "NOT THAT. PLEASE. PLEASE I'LL DRINK THE FUCKING POTION"
                        mc "That's a good boy!"
                        hide travscare
                        show travsad at right
                        t "This is it. I'm gonna die."
                        t "Tell Zane I always loved him"
                        lu "Wait, what?"
                        t "Let's just get on with it..."
                        play sound lucioohright
                        lu "OOhhkay..."
                        hide lucisad
                        show lucinorm at left
                    lu "So Travis, just drink the potion and tell me if you feel more energized, if your vision improves, anything that you notice"
                    t "okay..."
                    play sound gulp
                    window hide
                    pause (1.0)
                    hide travsad
                    show travnorm at right with dissolve
                    t "Hey, that tastes pretty goo-"
                    play sound thud
                    hide travnorm with easeoutbottom
                    with hpunch
                    lu "woah mama"
                    mc "...hm"
                    show lucinorm at center with ease
                    lu "So...now we know that the potion needs to be fixed.."
                    mc "What do we do with him?"
                    lu "Leave him, he'll wake up soon enough"
                    lu "Nice job convincing him, [mcname]. That was pretty cool"
                    mc "Haha, no problem"
                    lu "I'll see you around, I gotta go fix this potion-"
                    lu "Oh, and if anyone asks, the three of us got lunch and Travis suffered from food poisoning"
                    mc "...got it"
                    lu "Toodles!~"
                    hide lucinorm with dissolve
                    "Wow. What a way to start the morning."
                    "I guess I should head home now"
                    jump housemama
                "Try the potion yourself for Lucinda":
                    $ luciflag += 1
                    $ mcdrink=True
                    mc "...I'll do it! I'll try the potion!"
                    lu "..really?"
                    hide travsad
                    show travshock at right
                    play sound travconf
                    t "Slash gen?"
                    mc "Yeah! You need to test it, right? I'll do it for you!"
                    $ renpy.notify("Lucinda appreciates your help!")
                    hide lucinorm
                    show lucismirk at left
                    lu "Ooo, thank you so so much!! You're super awesome for this"
                    mc "Alright, let's do this."
                    lu "So [mcname], just drink the potion and tell me if you feel more energized, if your vision improves, anything that you notice"
                    mc "Right!"
                    "Okay. Here's to hopping I don't die."
                    play sound gulp
                    window hide
                    pause (1.0)
                    "..Hey, that's pretty good! It's got a bit of a sweet ta-"
                    play sound thud
                    scene black with dissolve
                    stop music
                    lu "[mcname!u]!!!"
                    t "OH MY GOD"
                    jump lucihome
        "Tell Lucinda to lay off":
            $ eventful = False
            $ nice = True
            mc "Hey, Lucinda, knock it off, if he doesn't want to try it, he doesn't have to."
            $ travflag +=1
            hide travscare
            show travsad at right
            $ renpy.notify("Travis appreciates your support!")
            t "Y-yeah! What [mcname] said! I have rights too!"
            play sound lucisigh
            lu "Oh my god you guys are so lame..."
            mc "Go pick on someone your own size!"
            lu "He's taller than me?"
            t "EXACTLY!"
            lu "Right i'm gonna leave you two alone now"
            lu "I guess I'll see you both later.."
            hide lucinorm with dissolve
            show travsad at center with ease
            hide travsad
            show travnorm
            t "Thanks so much for sticking up for me, [mcname]! We need more people like you"
            mc "Haha, no problem"
            hide travnorm
            show travsad
            t "Just thinking about what would've happened if I drank that potion....shivers!"
            t "She's always trying to make me do things for her witch stuff, I can't take it anymore!"
            mc "Haha, now that i'm here, I'll make sure to protect you!~"
            hide travsad
            show travnorm
            t "aa....you're...so cool..[mcname]...."
            t "I really needed this..."
            t "Hey, what were you doing here, anyway?"
            mc "Oh, I was just gonna take a walk around the park, but then I saw you two and wanted to say hi!"
            t "Oh em gee! I don't want to waste your time. Wanna walk together?"
            mc "Sure!"
            jump travwalk
label lucihome:
    hide window
    pause (2.0)
    "..yeeoowwchh..."
    scene lucinda_rest_cg_blur with fade
    lu "[mcname]! [mcname], can you hear me?"
    "hmmm...??"
    play music daydream loop
    scene lucinda_rest_cg_1 with dissolve
    pause (2.0)
    lu "[mcname]? Travis, I think they're waking up."
    t "Finally, I'm tryna go home"
    lu "Can you have some compassion?"
    mc "Lu-.....Lucinda...?"
    scene lucinda_rest_cg_2 with dissolve
    lu "[mcname]! Yes, it's me!"
    lu "Are you alright? How are you feeling?"
    mc "I'm...um...what happened?"
    scene luciroom with fade
    stop music 
    play music noonsong loop
    show travshock at left
    show lucinorm at right
    with dissolve
    t "What happened was Lucinda fed you her RAT POISON and you DIED."
    lu "That is not what happened!"
    t "Yeah? Then what?"
    lu "[mcname], you tried my potion and passed out for like, no more than 6 minutes."
    lu "Travis and I took you here to my house so you could rest. Feeling any better?"
    menu:
        "Feeling awful":
            mc "I feel...awful...yuck"
            hide lucinorm
            show lucisad at right
            lu "Aww..you poor thing...want a kiss to make you feel better?~"
            t "WHAT? You don't kiss me when I'm hurt!"
            lu "Yeah cuz I don't like you"
            t "HEY"
        "Feeling alright":
            mc "I'm feeling alright..! Just a bit tired...don't worry about me"
            lu "Oh, what a relief! We were so worried!"
            t "You're not gonna press charges right"
            menu:
                "I will":
                    mc "I will"
                    hide travshock 
                    show travscare at left
                    play sound travcry
                    t "NOOOOOOOOOOOOOOOOO MY SQUEAKY CLEAN RECORD" with hpunch
                    lu "Travis they're joking why would they press charges"
                    hide travscare
                    show travshock at left
                    t "Yeah I knew that...just wanted to know if you knew that...yknow"
                    lu "Uh huh"
                "I won't":
                    mc "No what- why would I press charges against you two"
                    t "Trust me i've had some scares back in my day"
                    mc "Seriously who are you"
    hide lucisad
    show lucinorm at right
    lu "Alright anyway, here's some water, it should help you feel a bit better"
    lu "..speaking of, did you notice any effects from the potion?"
    mc "Uhh...not really"
    lu "Fuck! How did I mess up this badly..?"
    hide travshock
    show travlaugh at left
    play sound travlaugh
    t "HAHAAAA you suck at your jobb lmfaooo"
    lu "I don't wanna hear it from the guy who cares more about Twitter drama than his own family"
    lu "To be bad at your job you'd need to have a job first"
    hide travlaugh
    show travshock at left
    t "See this is why we don't hang out one-on-one that much"
    mc "I'm sensing some hostility, I think I should go..."
    lu "Aht, no, no hostitlity here! Travis and I...uh...we joke! Yeah"
    mc "Haha, seriously though, I should probably head home, I don't want to trouble the two of you any longer."
    lu "Well, i'm glad that you're feeling better."
    hide lucinorm
    show lucisad at right
    lu "I'd hate if you got hurt over something I did.."
    mc "No no, it's not your fault! I just wanted to help you!"
    lu "And I can't ever thank you enough"
    window hide
    pause (2.0)
    lu "Travis why are you still here"
    t "Oh right yeah sorry I forgor"
    hide travshock with easeoutleft
    show lucisad at center with ease
    lu "Will you really be alright by yourself?"
    mc "Mhm! No need to worry about me"
    lu "Alright, then I'll see you later, kay?"
    mc "Bye Lucinda!"
    jump housemama
label travwalk:
    scene travis_walk_cg_1 with fade
    pause (2.0)
    t "We really should hang out more often, just the two of us, y'know?"
    mc "We should! I'd like to get to know you more!"
    t "I am actually, like, super cool. And you're super cool too! We're perfect together, actually"
    t "Haha, you know what they say, two rights make a wr- wait, I don't think that's the right line..."
    mc "Were you really just about to use a pick-up line on me??"
    t "I wanted to make you laugh!"
    mc "It was just a little bit funny, I'll give you that"
    t "Hehe!"
    scene travis_walk_cg_2 with dissolve
    stop music
    play music daydream loop
    t "You know, back in high school, Dante gave me tons of dating advice. He had a whole book and everything"
    t "Before that, I was super shy, could barely talk to anyone, but his advice really changed me"
    t "I became a lot more confident since then! Flirty, too. I mainly just used whatever tips Dante told me"
    t "But when I'm with you...I don't really feel the need to use all that, I feel like I can just talk to you how I normally would"
    mc "...r-really?"
    t "Sorry, I just made things awkward-"
    mc "No no, it's fine! I'm glad you can be yourself around me!"
    mc "You shouldn't ever have to feel like you need to be someone else"
    t "Ha, thanks, [mcname]. See? You're so cool!"
    mc "I guess I am! Haha"
    scene black with fade
    "We walked around for a bit..."
    scene parknoon with fade
    stop music
    play music noonsong loop
    show travnorm with dissolve
    play sound travlaugh
    t "So then I said, 'That's not a camel, that's my wife!'"
    t "Come on, it's a little bit funny!"
    mc "Haha..yeah"
    mc "Woah! It's already noon??"
    t "Wow! That's crazy"
    mc "I really should get going now, Travis."
    t "This was really fun, [mcname]. I like hanging out with you"
    hide travnorm
    show travflirt
    t "We really need to be together more often, dontcha think?"
    mc "Not when you're like that, we won't"
    hide travflirt
    show travnorm
    t "I'm playing! I'm playing"
    t "Seriously, we should get together again"
    mc "Absolutely!"
    t "Sweeeet"
    t "Welp! I gotta bounce. I'll see you around then!"
    mc "Bye Travis!"
    jump housemama
label neighevent:
    $ nice=False
    $ eventful=False
    scene streetday with fade
    "This is a really beautiful street. Much nicer compared to my hometown"
    "Man, I must be the luckiest person in the world! Being able to find a house in such a great neighbourbood filled with awesome people."
    "Speaking of awesome people, I think I recognize those two up ahead!"
    show zanemad at left
    show kcmad at right
    with dissolve
    z "You're WRONG! You are so incredibly WRONG!" with hpunch
    kc "Kawaii-chan isn't wrong, Zane-kun is!!" with hpunch
    "Looks like they're arguing...should I meddle with that?"
    menu:
        "Talk to Zane and Kawaii-chan":
            jump neighcont
        "Go to the park instead":
            "On second thought, maybe I will go to the park..."
            jump parkevent
    label neighcont:
    mc "Zane! Kawaii-chan! Hey guys!"
    z "Oh. [mcname], hey"
    kc "[lol]-san! This may not be the time.."
    mc "Why? What's going on?"
    z "Kawaii-chan and I are in a bit of an argument.."
    play sound kchey
    kc "A HEATED one!!!"
    mc "Okay...what are you even arguing over"
    z "Kawaii-chan, don't-"
    kc "Zane-kun believes that the best episode of My Little Horsies is the one where Pinkie Cake falls into depression or whatever.."
    kc "When really, the best episode is when Rainbow Flash learns her self worth when Pinkie Cake shows her how much she cares about her!"
    play sound zaneno
    z "FIRST OF ALL! It's not WHATEVER. Pinkie Cake forms self-esteem issues and feels that no one takes her seriously and that she's doomed to be the silly one, but is able to get through it with the help of her best friends!" with hpunch
    z "It's a deeply emotional and symbolic episode that develops Pinkie Cake's character while also showcasing My Little Horsies at it's best, when the Mane 6 all come together and work through their problems using friendship!"
    z "Compared to your silly episode..."
    kc "Uh, nuh uh! Rainbow Flash and Pinkie Cake's relationship is so much more fleshed out in 'Rainbow Flash's Dilemma'."
    kc "You can see that despite their differences, Pinkie Cake understands Rainbow Flash and her insecurity as the middle child to an older sister that's paid more attention by their parents!"
    z "That's only because 'Pinkie Cake and the Sad Times' features EVERY PONY! So they focus on each pony's relationship with Pinkie! And it goes into so much depth about how Pinkie Cake tries to stand out within her big family, going as far as to create this bubbly persona!"
    z "Better than The Godfather, really."
    kc "[lol]-san agrees with me, right??"
    mc "Uhh-"
    menu:
        "Rainbow Flash's Dilemma is better":
            $ kcagree = True
            $ zaneagree = False
            $ alonewalk = False
            jump kcagree
        "Pinkie Cake and the Sad Times is better":
            $ kcagree =False
            $ alonewalk=False
            $ zaneagree=True
            jump zaneagree
        "Both of you suck":
            $ kcagree =False
            $ alonewalk=True
            $ zaneagree=False
            mc "I think both of you are weird for liking a kid's show this much like what the fuck"
            mc "Are you guys not pushing 30 or"
            z "..."
            z "Come on, Kawaii-chan! Let's take our intellectual debate elsewhere."
            kc "Mhm!"
            hide zanemad
            hide kcmad
            with dissolve
            "...I guess they're both mad at me now."
            "Maybe that resolved their conflict...?"
            "I guess I'll just walk around on my own..."
            scene black with fade
            pause (1.5)
            scene streetnoon with fade
            stop music
            play music noonsong loop
            "What an exhilirating walk. I should head home now."
            jump housemama
    label kcagree:
    $ kcflag += 1
    mc "I haven't seen it, but Rainbow Flash's Dilemma sounds more intriguing..."
    mc "I'm more interested in Rainbow Flash's dynamic with her older sibling, how by being neglected by her parents affects her self esteem and ability to form relationships as and adult"
    mc "If only there was someone like Rainbow Flash to show us what that's like..."
    z "...WHATEVER! YOU DON'T UNDERSTAND REAL TELEVISION!"
    hide kcmad
    show kcnorm at right
    $ renpy.notify("Kawaii-chan's glad you agree!")
    kc "Hehe, don't worry [lol]-san, Zane-kun just doesn't get it~"
    mc "Hehehe!"
    z "H-Hey! You don't even watch My Little Horsies, [mcname]!"
    if aphchan == True:
        z "And....what's up with '[nick]'..?"
        kc "That's the nickname Kawaii-chan and Aphmau-Senpai came up with!"
        z "Right..."
    mc "Just because I haven't watched the show doesn't mean I can't give input!"
    z "That's exactly what that means."
    kc "Thanks for settling our debate, [lol]-san!"
    z "What? The debate hasn't been se-"
    mc "No problem, Kawaii-chan!"
    z "Grrrrr, I'm going home!"
    hide zanemad with dissolve
    show kcnorm at center with ease
    kc "Hehe, Zane-kun get's mad easily, but he doesn't mean it most of the time..."
    mc "I feel a little bad.."
    kc "Don't! Zane-kun knows we're joking around!"
    mc "Mhm"
    kc "So, where was [lol]-san going?"
    mc "Oh, nowhere in particular! I was just walking around. Wanted some fresh air."
    kc "Oooo, can Kawaii-chan join [lol]-san on your walk?"
    mc "Sure! I don't mind!"
    scene kawaiichan_walk_cg_1 with fade
    stop music
    play music daydream loop
    pause (2.0)
    kc "The breeze is so nice today..."
    mc "It is!"
    kc "Kawaii-chan loves talking to [lol]-san..."
    kc "She knows we just met...but..."
    kc "Kawaii-chan just senses such kind energy from [lol]-san!"
    mc "Aww, thank you.. but you're the real kind one here, Kawaii-chan"
    play sound kclaugh
    kc "Hehee~"
    menu:
        "Ask about the way she speaks":
            mc "So..why do you uh, talk like that? In 3rd person with the honorifics?"
            scene kawaiichan_walk_cg_2 with dissolve
            kc "Hm? Oh...err...that's just how...Kawaii-chan speaks..."
            kc "No real reason.."
            mc "Have you been talking like that since you were born?"
            kc "Ummm..."
        "Ask about her name":
            mc "So...is Kawaii-chan just a nickname? Or.."
            scene kawaiichan_walk_cg_2
            kc "Umm..that's..."
            kc "That's Kawaii-chan's real name..."
            mc "Really?"
            kc "Yeas...."
            mc "That's pretty peculiar...did your parents have any reason as to why-"
    kc "Wow! The sun is already setting!"
    scene streetnoon
    stop music
    play music noonsong loop
    show kcsad with dissolve
    mc "I'm sorry, was that too personal?"
    kc "A little.."
    mc "That's my bad, I should've realized that wasn't appropriate to ask.."
    kc "It's okay...Kawaii-chan knows she's a bit weird..."
    mc "You're not weird! I just wanted to know more about you.."
    mc "Don't ever let anyone tell you you're weird, Kawaii-chan"
    kc "Hehe...thank you, [lol]-san."
    kc "One day, Kawaii-chan would love to tell [lol]-san everything about herself-"
    kc "But...she's not ready.."
    mc "Don't pressure yourself."
    hide kcsad
    show kcnorm
    kc "Kawaii-chan is so happy [lol]-san understands..!"
    mc "Of course!"
    kc "Well, Kawaii-chan should probably go home now...she assumes [lol]-san has things to do too?"
    mc "You're right, yeah, I do"
    mc "I'll see you around, Kawaii-chan!"
    kc "Bye byeee~!"
    hide kcnorm with dissolve
    jump housemama
    label zaneagree:
    $ zaneflag += 1
    mc "I haven't seen it, but Pinkie Cake and the Sad Times sounds more intriguing..."
    mc "I'm more interested in Pinkie Cake's persona. How she feels that in order to stand out, she has to be someone she isn't, a caricature of sorts. Hiding who she really is because she can't guarantee that her friends will like the REAL Pinkie Cake"
    mc "If only there was someone like Pinkie Cake to show us what that's like..."
    kc "...Kawaii-chan still doesn't agree!"
    hide zanemad
    show zanenorm at right
    $ renpy.notify("Zane is glad you agree!")
    play sound zanethanks
    z "See, Kawaii-chan? Even [mcname] agrees."
    z "..thanks..by the way"
    kc "Grr..."
    z "Why don't you give it another watch, Kawaii-chan? Maybe you'll see the true greatness this time around."
    kc "MAYBE SHE WILL!"
    hide kcmad with dissolve
    show zanenorm at center with ease
    mc "She's stubborn, isn't she?"
    z "Quite."
    z "I'm shocked, you were able to tell which episode is better based on a simple description"
    mc "I'm shocked too, I never pegged you to be a My Little Horsies fan~"
    hide zanenorm
    show zaneshock
    z "Uh- I- Well-"
    mc "It's okay, Zane, I don't care. It's okay to like that show"
    z "...you don't think i'm lame?"
    mc "What? Of course not!"
    mc "Hey, if it makes you feel any better..."
    menu:
        "I like Guardian Moon":
            mc "I like kid's shows too! Guardian Moon is my favourite."
            z "Ah, that's the one Kawaii-chan and Aphmau like.."
        "I like Fairy Club":
            mc "I like kid's shows too! Fairy Club is my favourite."
            z "Oh, I know Lucinda used to like that show a lot.."
    hide zaneshock
    show zanesad
    z "That..actually does make me feel a little better...knowing we're similar.."
    hide zanesad
    show zanenorm
    z "Uh. Anyway. What were you doing here?"
    mc "Oh, right! I wanted to go on a walk around the neighbourhood, but then I saw you guys and wanted to see what was up."
    z "Mhm..well..since we're both here...I hope you wouldn't mind if I were to join you..?"
    mc "Of course not!"
    z "...yay.."
    scene zane_walk_cg_1 with fade
    stop music 
    play music daydream loop
    pause (2.0)
    z "This place looks so nice when the sun sets.."
    mc "It does, Doesn't it?"
    z "Walking around at this time is one of my favourite things to do. There's not much people around...its calm..quiet."
    mc "You're much more....reserved, compared to everyone else"
    z "That's just how I am, I guess.."
    mc "..can I ask, why you wear that mask?"
    scene zane_walk_cg_2 with dissolve
    z "...."
    mc "You don't have to tell me if you're not comfortable."
    z "..Just..not a fan of how I look. It's easier with the mask.."
    mc "I'm sure you look ama-"
    z "No, don't do that! Don't tell me you think I look fine, it's not true and you saying that won't do anything.."
    mc "Well, even then, looks don't matter, Zane."
    mc "I know that on the inside, you're beautiful, and I'd much prefer that over you looking good or whatever"
    scene zane_walk_cg_1 with dissolve
    z "..thanks, [mcname]"
    scene streetnoon with fade
    stop music
    play music noonsong loop
    show zanesad with dissolve
    z "If you want me to take my mask off for you, I won't."
    mc "Don't worry, I'd never want you to do anything you don't want to."
    mc "Zane, I just want you to know...I wish you could give yourself more credit..you're so great!"
    mc "I know we just met, but seriously Zane, I like hanging out with you, believe me"
    z "..."
    z "So corny..."
    mc "Hey, I was being nice!" with hpunch
    hide zanesad
    show zanenorm
    z "Haha, you're right, sorry."
    z "..I really appreciate that, [mcname]. You're one of the only people I feel really sees me."
    mc "Of course, Zane."
    z "I should go now, I have some things to do. But thanks for this walk, I really needed this"
    z "Bye, [mcname]"
    mc "Bye Zane!"
    hide zanenorm with dissolve
    jump housemama
label housemama:
    scene houseinsidenoon with fade
    if eventful ==True:
        "Hm. What an...eventful morning."
    elif nice==True:
        "That was a really nice walk with Travis. I'm glad I got to see more of who he really is."
    elif kcagree==True:
        "Walking with Kawaii-chan was fun, I hope one day I could learn more about her.."
    elif zaneagree==True:
        "Walking with Zane was fun, I hope he really listened to everything I said.."
    elif alonewalk==True:
        "What a nice walk on my own."
    "But wow, time really flew by today, I haven't even had breakfast yet!"
    "I'll just go make some cereal."
    scene kitchen with fade
    "Bowl of cereal, aanndd..."
    "No! What? I have no milk!"
    "I must've forgotten to get some since I bumped into Laurance the other day..."
    "Oh, I really don't feel like going to the grocery store, but I already poured the cereal.."
    "Maybe I can ask around to see if anyone would let me borrow some milk?"
    $ luciknow = False
    label ask:
    menu:
        "Ask Aphmau, Kawaii-chan, and Katelyn":
            "I'll go ask the girls!"
            jump askgirl
        "Ask Laurance, Dante, Travis, and Garroth":
            "I'll go ask the guys!"
            jump askguy
        "Ask Zane":
            "I'll go ask Zane!"
            jump askzane
        "Ask Aaron":
            "I'll go ask Aaron!"
            jump askaaron
        "Ask Lucinda" if luciknow==False:
            if park==True:
                "Lucinda might be busy with her potion, I don't want to bother her..."
                "Who else could I ask?"
                $ luciknow =True
                jump ask
            else:
                "I'll go ask Lucinda!"
                scene lucihouse with fade
                "Ringing the doorbell.."
                play sound doorbell
                window hide
                pause (2.0)
                "Looks like she isn't home.."
                "Who else could I ask?"
                menu:
                    "Ask Aphmau, Kawaii-chan, and Katelyn":
                        "I'll go ask the girls!"
                        jump askgirl
                    "Ask Laurance, Dante, Travis, and Garroth":
                        "I'll go ask the guys!"
                        jump askguy
                    "Ask Zane":
                        "I'll go ask Zane!"
                        jump askzane
                    "Ask Aaron":
                        "I'll go ask Aaron!"
                        jump askaaron
label askgirl:
    scene aphdoor with fade
    play sound doorbell
    pause (2.0)
    show aphnorm with dissolve
    a "[lol]? Hey! What're you doing here?"
    mc "Hi [aph]! Sorry to bother you, but is it possible that I could borrow some milk?"
    if aphhelp ==True:
        a "Oh, yeah, of course! You helped me, so I help you"
        a "Come on in!"
    else:
        a "Hah...so you'd like my help..."
        mc "Hm?"
        a "Sorry! Come on in"
    scene aphhouse with fade
    show aphnorm with dissolve
    a "I'll just put the milk in a cup for you, give me a second!"
    hide aphnorm with dissolve
    "What shall I do while I wait..."
    menu:
        "See Aphmau in the kitchen":
            jump aphkitchen
        "Visit Katelyn's room":
            jump katroomawyeah
        "Visit Kawaii-chan's room":
            jump kcroomawyeah
    label aphkitchen:
    $ aphflag += 1
    scene kitchen with fade
    show aphnorm with dissolve
    $ renpy.notify("Aphmau enjoys your company!")
    a "Oh! You scared me there.."
    mc "Sorry! Oh wow, our kitchens look identical"
    a "Sooo...you were too lazy to go grocery shopping today?"
    a "I get that, I never feel like going grocery shopping.."
    mc "Haha, not necesarrily, I went shopping a while ago but...was distracted.."
    mc "Forgot to buy milk and I didn't feel like going to the grocery store just for one thing"
    a "Haha! But you'll have to get the milk eventually?"
    mc "I know, I know! I just...I'll do it next week"
    a "What do you need the milk for? Oh! Are you baking something??"
    mc "I wish, just making cereal"
    hide aphnorm
    show aphconf
    a "Cereal?"
    mc "Yeah I kinda forgot to eat breakfast today.."
    hide aphconf
    show aphshock
    play sound aphwhat
    a "WHAATT??"
    a "[lol], it's noon! Have you seriously not eaten anything!?"
    mc "I forgor.."
    a "[lol], seriously, that's an awful habit! You need to be eating breakfast! It's the most important meal of the day!"
    mc "I'm sorry! I'm sorry!"
    a "If you ever feel like you don't want to make breakfast, drop by here! I'd happily make you something"
    menu:
        "You're not my mom":
            mc "You're not my mom tf"
            hide aphshock
            show aphsad
            a "I wasn't trying to be..."
            hide aphsad 
            show aphnorm
            a "Anyway.."
        "Thank you":
            mc "Thanks for the offer, but this was a one time thing, I swear.."
            hide aphshock
            show aphnorm
            a "That's good to hear."
    a "Sorry if this is kinda random, [lol], but I am really grateful that you're here"
    mc "Asking for milk?"
    a "No! I mean, here in the neighbourhood!"
    a "You're really cool, and fun, and I'm glad to have a new friend, y'know?"
    a "You've been an awesome new neighbour, really!"
    mc "Oh, thank you, Aphmau..I'm glad I'm here too."
    mc "I'll be honest, this wasn't my first choice to move, but I'm really glad I came here anyway."
    mc "I hope I can bring more excitement to you guys!"
    a "Hah, don't worry about that, you're not like, our toy, or anything"
    a "You simply being here is exciting enough!"
    mc "Oh stawp it, you're too kind~~"
    a "Anyway, here's your milk!"
    mc "Oh, thank you so much! Seriously!"
    a "No problem!"
    a "And remember, from now on, breakfast is the very first thing you do when you wake up!"
    mc "Right, I'll try to remember that.. see ya!"
    jump milkafter
    label katroomawyeah:
    scene katroom with fade
    $ katflag += 1
    show katnorm with dissolve
    $ renpy.notify("Katelyn enjoys your company!")
    k "Oh, [mcname], hey, what are you doing here?"
    mc "Sorry, I came to borrow some milk, Aphmau's getting it for me.."
    mc "Just wanted to see what you're up to"
    k "Oh, cool. I was just watching a show, was thinking of maybe playing some volleyball after this."
    mc "What're you watching?"
    k "Uh..it's this show called Once Upon A Time, I was just rewatching an episode I liked"
    menu:
        "I love that show!":
            mc "Hey, I love that show!"
            hide katnorm
            show katsmile
            $ katflag +=1
            $ renpy.notify("Yoou and Katelyn share a common interest!")
            k "Wait, really? Oh my god! I haven't met anyone who's liked the show!"
            k "Everyone thinks it's stupid, but I always liked it. It's what started my passion for theatre, I'd say"
            mc "Woah, you're into theatre? Didn't know that!"
            k "I guess I don't really talk about it often..but yeah, I'm into dramatic arts and all that stuff."
            k "You should ask Aphmau, I'm always dragging her off to watch whatever musical's in town."
            k "Maybe that's something we'll have to start doing together?"
            mc "I wouldn't mind!"
            hide katsmile
        "Fuck ass show":
            mc "That show? It's so stupid.."
            hide katnorm
            show katdis
            k "..oh. You're one of those.."
            k "It's not stupid, for your information, but I don't want to waste my breath explaining to you why it's good."
            mc "Uh huh.."
            hide katdis
    show katnorm
    k "So, wait, you came here to get milk?"
    mc "Yeah, no, I forgot to get some when I went grocery shopping, and I really wanted cereal.."
    k "Cereal? It's noon"
    mc "Can you not judge my choices"
    k "Haha, no judging here, I get you"
    k "Can I just say, [mcname], I'm really glad you decided to move here"
    k "Don't get me wrong, I love everyone-"
    hide katnorm
    show katdis
    k "..mostly everyone.."
    hide katdis
    show katnorm
    k "But after a while, things kinda get boring when you talk to the same people every day..."
    hide katnorm
    show katsmile
    k "I feel though that you're gonna bring lots of more fun times around here."
    mc "Oh, well, thank you, Katelyn. I really do hope I can bring something exciting to you all"
    k "I know you will!"
    mc "I've only been here a couple days, but so far, I really am loving it here a lot more than I thought I would!"
    mc "You guys are all so fun to be with-"
    a "[lol]?"
    mc "Oh! That's my milk. I'll see you around, Katelyn!"
    jump aphmilk
    label kcroomawyeah:
    scene kcroom with fade
    $ kcflag +=1
    if park==False:
        if kcagree==True:
            show kcnorm with dissolve
            $ renpy.notify("Kawaii-chan enjoys your company!")
            kc "[lol]-san! Hi! Kawaii-chan is glad to see you again!"
            mc "Hey Kawaii-chan!"
        else:
            show kcmad with dissolve
            kc "Oh, [lol]-san...Hi..."
            mc "..are you still mad at me over the My Little Horsies thing?"
            kc "..a little.."
            mc "Come on, Kawaii-chan, it wasn't personal!"
            hide kcmad
            show kcnorm
            kc "Haha, [lol]-san is right, Kawaii-chan is being stubborn."
        kc "So, what is [lol]-san doing here anyway?"
    else:
        show kcnorm with dissolve
        kc "[lol]-san! What are you doing here?"
    mc "Funny story, actually..I was making cereal-"
    kc "Cereal? At noon...?"
    mc "Yeah no I forgot to have breakfast today.."
    hide kcnorm
    show kcsad
    kc "[lol]-san! It's noon, almost night! How could you forget??"
    mc "I'm sorry! This isn't a regular thing, I swear!"
    kc "Better not be...breakfast is incredibly important!"
    mc "I know...oh, right, I hope you don't mind that I just barged in.."
    hide kcsad
    show kcnorm
    if kcagree==False:
        $ renpy.notify("Kawaii-chan enjoys your company!")
    kc "Oh, it's alright! Kawaii-chan doesn't mind! She likes your company!~"
    mc "Soo, what were you up to?"
    kc "Oh, Kawaii-chan was just doodling, nothing much..."
    kc "Here, Kawaii-chan was working on a self-portrait for funsies!"
    show kcportrait at center with easeinbottom
    kc "Does [lol]-san think it's good..?"
    menu:
        "That's awesome!":
            mc "Woah, Kawaii-chan, that's so awesome! I didn't know you were such a great artist!"
            $ kcflag +=1
            $ renpy.notify("Kawaii-chan appreciates the compliment!")
            show kcnorm at left with ease
            kc "Hehe, thanks so much! But Kawaii-chan isn't that good.."
            mc "No, really, you are!"
            play sound kclaugh
            kc "Well...I guess she's a little good.."
            hide kcportrait with easeoutbottom
            show kcnorm at center with ease
        "Needs some work":
            mc "Hmmm..I don't know, it could be better..."
            mc "Your art style is kind of weird.."
            hide kcnorm
            show kcsad
            show kcsad at left with ease
            kc "R-really..? [lol]-san thinks it's weird..?"
            mc "Yeah...is this uhh..'anime'?"
            kc "Well, um, yes.."
            mc "Hmm.."
            kc "Uhh, Kawaii-chan will take that..."
            hide kcportrait with easeoutbottom
            show kcsad at center with ease
            hide kcsad
            show kcnorm
    kc "Anyway...can Kawaii-chan tell you something, [lol]-san?"
    mc "Sure! What's up?"
    kc "Well, everyone has been glad [lol]-san's here, but Kawaii-chan especially is really happy!"
    kc "She thinks [lol]-san is exciting, and fun, and Kawaii-chan just wants to thank [lol]-san for being here."
    mc "Oh, Kawaii-chan..that's so sweet, thank you, I don't know what to say.."
    kc "Hehe, [lol]-san doesn't have to say anything! Kawaii-chan just wishes to express her gratitude~"
    a "[lol]?"
    mc "Oh! That's my milk. It was fun talking to you, Kawaii-chan"
    kc "See ya later!"
    jump aphmilk
    label aphmilk:
    scene aphhouse with fade
    show aphnorm with dissolve
    a "Here's your milk!"
    mc "Thanks so much, truly!"
    a "Anytime!"
    jump milkafter
label askguy:
    scene guydoor with fade
    play sound doorbell
    pause (2.0)
    show dannorm with dissolve
    play sound danheybaby
    d "Yoo! [mcname], what's up?"
    mc "Hey Dante, so sorry to bother you, but is it possible I could borrow some milk?"
    d "Oh, yeah, sure, come in"
    scene guyhouse with fade
    show dannorm with dissolve
    d "Hang in there for just a second, I'm gonna go see if we have any that isn't expired"
    mc "What"
    hide dannorm with dissolve
    "What shall I do while I wait..."
    $ travnotknow =False
    label guyask:
    menu:
        "See Dante in the kitchen":
            jump dankitchen
        "Visit Laurance's room":
            jump laurroomawyeah
        "Visit Travis's room" if travnotknow==False:
            if park ==True:
                if travdrink ==True:
                    "You know, Travis is probably still out there at the park..."
                    "Who else could I visit?"
                    $ travnotknow =True
                    jump guyask
                else:
                    jump travroomawyeah
            else:
                jump travroomawyeah
        "Visit Garroth's room":
            jump garroomawyeah
    label dankitchen:
    $ danflag +=1
    scene kitchen with fade
    show dannorm with dissolve
    $ renpy.notify("Dante enjoys your company!")
    d "Ya, so it turns out we DO have non-expired milk! Isn't it beautiful how life works that way?"
    mc "I'm a bit concerned is expired milk normal for you guys"
    hide dannorm
    show danmad
    d "Hey, clearly you aren't shopping for new milk either, so not too much on us"
    mc "You're right I'm sorry"
    hide danmad
    show dannorm
    d "Hahaaaa, I'm just playing."
    d "Oh yeah, I hope you don't mind, this is Skin milk"
    mc "Oh yeah no it's fi- did you mean Skimmed milk?"
    d "No this is like, some special milk we got a couple years ago, it's supposed to be derived from like angel skin or something"
    mc "A couple YEARS?"
    hide dannorm
    show danmad
    d "Yeah you see why I had to check if it was expired?"
    mc "Have you drunk this before??"
    d "Of course?"
    mc "..and you're alive?"
    play sound danhuh
    d "Why wouldn't I be?"
    mc "Dante you're drinking years-old milk that is 'derived from angel skin' there's gotta be like ecstasy or something in there"
    d "I don't know, I don't think MaccyDonald's would put ecstasy in their milk,"
    mc "YOU GOT IT FROM MACCYYDONALDS ?"
    d "Well, you know the guy behind the MaccyDonald's? Says he's part of the FBI?"
    mc "Dante I don't want to talk about the milk anymore"
    d "Yeah this happens a lot"
    hide danmad
    show dannorm
    d "So, like, how's the move been? You liking this place?"
    mc "Oh, yeah, it's been great, I've really been enjoying talking to all of you guys!"
    d "Sweet! We all like you too. It's been kinda boring around here, we've been waiting for something to spice everything up, y'know?"
    mc "I can't imagine you lot being bored.."
    d "Welp, here's your milk. Couldn't find a glass to put it in so I hope this baby bottle suffices?"
    hide dannorm
    show danmad
    d "It's for Laurance's brother just- don't tell him I gave it to you"
    mc "You have fun Dante"
    jump milkafter
    label laurroomawyeah:
    scene laurroom with fade
    show laurshock with dissolve
    la "[mcname]! What a surprise"
    $ laurflag +=1
    la "What are you doing here?"
    mc "Sorry, came to borrow some milk for you guys and thought to come visit you while Dante's pouring the milk"
    la "It shouldn't take that long to pour milk..?"
    mc "Oh, you're right , I should go-"
    $ renpy.notify("Laurance enjoys your company!")
    la "No! Stay! Sorry, I didn't mean it like that,"
    hide laurshock
    show laurnorm
    la "So, what's up?"
    mc "Not much, really, just wanted to know how you were doing"
    la "Oh, well, I'm fine, thanks for asking"
    la "Wasn't really doing much, actually. Just sitting around waiting for Garroth"
    mc "Where's Garroth?"
    la "He went out to buy toothpaste, we ran out"
    hide laurnorm
    show laursad
    la "I've been waiting since I wanted to do something.."
    la "I'm really bored.."
    mc "Aw, what a bummer."
    hide laursad
    show laursmile
    la "But I will say, things have been more exciting since you came!"
    la "We've all been eager to get to know you more."
    la "I can say that personally, I've loved every second of talking to you"
    mc "Really..?"
    hide laursmile
    show laurshock
    play sound lauruhh
    la "Not in a weird way, of course!"
    hide laurshock
    show laursad
    la "Sorry, I didn't mean for it to come out like that.."
    mc "You..suck at talking, don't you?"
    hide laursad
    show laurdis
    la "Excuse me?"
    mc "Haha, you just keep saying things that you 'don't mean for it to sound like that'"
    hide laurdis
    show laursmile
    play sound laurlaugh
    la "Hehheh, sorry, I just get kind of nervous talking to new people, I guess."
    d "[mcname]? Where'd you go??"
    mc "Oh, that's my cue, I'll see you around, Laurance."
    jump danmilk
    label travroomawyeah:
    scene travroom with fade
    $ travflag +=1
    $ renpy.notify("Travis enjoys your company!")
    show travnorm with dissolve
    if mcdrink==True:
        t "[mcname]! Hey! You uhh..you feeling better?"
        mc "Yeah, no, I'm fine, yeah"
    if nice==True:
        t "Oh, [mcname], hey again!"
        mc "Hey Travis!"
    else:
        t "[mcname]! Hey!"
        mc "Hey Travis!"
    t "Soo..um"
    hide travnorm
    show travshock
    t "What are you doing in my room randomly?"
    mc "Oh..right, yeah, I came here to borrow some milk, and Dante's grabbing it for me right now, so I just wanted to visit you."
    if nice==True:
        hide travshock
        show travnorm
        t "Ooo, awesome!"
    else:
        hide travshock
        show travflirt
        t "Heh heh...you wanted to see me?"
        mc "Don't"
        hide travflirt
        show travshock
        t "sorry"
    t "So wait, you came to borrow.. milk?"
    t "How do you borrow milk? How does someone use milk and then return it?"
    mc "Like I feel like you know what I mean but you're being obtuse on purpose"
    mc "Anyway, what were you up to?"
    hide travshock
    show travnorm
    t "Not much! Just chilling. I seriously need to pick up a new hobby, I don't have anything to do these days!"
    mc "Ohh I get that feeling, I can never find something to do"
    t "Yeah, but y'know what? I haven't really felt like that since you moved here!"
    t "You're so fresh! Like...there's always something new with you!"
    mc "Well, that's only because you don't know me, ahah"
    t "Yeah yeah, but still! Every day i'm just like, 'man. I wonder when I can talk to [mcname] again. I sure do miss [mcname]!'"
    t "Pretty sure it's the same for everyone else."
    mc "Oh..wow, thank you, Travis"
    t "Seriously, though. We all are very glad to have you here."
    hide travnorm
    show travflirt
    play sound travlaugh
    t "Especially me~~"
    mc "Oohhkay"
    hide travflirt
    show travnorm
    t "Hmm. You know what? I'm gonna ask Laurance if he wants to watch a movie with me"
    if travzandan ==True:
        t "I'm still so....influenced by Killer Babez vs MICHAEL and I think it's time I enter the world of film with him."
    else:
        t "Yesterday, Dante, Zane and I all went to see this movie called Killer Babez vs MICHAEL and it....it really moved me."
        t "Laurance is into all that film stuff so I'd like to enter the world of film with him now."
    mc "Haha, wow. That's awesome."
    t "Care to join us one day for a movie?"
    mc "That sounds great, I'm in!"
    t "Sick!"
    d "[mcname]? Where'd you go??"
    mc "Whoops, that's my cue. I'll see you around Travis!"
    jump danmilk
    label garroomawyeah:
    scene garroom with fade
    "Hmm..looks like Garroth isn't home."
    "He has a pretty nice room...although, I feel bad for being here when he isn't."
    "Who else can I visit?"
    menu:
        "See Dante in the kitchen":
            jump dankitchen
        "Visit Laurance's room":
            jump laurroomawyeah
        "Visit Travis's room" if travnotknow==False:
            if travdrink ==True:
                "You know, Travis is probably still out there at the park..."
                "Who else could I visit?"
                $ travnotknow =True
                jump guyask
            else:
                jump travroomawyeah
    label danmilk:
    scene guyhouse with fade
    show dannorm with dissolve
    d "Here's your milk, hope it's up to your standards!"
    mc "I'm sure it is. Thanks so much!"
    d "Anytime brah!"
    jump milkafter
    label askzane:
    scene zanedoor with fade
    play sound doorbell
    pause (2.0)
    if park==True:
        if zaneagree==True:
            show zanenorm with dissolve
            z "[mcname]? Hey again?"
        else:
            show zanemad with dissolve
            z "Oh. [mcname]...you."
            mc "You're not still mad at me about the My Little Horsies thing are you"
            z "..."
            mc "Come on man it's a kids show it can't be that serious"
            z "Sure.."
            hide zanemad
            show zanenorm
            mc "Anyway-"
    else:
        show zanenorm with dissolve
        z "[mcname]? Hello?"
    mc "I'm sorry to bother you, Zane, but is it okay if I could borrow some milk?"
    $ zaneflag +=1
    $ renpy.notify("Zane appreciates you came to him!")
    z "Oh...sure..come in"
    scene zaneinside with fade
    show zanesad with dissolve
    z "Sorry about the mess, if you had told me you were coming beforehand, I would have cleaned up."
    mc "Zane this is the cleanest house i've ever seen in my life"
    z "Here's the kitchen"
    scene kitchen with fade
    show zanenorm with dissolve
    mc "Hey, we have the same kitchen!"
    z "I'm sure we do."
    z "So, why do you need the milk?"
    mc "I'm sacrificing a virgin tonight"
    z "?"
    mc "JK i'm making cereal lol"
    z "Oh, I thought Lucinda indoctrinated you..."
    z "Wait, cereal? It's noon"
    mc "I may or may have not forgotten to eat breakfast this morning.."
    z "Yeesh, [mcname], that's not good"
    z "You need to be eating your meals on time."
    mc "I know, I know, it was just a slip up.."
    z "Here, a glass of milk. It's a plastic cup so you don't have to worry about returning anything."
    mc "Thanks so much- why is the milk gray"
    z "Hm?"
    mc "The milk. It's gray."
    hide zanenorm
    show zanemad
    z "Ohhh...right.."
    z "A week ago Travis put black food dye in every edible item I own so that it could 'match my soul'"
    z "I got so used to it I forgot."
    menu:
        "That's really funny":
            mc "That is incredibly funny my god"
            z "It really isn't..."
        "I'm so sorry":
            mc "That's so awful, why would he do that?"
            z "He's just a prankster, I suppose..."
    hide zanemad
    show zanenorm
    z "But I assure you, it's safe for consumption."
    mc "Good to hear.."
    mc "Well, I should g-"
    z "Wait, before you go.."
    z "I just want to say..err.."
    z "i'm..WE...are all very glad to have you here."
    z "I may have not been the nicest to you but...it's nice to have a new person around."
    z "So..thanks for being here, [mcname]. I value your prescence"
    mc "Aww..Zane, that's really nice..thank you."
    mc "I'm glad to be here too, it's been really fun hanging out and talking with everyone"
    z "I'm glad to hear that.."
    z "Well...I don't want to keep you. You should go."
    mc "Right..thanks so much, Zane"
    z "You can come anytime if you need help again."
    jump milkafter
    label askaaron:
    $ aarflag +=1
    scene aardoor with fade
    play sound doorbell 
    pause (2.0)
    show aarnorm with dissolve
    ar "Oh, hey [mcname]. What's up?"
    mc "Hi Aaron! Sorry to bother you, but I really need to borrow some milk, is that fine?"
    $ renpy.notify("Aaron appreciates you came to him!")
    play sound aarsure
    ar "Oh, sure, come on in!"
    scene aarinside with fade
    show aarnorm with dissolve
    ar "So, I take it you haven't gotten a chance to grocery shop since you moved here?"
    mc "Uhh...not necessarily.."
    scene kitchen with fade
    show aarnorm with dissolve
    ar "Oh no...I'm running out of milk too.."
    mc "Oh, I can ask someone else-"
    ar "No no, it's fine, just enough to fill a glass for you."
    mc "Ahh, I don't want to take it if you don't have much left.."
    hide aarnorm
    show aarsmile
    ar "I insist, [mcname]. Really."
    mc "Alright..."
    hide aarsmile
    show aarsad
    ar "And since you're here already..."
    ar "I've been meaning to say...well..."
    ar "Things have been really great now that you're here."
    ar "And uhh...we really appreciate that you're taking the time to become friends with us."
    ar "I've struggled a lot in the past with making friends, and socializing, but it feels so much more natural with you, [mcname]."
    ar "We all are really glad, but I wanted to say that personally, I'm really happy you're in our lives now."
    mc "Wow, Aaron...I don't know what to say.."
    ar "S-sorry...that was random..forget I said anything..."
    mc "No, Aaron, that was sweet, really."
    mc "I'm glad to be here too. To have met you...met everyone..it's really great."
    mc "I think I really needed a group as great as this one...you all really have changed me within a matter of days."
    hide aarsad
    show aarsmile
    ar "I'm glad to hear that."
    ar "And hey, if you ever run out of anything again, you can always come by here."
    ar "You can come by for any sort of help, really."
    mc "Thanks Aaron, I'll keep that in mind."
    mc "And thanks for the milk, I'll get going now."
    ar "Have a good night, [mcname]!"
    mc "Goodnight!"
    jump milkafter
label milkafter:
    scene housenoon with fade
    scene houseinsidenoon with fade
    "Ahh...finally got the milk. Now I can enjoy my cereal-"
    play sound crash
    "!!!!" with hpunch
    "What was that????"
    scene housenoon with fade
    "Oh my god...my window broke.."
    "...is that a volleyball?"
    k "Oh my god!! [mcname]!!"
    show katnorm at left
    show nicolesad at right
    with dissolve
    q "Oh my god...."
    k "[mcname], I'm so sorry, me and my friend Nicole were just playing some volleyball and then-"
    k "I may have hit the ball too hard.."
    n "We're really sorry, um, [mcname]."
    n "This is such an awful way to meet.."
    menu:
        "Forgive Katelyn":
            jump katforgive
        "Yell at Katelyn":
            mc "KATELYN. WHAT THE FUCK IS WRONG WITH YOU."
            mc "I HAVEN'T EVEN HAD THIS HOUSE FOR A WEEK YET."
            k "look, I'm really sorry..."
            mc "Leave. I can't even look at you right now."
            k "Yeah..uh...I'll just give you this $200 for the window and uhh.."
            k "Come on, Nicole, let's go.."
            n "We're so sorry..."
            hide katnorm
            hide nicolesad
            with dissolve
            "Cannot believe the audacity of those two."
            jump branchoff
    label katforgive:
    $ katflag +=1
    mc "Hey, Katelyn, it's okay. We all make mistakes"
    hide katnorm
    show katsmile at left
    $ renpy.notify("Katelyn's happy you forgave her!")
    k "Oh, thank you for understanding, [mcname]..."
    k "I'll replace the window, I swear"
    k "Here, I just so happen to have $200 in my pocket, that should be enough"
    mc "Oh wow, thank you, Katelyn."
    hide nicolesad
    show nicolenorm at right
    n "Wow, your friend is so understanding, Katelyn!"
    n "Hi, i'm Nicole, I live not too far from here. It's great to meet you!"
    mc "Great to meet you too!"
    k "Nicole's awesome, I'm sure you guys will get along great."
    n "Right. That's been settled. Shall we go?"
    k "Mhm. Thanks again, [mcname], for understanding. And sorry about the window!"
    mc "No worries! You girls have fun"
label branchoff:
    scene houseinsidenight with fade
    stop music
    play music nightsong loop
    "Man. It's been such a day. I don't even want my cereal anymore. I think I'm just gonna sleep now."
    scene bedroomnight with fade
    "It's only been a couple days...but I really have been enjoying my time here."
    "I feel like I really have gotten close with everyone!"
    if aphflag == 6:
        "Especially with Aphmau..."
    elif katflag == 6:
        "Especially with Katelyn..."
    elif kcflag == 6:
        "Especially with Kawaii-chan..."
    elif luciflag == 6:
        "Especially with Lucinda..."
    elif laurflag == 6:
        "Especially with Laurance..."
    elif garflag == 6:
        "Especially with Garroth..."
    elif danflag == 6:
        "Especially with Dante..."
    elif travflag == 6:
        "Especially with Travis..."
    elif aarflag == 6:
        "Especially with Aaron..."
    elif zaneflag == 6:
        "Especially with Zane..."
    else:
        "No one in particular though..."
    "i'm so excited to see what my future has in store!"
    scene black with fade
    if aphflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump aphroutestart
    elif katflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump katroutestart
    elif kcflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump kcroutestart
    elif luciflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump luciroutestart
    elif laurflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump laurroutestart
    elif garflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump garroutestart
    elif danflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump danroutestart
    elif travflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump travroutestart
    elif aarflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump aarroutestart
    elif zaneflag == 6:
        centered "{color=#fff}End of Act 1.{/color}" with dissolve
        jump zaneroutestart
    else:
        jump badend1
label badend1:
    scene bedroomday with fade
    stop music
    play music daysong2 loop
    "What a bright and beautiful morning!"
    "Nothing can ruin my day!"
    play sound doorbell
    "Now who could that be?"
    scene frontdoorday with fade
    show tylernorm with dissolve
    "..something can ruin my day"
    ty "YOU FAILED! YOU FAAIIILLEEEDDDD!!"
    mc "What??"
    ty "THE TIME OF JUDGEMENT HAS COME AND YOU FAILED!!!"
    mc "What? What are you talking about?"
    ty "Visit Aphmau's house...and you'll understand"
    hide tylernorm with dissolve
    "I seriously have got to do something about this guy."
    "I guess I should go visit [aph] and see what he's talking about...?"
    scene aphdoorday with fade
    "Woah, sounds like she's blasting music in there."
    "Are the girls having a party...?"
    window hide
    play sound doorbell
    pause (3.0)
    "Where is she?"
    window hide
    pause (1.0)
    show aphnorm with dissolve
    a "GUYS! PIZZA'S HE-"
    hide aphnorm
    show aphsad
    a "Oh! [lol]....hey...."
    mc "Hey [aph]...uhhh...what's up?"
    a "Uhh..nothing much...did you need something?"
    mc "..are you throwing a party in there?"
    a "Hm? Well..it's just a little get-together, I guess..."
    show danlaugh at left with dissolve
    d "THIS PARTY IS AWEESOMEEEEEEEE"
    hide danlaugh
    show danmad at left
    d "Oh. [mcname]. Didn't expect to see you here."
    mc "Hey Dante.."
    show danmad:
        xalign 0.0
        linear 0.3 xpos 0.2
    d "Aphmau...I thought we said we weren't inviting [mcname]...?"
    a "I didn't invite them..! It must've been someone else..!"
    show lucinorm at right with dissolve
    lu "Hey guys, what's the holdu-"
    hide lucinorm
    show lucisad at right
    lu "[mcname]! Heeyyyy!"
    mc "You guys were throwing a party without me...?"
    show katnorm at left with dissolve
    k "Guys if i don't stuff pizza into my mouth right now I might die"
    k "[mcname]!?"
    a "Listen...[mcname]..."
    d "None of us really know you like that..sooo..."
    mc "What?? But yesterday...last night...you guys..."
    k "We were just being polite..."
    hide lucisad
    show laurdis at right with new
    la "Oh, [mcname] is here..?"
    mc "I can't believe you guys...I thought we were all becoming friends..."
    k "WE all are friends"
    k "You? Well...you just moved here.."
    mc "..."
    d "Come on guys, let's go back to partying"
    hide danmad
    hide aphsad
    hide katnorm
    hide laurdis
    with dissolve
    "...."
    scene black with dissolve
    "I don't know what to say...I thought we were all friends...I thought they liked me..."
    "After everything they said...that we did together...turns out it was just me who thought things were going good.."
    "Maybe I should have listened to Tyler...maybe I should have been more careful with how I interacted with everyone..."
    "I failed my operation.."
    $ persistent.ending_nobody = True
    centered "{color=#fff}Secret Ending 2: Nobody.{/color}" with dissolve
return