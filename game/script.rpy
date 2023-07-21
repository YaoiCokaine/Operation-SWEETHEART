label start:

    $ mcname = renpy.input("What is your name?")
    scene street with fade
    play music track1 loop
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
    play voice aphperf
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
            play voice aphperf
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
            play voice aphcry
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
    play voice garsigh
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
            d "Dude. Whatever."
            d "I never said I WILL pay...just...later"
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
    play music track19
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
    play music track4
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
    play music track6
    pause(3.0)
    q "Are you alright?"
    q "Do you need help getting up?"
    mc "Oh...I...uhh....yeas...."
    scene laur_grocery_cg_2 with dissolve
    q "Ha ha! Here, take my hand"
    scene grocerystore with fade
    show laurnorm with dissolve
    stop music
    play music track4
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
    la "I need to get going, I still have to get you a gift ahaha"
    mc "Oh, you don't need to worry about a gift-"
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
    "Aphmau should be coming soon to help out with the party-"
    play sound doorbell
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
    "I'm really excited to meet everyone!"
    play sound doorbell
    "Oh, that's them...I'm so nervous!"
    scene frontdoor with fade
    if aphparty < 1:
        show aphnorm
        a "Hi [mcname]!! I brought everyone that I could!"
        mc "That's great! Thanks so much"
        a "No problem! I got you this cool scented candle as a gift. I hope you like it!"
        mc "It's lovely, thank you"
        hide aphnorm with dissolve 
    show katnorm with dissolve
    k "Hi. You're [mcname], right?"
    mc "I'd be concerned if I wasn't!"
    k "...haha?"
    k "Anyway. I'm one of Aphmau's roommates. I brought you this bottle of wine, as a gift"
    mc "Ooo, cool! I'm not a big wine person but-"
    k "Okay? I'll just keep it then"
    mc "...okay"
    hide katnorm with dissolve
    show kcnorm with dissolve
    if kcconvflag == 1:
        kc "Good evening [mcname]-san!!"
        mc "Hey Kawaii-chan!"
        kc "Kawaii-chan was very excited for your party. She brought the cookies from yesterday since [mcname]-san liked them so much!"
        mc "Oh wow, that's great! Thanks so much! Everyone's gonna love these"
        

    return
