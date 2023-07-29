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
    scene frontdoor with fade
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
            $ aphparty += 1
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
    scene bedroom with fade
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
    $ gardanflag += 1
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
    $ kcconvflag += 1
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
    if aphparty == 1:
        "I guess I should call Aphmau to discuss some stuff...I hope she isn't busy!"
        "It.s dialing...."
        a "Hello?"
        mc "Hi Aphmau! I was just calling because I wanted to talk about the party"
        a "Ooo, that's right! You don't have to worry at all about decorations and inviting people, I've got that completely covered! You just think about the food and drinks"
        mc "Oh, alright then! Thanks for everything!"
        a "Anytime! Now, I've gotta get back to what I was doing. I'll pop by tomorrow afternoon to help set up! Bye byeee!"
        "Glad to know she's got all of that taken care of"
        play sound doorbell
        "Food and drinks...I could make some pasta for everyone!"
    else:
        "How do you even organize a housewarming party? I guess I could cook some food for everyone.."
        "Hopefully pasta works..."
        "I can't wait to meet everyone. It seems like Aphmau will tell all her friends to come over, so maybe I can make some new friends too!"
        play sound doorbell
        "Right, I also need to look for a job here...that's gonna be tough..."
    "Oh wow, the pizza is already here!"
    scene frontdoornight with fade
# TODO: tyler sprite
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
    mc "Can you just leave"
    ty "ok"
    hide tylerpizza with dissolve 
    "What an....interesting delivery guy."
    "And it's already dark out! I guess I should get some sleep now."
    scene bedroomnight with fade
    "Hopefully the party goes well tomorrow..."
    scene black with fade
    scene bedroom with fade
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
    pause(3.0)
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
    la "My name is Laurence, by the way."
    mc "I'm [mcname]...thanks for helping me up"
    if gardanflag == 1: 
        mc "Wait a second, Laurence..I live across you!"
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
    if aphparty == 1:
        jump aphpartyplan
    else:
        jump partyplan
    label aphpartyplan:
    scene houseinside with fade
    play sound doorbell
    "Aphmau should be coming soon to help out with the party-"
    "Oop! That's her!"
    scene frontdoor with fade
    show aphnorm with dissolve
    a "I brought decorations!"
    mc "Woah! That's quite a few!"
    a "Of course! Every great party needs great decorations"
    scene aphmau_party_cg with fade
    pause (3.0)
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
    scene frontdoor with fade
    if aphparty < 1:
        show aphnorm with dissolve
        a "Hi [mcname]!! I brought everyone that I could!"
        mc "That's great! Thanks so much"
        a "No problem! I got you this cool scented candle as a gift. I hope you like it!"
        mc "It's lovely, thank you"
        hide aphnorm with dissolve 
    show katnorm at left with dissolve
    show kcnorm at right with dissolve
    if kcconvflag == 1:
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
    else:
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
    if gardanflag:
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
    mc "Right! You're with Laurence and those guys!"
    t "Yeah..! Sorry...I ran here..."
    mc "What were you doing before you got here?"
    t "Suckin cock"
    mc "Oh"
    play sound travlaugh
    t "Haha jk. Just had some business"
    mc "..right. Come on in, we've got everyone"
    if aphparty == 1:
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
                    define b = Character("Both")
                    b "AAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!"
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
    if aphparty == 1:
        scene houseinsidedecornoon with fade
    else:
        scene houseinsidenoon with fade
    "Seems like everyone's broken off into their own groups...who should I join?"
    menu:
        "Aphmau, Kawaii-chan":
            jump aphchanconv
        "Lucinda, Katelyn":
            jump lucikatconv
        "Laurence, Garroth, Aaron":
            jump laurgaraarconv
        "Travis, Zane, Dante":
            jump travzandanconv
    label aphchanconv:
        $ renpy.notify("Aphmau and Kawaii-chan are glad to talk to you!")
        $ aphflag += 1
        $ kcflag += 1
        define aphchan = 0
        $ aphchan +=1
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
        define lucikat = 0
        $ lucikat +=1
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
        $ renpy.notify("Laurence, Garroth, and Aaron are glad to talk to you!")
        "Let's see with Laurence, Garroth, and Aaron are up to!"
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
                define laurrest = 0
                $ laurrest +=1
                $ laurflag += 1
                mc "I think Piping Hot Pizza Palace sounds the best, I love me a good pizza!"
                hide laurdis
                show laursmile
                $ renpy.notify("Laurence is glad you like his suggestion!")
                play sound laurexactly
                la "It's so good! You're gonna love it, [mcname]."
                la "We should go tomorrow, you'll see just how great it is."
                mc "Looking forward to it!"
                g "Whatever...who want's piping hot pizza or sizzling sausages in this weather? A nice, cool ice-cream is perfect.."
            "Sizzling Sausage Shack sounds the best":
                define aarrest = 0
                $ aarrest +=1
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
                define garrest = 0
                $ garrest +=1
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
        define travzandan = 0
        $ travzandan += 1
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
        define e = Character("Everyone")
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
if aphparty == 1:
    "And I finally got all of these decorations down..."
"Man, i'm so tired!"
"But i'm really looking forward to tomorrow!"
if aphchan == 1:
    "I can't wait to hang out with Aphmau and Kawaii-Chan. Hopefully I can get to know them better!"
    "Also looking forward to using Lucinda's gift card, apparently the CreamyDreamy coffee is spectacular."
if lucikat == 1:
    "I can't wait to go bowling with Katelyn and Lucinda!"
    "Or well...I guess I'm not bowling, i'm just watching them bowl...but that'll probably be fun, too!"
if laurrest ==1:
    "I can't wait to go to Piping Hot Pizza Palace with Laurence! It sounds soooo good..."
    "It'll also be great to spend some time with Laurence and get to know him more!"
if aarrest ==1:
    "I can't wait to go to Sizzling Sausage Shack with Aaron! It sounds soooo good..."
    "It'll also be great to spend some time with Aaron and get to know him more!"  
if garrest ==1:
    "I can't wait to go to Cloud 9 Nice Ice Cream Parlour with Garroth! It sounds soooo good..."
    "It'll also be great to spend some time with Garroth and get to know him more!" 
if travzandan == 1:
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
mc "...right. Definitely"
ty "I'm just saying, if you really want to be with your one person, then really dedicate yourself to that one person. If you mess around..you might get an ending you're not happy with"
mc "an 'ending'? What is that supposed to mean?"
ty "You will learn as time goes on"
mc "Hey man don't you have pizzas to deliver"
label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass
ty "Farewell, [currentuser]"
mc "??? who is [currentuser]???"
hide tylernorm with dissolve
"Jesus christ that guy is weird"
scene Bedroom_Night_Dark with fade
"I need to go to sleep now"
"That guy was...really creepy...but maybe he's right"
"I can't be fooling around too much...I should be careful with how I progress from here"
scene black with fade
pause (3.0)
scene Bedroom_Day with fade
"*yaawn* What a beautiful morning!"
if aphchan == 1:
    "I should probably get ready to get coffee with Aphmau and Kawaii-chan."
if lucikat == 1:
    "I should probably get ready to go bowling with Lucinda and Katelyn."
if laurrest ==1:
    "I should probably get ready to go to Piping Hot Pizza Palace with Laurence."
if aarrest ==1:
    "I should probably get ready to go to Sizzling Sausage Shack with Aaron." 
if garrest ==1:
    "I should probably get ready to go to Cloud 9 Nice Ice Cream Parlour."
if travzandan == 1:
    "I should probably get ready to go watch Killer Babez VS MICHAEL with the guys."
"Hmm..I wonder if I should dress up nicely?"
menu:
    "Dress up nicely":
        define dressup = 0
        $ dressup += 1
        "I'll make a good impression if I put some effort into my look."
    "Don't":
        "Eh, it's not a big deal, a shirt and sweatpants should probably be fine."
if aphchan == 1:
    jump aphchancoffee
if lucikat == 1:
    jump lucikatbowl
if laurrest ==1:
    jump laurpizza
if aarrest ==1:
    jump aarsausage
if garrest ==1:
    jump garcream
if travzandan == 1:
    jump guymovie
label aphchancoffee:
    scene houseday with fade
    mc "I guess I should just wait out here"



return
