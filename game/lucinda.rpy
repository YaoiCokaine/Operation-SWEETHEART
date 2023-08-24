label luciroutestart:
$ persistent.ending_lucinda_good = False
$ persistent.ending_lucinda_bad = False
$ persistent.ending_lucinda_secret = False
$ persistent.ending_lucinda_lucky = False
scene bedroomday with fade
stop music
play music daysong1 loop
"What a beautiful morning!"
play sound phonecall
"Oh...someone's calling me?"
show luciphonecall with easeinright
lu "Hey, [mcname]! Good morning!"
mc "Oh, good morning Lucinda! How'd you know I just woke up?"
lu "Had a feeling. Y'know, cuz our souls are intertwined~"
mc "W-what!?"
play sound lucilaugh
lu "Haha! I'm just teasing you."
lu "Come on, we're going out"
mc "Huh? Where?"
lu "That's a surprise~"
lu "Just be outside in 5 minutes and I'll come pick you up. Don't keep me waiting~"
play sound hangup
hide luciphonecall with easeoutright
"Hmm..I guess Lucinda and I are hanging out today! Yay!!"
"I wonder...should I dress up nice for her?"
$ bdaysuit = False
$ dressup=False
menu:
    "Dress up nice":
        $ luciflag += 1
        $ dressup =True
        "I'll clean myself up a bit..."
        "What should I wear?"
        label dressup:
        menu:
            "Shirt and pants":
                "A nice shirt and some pants should be good!"
            "Dress":
                "A nice dress should be good!"
            "Birthday suit" if bdaysuit ==False:
                "haha"
                $ bdaysuit =True
                jump dressup
    "Never that serious":
        "Eh. Never that serious."
"Guess I should go and wait outside then!"
scene houseday with fade
"I wonder where Lucinda's gonna take me.."
"Would this count as a date..?"
show lucinorm with dissolve
lu "Hey [mcname]! Hopefully you weren't waiting long?"
mc "Nope! I just came out."
lu "That's good to hear."
if dressup==True:
    $ renpy.notify("Lucinda likes your outfit!")
    hide lucinorm
    show lucismirk
    lu "-And you dressed up! Lookin' good, [mcname]"
    mc "Ahah, thank you!"
mc "So, can I know where we're going now?"
lu "Nope~ just get in the car, you'll have to see once we get there."
mc "This is how people get kidnapped"
scene black with fade
lu "We're almost theeeree~"
lu "oop! We've arrived at our destination!"
lu "Here, come out of the car, but don't open your eyes!"
lu "I wanna surprise you when we get inside~"
mc "Hehe, I'm excited..."
lu "Alright, open your eyes!"
scene grocery_store with fade
show lucinorm with dissolve
lu "We are at the grocery stoooreee!!~"
mc "....the grocery store..?"
"So much for our date..."
lu "Okay, I may have tricked you kind of..."
lu "But I had to go grocery shopping and didn't want to do that alone because, quite frankly, it's boring as fuck"
lu "Soo I thought I would bring you along so we could both have a fun time!"
mc "That..makes sense, I guess."
lu "Great. Now if you see any sales, tell me"
lu "If not...get ready to fill your pockets."
mc "LUCINDA WE'RE NOT STEALING ?"
hide lucinorm
show lucisad
lu "I'm jokingg~ jeez..."
lu "..."
mc "Were you really..?"
show teonynorm at offscreenright
lu "Let's just go find some eggs..."
q "Lucinda??"
mc "?"
show teonynorm at right
show lucisad at left 
with ease
q "Lucinda! Oh my god, it is you!"
hide lucisad
show lucismirk at left
lu "TEONY! Oh my god!"
show lucismirk:
    xalign 0.0
    linear 0.3 xpos 0.25
show teonynorm:
    xalign 0.0
    linear 0.3 xpos 0.3
with ease
"Oh wow they're hugging now"
show lucismirk at left
show teonynorm at right
with ease
lu "I can't believe it, it's been ages!"
te "I know!"
mc "...AHEM..."
lu "Oh, right, [mcname]. This is Teony, an old friend of mine from high school."
lu "Teony, this is my friend [mcname]. They just moved here."
te "Hi! It's nice to meet you!"
mc "..nice to meet you too..."
lu "Wow, what are you even doing here? I thought you moved far away."
te "I'm in town for a bit! I didn't even think i'd bump into any of you guys."
te "Tell me, is everyone else still living here?"
lu "Haha, yes! We all live on the same street, actually"
hide teonynorm
show teonyhappy at right
te "Wow! That's just terrific~!"
mc "yeah guys totally agree"
te "I should get going now, don't want to hold you two."
te "But i'd love for us to do something while I'm in town!"
lu "Yes!! Definitely!"
te "See you around Luci!"
hide teonyhappy with dissolve
show lucismirk at center with ease
"Luci!? I don't even call her Luci!!"
"Who even is this girl..."
lu "Ahhh. Wow. I missed her."
mc "Were you guys close?"
lu "Ehh. Not really. But we were as close as I was with everyone else, so knowing that I'm friends with everyone the way that I am today, it kinda sucks that I couldn't get to know her like that as well."
mc "Right..."
lu "I think I got all my groceries.."
mc "We didn't shop at all?"
lu "Trust"
scene Old_Street with fade
show lucinorm with dissolve
lu "Hey, [mcname], remember how I said I knew some secret spots around this town?"
mc "Mhm?"
lu "Well, there's one I'd like for us to explore.."
lu "There's this creepy forest nearby that no one ever dares to go near."
lu "Me personally, I think it's haunted~"
mc "Sounds fun, I'm in!"
show dansmirk at left with easeinleft
play sound danheybaby
d "Am I hearing talks of fun?"
hide lucinorm
show lucisad
play sound lucisigh
lu "*sigh*.....hello Dante."
d "Hello lovelies, what art thou talking about on this fine occassion?"
mc "What the fuck are you talking about"
hide dansmirk
show danmad at left
d "Sorry. I stole Katelyn's Shakespeare book because I thought that guy would know how to butter someone up."
d "He was probably swimming in ladies back in the day! Girls love that indie stuff."
mc "Dante....Shakespeare was-"
lu "Dante, what do you want?"
d "Woah, can a man not talk to his friends?"
lu "Are we friends?"
d "WHAT. Luci..."
lu "Don't call me that"
d "Look, I was just walking by and overheard you guys."
lu "Well...[mcname] and I were planning on heading to this haunted forest sometime.."
hide danmad
show dannorm at left
d "Ooo! Sounds fun, I'm in!"
lu "Are you sure Dante? It's gonna be scary."
d "I'll be fine! I'm scared of nothin!"
mc "We were thinking this would be..just the two of us..."
d "Come onn, who doesn't love a good threesome?"
lu "Oh my god I think I just popped a blood vessel"
d "Come on Lucinda, please let me come! Please please please!"
d "I have nothing else to do!"
lu "OKAY fine but we're going tomorrow. I've talked to you enough today"
d "Aye aye captain!"
d "Well, I'll see you two around tomorrow. Byeee!"
hide dannorm with dissolve
lu "...so Dante's with us now."
mc "That's okay, I still think it'll be fun!"
hide lucisad
show lucinorm
lu "You're right. As long as we're together, anything will be fun~"
lu "I'm gonna head home now. See you later, [mcname]?"
mc "Sure! See you later!"
hide lucinorm with dissolve
"Hm. I guess I'm on my own now..."
"I'm feeling a little threatened by that Teony girl...what is her goal?"
"No, I'm being paranoid, she's just an old friend. I'm not even dating Lucinda! I have no claim on her..."
"...but I need to make sure she doesn't steal Lucinda away from me.."
"Whatever. What should I do now?"
$ coffeegoing = False
$ homegoing =False
menu:
    "Go home":
        "I feel like going home now..."
        jump homemamatwice
    "Get some coffee":
        "I guess I can head to the CreamyDreamy Coffee Co."
        jump someonecoffeemama
label homemamatwice:
    $ homegoing = True
    scene houseday with fade
    show tylernorm with dissolve
    mc "What th- Tyler? What are you doing infront of my house?"
    ty "Idk I'm bored. Hey did you know your window is broken?"
    mc "Yeah no I know.."
    ty "Right. Can I come in"
    mc "Why?"
    ty "Idk"
    mc "See cuz I'm not gonna let you in"
    ty "PLEASE"
    ty "I don't have any other friends...you're the only person I talk to"
    menu:
        "We are not friends":
            mc "Who told you we were friends"
            ty "Well like...we talk...I give you advice.."
            mc "Shitty advice yea"
            ty "PLEEEEEAAASEE CAN I COME IN PRETTY PLEAASEE PLSPLSPLSPLSPLSPLSPLSPLSPLSPLS PLEASE PLSAAAA"
            mc "OH MY FUCKING GOD YES just stop crying omg"
            ty "Teehee"
        "Of course we're friends":
            mc "Aw, Tyler, of course we're friends!"
            mc "Come on in."
    scene mclivingroom with fade
    show tylernorm with dissolve
    ty "So. How's the move been?"
    mc "I mean, it's been fine...I'm really liking things around here."
    mc "Tyler, do you live on this street?"
    ty "Oh no i'm homeless"
    mc "WHAT"
    ty "yeah no I be doing shit all the time and I was never home so i was like 'hey what if i sold my home' so I did"
    ty "Made bank too. Sold it for $200! You could by a house with that, yknow?"
    mc "Right..."
    mc "I figured you'd be rich considering all the jobs you work.."
    ty "What jobs?"
    mc "Y'know? Like, Pizza delivery...the bowling alley.."
    ty "I don't know what you're talking about"
    mc "See this is why I don't like talking to you"
    mc "Tyler like....what even...are you?"
    ty "Wdym"
    mc "You're different from the others..I don't know how to explain it, but you're just...what are you?"
    ty "[mcname], I think it's best we keep this  relationship strictly professional"
    mc "Oh?"
    ty "I should go now. But before I do,"
    ty "Look out for Teony."
    mc "You know Teony??"
    ty "You two are similar in ways you won't like"
    ty "I'll see myself out. Got bitches to fuck and whatnot"
    mc "Definitely"
    hide tylernorm with dissolve
    "Genuinely we need to kill this guy."
    if coffeegoing ==False:
        "I think I'm in the mood for some coffee after that."
        jump someonecoffeemama
    else:
        jump event1after
label someonecoffeemama:
    $ coffeegoing =True
    scene coffeeshop with fade
    "I haven't actually been here before. I wonder what I should get.."
    g "[mcname]? Is that you?"
    show garnorm with dissolve
    g "[mcname]! Hey!!"
    mc "Oh, Garroth! Nice to see you!"
    g "Were you about to order something?"
    g "Here, the worker gave me an extra French Vanilla for some reason, you can have it!"
    mc "Oh wow, that's convenient"
    g "Sooo...what's up?"
    mc "I mean, not much, i'm just finding stuff to do, I guess."
    mc "Hey, do you know someone named Teony?"
    hide garnorm
    show garshock
    g "Teony? Man, I haven't heard that name in a while."
    g "She was this girl from our highschool, friends with the girls. I never really talked to her, I don't think.."
    g "Why? How do you know Teony?"
    mc "Well, Lucinda and I bumped into her earlier today.."
    hide garshock
    show garnorm
    g "Woaahh, really? I thought she moved away!"
    mc "She's back in town, apparently..."
    g "That's awesome! You should tell the girls about that, they'll be ecstatic to hear Teony's here. It's always fun seeing an old friend!"
    mc "...were Lucinda and Teony close?"
    g "Hmm, not much closer than anyone else, I don't think. They were good friends though"
    g "Oh, you know what? I think Lucinda used to have a crush on her!"
    mc "WHAT"
    g "Yeah, she told us during Truth or Dare once, but she was also drunk....and Lucinda says all kinds of things when she's drunk."
    mc "Mhm..."
    g "What's up with all of these questions?"
    play sound garlaugh
    g "WAIT. I get it now...."
    mc "W-what!? What do you get??"
    g "You're jealous of Teony! Because you LIKE Lucinda~"
    mc "What? No......Whaat? Noo...."
    g "No need to hide it, [mcname]. We all kinda know already"
    mc "What? How??"
    g "It's a bit obvious...we can kinda feel the vibe anytime you're together"
    mc "Wow..."
    g "You don't need to worry about Teony, Lucinda's looong been over her"
    mc "They seemed very close earlier today.."
    g "Then you just have to get even closer!"
    g "Try hanging out with Lucinda more!"
    mc "Hmmm...I guess I'll just have to try that."
    g "Yuppers!"
    mc "I'll get going then. Thanks for the coffee, and this talk, Garroth!"
    g "No problem!"
    if homegoing ==False:
        "Guess I'll just go home now"
        jump homemamatwice
    else:
        jump event1after
label event1after:
    scene houseinsidenoon with fade
    stop music
    play music noonsong loop
    "It's noon already."
    "I can't tell if I'm just waking up super late or if the days are super duper short"
    "I've been asking but I wonder what I could do now?"
    "Oh, I just got a text message from Lucinda..."
    lu "Pull up @ Clover's Bar. Let's have a fun night!"
    "WOOHOOOOOO!! Lucinda wants to hang out!!!"
    "I gotta rush to this Clover's Bar place."
scene cloversbar with fade
show lucinorm with dissolve
lu "Hey [mcname]! Glad you made it!"
show aphnorm at left with dissolve
show lucinorm at right with ease
a "Hi [mcname]!"
mc "Oh, Aphmau, you're here too?"
lu "Mhm! I was gonna bring Teony along, but she was busy, and I found Aphmau, so we went to the bar and I decided you should come too!"
mc "Oh because we can't hang out alone right..."
lu "What was that?"
mc "Nothing let's just drink"
a "Right, so finish your story, Lucinda?"
lu "Mhm, so then me and Teony just chilled out for a while after that. She had to go so we cut our day short"
mc "Wait what is this story about?"
lu "Oh, I was just telling Aphmau that after grocery shopping, Teony and I hung out for a while and caught up"
mc "You guys hung out..."
a "Let's get our drinks!"
show tylerwaiter with dissolve
ty "Hey guys welcome to Clover's what can I get ya"
mc "Good god"
mc "I'll have some alcohol"
ty "You can't just order pure alcohol you need to get an actual drink"
mc "What if I wanted pure alcohol? Then what?"
a "I'll just have a Martini!"
lu "I'll have Clover's Lucky Mix~~"
mc "What's that?"
lu "It's the special. It's a mix of juice, water, alcohol, milk, fanta, gasoline, cough syrup, and bleach. But if you're lucky, they serve you this reaalllyy good margarita"
mc "Genuinely who would even enjoy that"
lu "You don't. It's about the thrill of getting the lucky drink."
lu "Apparently it has some...interesting..effects, but I wouldn't know what they are, I haven't gotten the lucky drink yet."
mc "Uh huh..."
$ clover = False
menu:
    "Get Clover's Lucky Mix":
        $ clover = True
        mc "I'll have Clover's Lucky Mix please!"
        $ luciflag +=1 
        $ renpy.notify("Lucinda's glad you're trying new things!")
        hide lucinorm
        show lucismirk at right
        lu "Atta girl!"
    "Get water":
        mc "I'll just have some water.."
        ty "BOORRRINNGGGGG"
ty "Ok i'll go get all of that for you"
hide tylerwaiter with dissolve
a "I can't believe Teony's back into our lives..I really did miss her!"
lu "It is really awesome!"
menu:
    "So cool":
        mc "Yeah, must be so cool to see an old friend"
        lu "Haha, don't worry [mcname], you're still our beloved newbie."
    "She's not all that":
        mc "She's not all that...let's calm down guys. Shes just someone you knew from school or whatever"
        $ luciflag -= 1
        $ renpy.notify ("Lucinda doesn't like that you said that...")
        hide lucismirk
        hide lucinorm
        show lucisad at right
        lu "Woah, [mcname], that's really rude..."
        mc "Sorry..."
a "Annywaay...so. You guys have any big plans this week?"
hide lucisad
show lucinorm at right
lu "Mm, nothing major. [mcname], Dante, and I were all trying to go to this creepy forest tomorrow."
a "Ooo, sounds fun!"
hide aphnorm
show aphconf at left
a "...with Dante?"
mc "Yeah we didn't really plan for that initially"
show tylerwaiter with dissolve
label leftoff:
if clover ==True:
    ty "Alright, here are your drinks. One martini, and two of Clover's Lucky Mix."
    lu "Alright, let me try this...."
    window hide
    play sound gulp
    hide lucinorm
    show lucisad at right
    lu "...nope. Didn't get lucky.." 
    mc "I guess it's my turn"
    "Let's hope I get lucky!"
    window hide
    play sound gulp
    "..."
    $ result = renpy.random.randint(1, 20)
    if result == 1, 19:
        mc "...nope. No luck."
        lu "Awww, bummer."
        a "Those chances are really low...I don't think many people have actually gotten it!"
        jump drinkcont
    if result == 20:
        play sound wow
        mc "OooooWOW! I AM FEELING LUCCKKKYYYYYY!!!"
        lu "WOOW"
        a "WOOWWW"
        lu "[mcname]....now that i'm looking at you.....you're incredibly hot..."
        mc "Really....???"
        lu "I think i'm in love with you [mcname]."
        lu "MArry me."
        a "This is crazy guys"
        mc "Yes! Of course i'll marry you!"
        ty "What the fuck"
        $ persistent.ending_lucinda_lucky = True
        scene black with fade
        centered "{color=#fff}Secret Ending 3: Lucky!{/color}" with dissolve
        "Wow, you got lucky! 1 in 20 chance!"
        "Would you like to return to where you left off or to the beginning of the game?"
        menu:
            "Where I left off":
                scene cloversbar
                show aphconf at left
                show tylerwaiter
                show lucinorm at right
                with dissolve
                jump leftoff
            "To the beginning":
                return           
label drinkcont:
hide aphconf
show aphnorm at left
a "But I will say, this martini is good!"
ty "Thanks man I tried really hard you see we use this special method called-"
mc "No one asked"
ty "Yeah you're right"
hide tylerwaiter with dissolve
lu "Mm. You know once you have this dumpster mix so many times it starts to tase kind of good"
mc "Yeah no I'm throwing this out"
hide lucinorm
show lucismirk at right
lu "So, guys, let's talk. Is there anyone ~special~ on our minds?"
mc "W-what do you mean by special...?"
lu "You knooowww~~ a crush!"
a "Mmmngmg...~~~ mayhbe,,.."
mc "Is she already drunk"
hide lucismirk
show lucisad at right
lu "Yeah i'm not sure how she manages to do this"
a "Guys....youdiotnt undertsnad....this sint REAL."
a "we aare WARRIORS. we msust defend PHEONIX DROP!"
lu "Aphmau, honey, Pheonix Drop High is fine..."
a "NO! NOT THE SCHOOOLl!!!"
lu "Aphmau we're calling an uber for you"
mc "What is she talking about"
lu "I don't know...Aphmau's been talking about how she 'woke up' and that she's like a divine lord or something?"
a "Lucinda.a.a. you dont know ths. but your a WITCH~~~"
lu "Yes honey I know"
a "YOU'RE THE WHITE WITCH!"
lu "Okay Aphmau I just messaged Aaron to pick you up and he's outside, why don't you go home and rest?"
a "You will understand soon...."
hide aphnorm with dissolve
show lucisad at center with ease
lu "Yea i'm not too sure what's been up with her recently."
mc "She'll figure things out, I'm sure..."
hide lucisad
show lucinorm
lu "You're right"
lu "Let's just enjoy the rest of our night~"
scene black with fade
"We talked and drank some more..."
scene cloversbar with fade
stop music
play music nightsong loop
show lucismirk with dissolve
lu "Hahaaa~! You are a funny one, [mcname]~"
mc "Hehe! Oh, wow, it's getting super late"
hide lucismirk
show lucisad
lu "Shooottt....I guess we should head outt..."
scene housenight with fade
show lucinorm with dissolve
lu "You didn't get super drunk, did you?"
mc "Not reallyy.."
lu "Haha, you've got a nice tolerance, might have to make you my new drinking buddy~"
mc "I'd love to be~"
lu "Say, [mcname], for tomorrow's adventures in the forest, how about we pre-game with a fun scary movie at my house?"
$ lucimovie = False
menu:
    "No":
        mc "Hmm, I don't think so...i'm not a fan of scary movies"
        hide lucinorm
        show lucisad
        lu "Really..?"
        mc "Yeah, I get scared pretty easily."
        lu "...we're exploring a haunted forest tomorrow?"
        lu "Whatever, I'll just watch with Teony, I guess..."
    "Yes":
        $ luciflag +=1
        $ lucimovie = True
        mc "Sure! That sounds super fun"
        hide lucinorm
        show lucismirk
        $ renpy.notify("Lucinda's happy you agreed to watching a movie!")
        play sound lucilaugh
        lu "Awesome! Tomorrow will be so great."
lu "Welp, I'll see you around, [mcname]"
hide lucismirk with dissolve
hide lucisad with dissolve
scene bedroomnight with fade
"I'm super stoked for tomorrow."
if lucimovie == True:
    "I'll get to watch a movie with Lucinda and go into that creepy forest with her too!"
else:
    "We'll be going to that creepy forest!"
"..along with Dante, I guess..."
"I should get a good night's sleep so I'm energized in the morning."
scene black with fade
pause (2.0)
scene bedroomday with fade
stop music
play music daysong2 loop
"Ooo, I feel the energy!"
$ travhang = False
$ kathang =False
$ aarhang =False
if lucimovie== True:
    "I should probably head over to Lucinda's house so we can watch that movie."
else:
    "I should find something to do. Maybe I'll hang out with someone. I wonder who's available right now?"
    menu:
        "Travis":
            $ travhang =True
            "I'll go hang out with Travis!"
        "Katelyn":
            $ kathang =True
            "I'll go hang out with Katelyn!"
        "Aaron":
            $ aarhang =True
            "I'll go hang out with Aaron!"
play sound doorbell
"Huh...looks like someone's here. I wonder who it could be?"
scene frontdoorday with fade
show teonynorm with dissolve
te "Hi! [mcname], it's me, Teony, if you remember."
mc "...how do you know where I live"
te "Lucinda told me.."
mc "Of course she did"
te "May I come in?"
$ teonytalk = False
menu:
    "Yes":
        mc "Y'know what, sure. But we have to make this quick, I have places to be"
        te "Of course!"
        jump teonyinside
    "No":
        mc "Sorry, I've got somewhere to be.."
        hide teonynorm
        show teonysad
        te "Well, this is kinda important-"
        mc "I DON'T GIVE A FUUUCKKKK"
label mermer:
if lucimovie==True:
    jump lucimovieevent
elif travhang ==True:
    jump travnomovie
elif kathang ==True:
    jump katenomovie
elif aarhang==True:
    jump aarnomovie
label teonyinside:
    scene houseinside with fade
    show teonysad with dissolve
    mc "Sooo...what do you want"
    te "Well...I wanted to talk, since....well..I don't know how to say this.."
    mc "Can we hurry this up"
    te "Okay. Well.."
    te "When we met at the grocery store, I really felt some hositility from you...it just feels like you don't like me.."
    te "And Lucinda's been thinking this too, she tells me that whenever she mentions my name, you start acting weird.."
    te "And I just wanted to ask if I did anything wrong...?"
    mc "..."
    menu:
        "It's not your fault":
            label teonytalkyes:
            stop music
            play music sadsong loop
            $ teonytalk = True
            mc "No..it's' not your fault. You didn't do anything wrong. It's just..."
            mc "I'm not used to having to share Lucinda...."
            te "huh..."
            mc "I really like her, and it just feels like you've been stealing her from me...truth is, i'm jealous!"
            te "Oh, [mcname], I don't know how to respond to that.."
            mc "Tell me, Teony, do you like her? Do I need to worry about you?"
            te "Goodness, no! Well, of course I LIKE Lucinda, but nothing more than just as a friend."
            te "I have someone of my own to worry about back at home.."
            mc "Oh!"
            te "I'm sorry I made you feel like I was taking Lucinda away. I assure you, you don't have to worry about me."
            hide teonysad
            show teonyhappy
            te "And you didn't hear this from me, but I think she might like you too~"
            mc "WHAT!? Really??"
            te "Haha! You'll have to ask her yourself."
            mc "Wow...I..."
            mc "I'm so sorry, Teony...I've been so rude to you for no reason..."
            te "It's okay, [mcname]. I get it, you care a lot about Lucinda. I do too"
            te "That's why I really want you two to work out."
            mc "Thank you so much, Teony.."
            te "No problem. I'm glad we talked!"
            hide teonyhappy
            show teonynorm
            te "Well, I need to go now. I'll see you around, hopefully?"
            mc "Yeah, me too!"
            jump mermer
        "Kill her":
            stop music
            play music scarysong2 loop
            menu:
                "Wait, you're kidding, right?":
                    "Oh my god. What was I thinking??"
                    te "You okay, [mcname]?"
                    mc "Yeah yeah...I..."
                    jump teonytalkyes
                "Kill her":
                    menu:
                        "You can't be serious...":
                            "Oh my god. What was I thinking??"
                            te "You okay, [mcname]?"
                            mc "Yeah yeah...I..."
                            jump teonytalkyes
                        "Kill her":
                            menu:
                                "You won't be able to come back from this...":
                                    "Oh my god. What was I thinking??"
                                    te "You okay, [mcname]?"
                                    mc "Yeah yeah...I..."
                                    jump teonytalkyes
                                "Kill her":
                                    menu:
                                        "This is your final chance.":
                                            "Oh my god. What was I thinking??"
                                            te "You okay, [mcname]?"
                                            mc "Yeah yeah...I..."
                                            jump teonytalkyes
                                        "Kill her":
                                            "I can't let her take Lucinda away from me!"
                                            te "[mcname]? What are you gonna do with that comically large frying pan?"
                                            te "Where did you even pull that out of-"
                                            scene black with fade
                                            play sound thud 
                                            te "AAAAAAAAAAAAAAAAAAAAAAAAA" with hpunch
                                            scene houseinsidenoon with fade
                                            "...."
                                            "...what..did I do..."
                                            show laurshock at left with easeinleft
                                            la "[mcname!u]! I was walking by and I heard a scream, and your door was open, what hap-"
                                            la "...Teony..?"
                                            mc "Laurance...this isn't what you think..."
                                            la "You're...holding a comically large frying pan..."
                                            mc "..okay yeah but like"
                                            la "How could you..."
                                            la "YOU MONSTER!!!" with hpunch
                                            hide laurshock with easeoutleft
                                            mc "LAURANCE! WAIT!"
                                            "Oh my god....he's gonna tell everyone..."
                                            "He's gonna tell everyone I'm a murderer..."
                                            "Why..why did I do that..??"
                                            "Lucinda will never love me now..."
                                            $ persistent.ending_lucinda_secret = True
                                            centered "{color=#fff}Secret Ending 4: Envy.{/color}" with dissolve
                                            return
label lucimovieevent:
    stop music
    play music daysong2 loop
    scene aardoorday with fade
    play sound doorbell
    pause (1.5)
    show lucinorm with dissolve
    lu "Heyyy! Come on in."
    scene luciroom with fade
    show lucinorm with dissolve
    mc "Haha, I'm getting flashbacks to when I tried your potion..."
    hide lucinorm
    show lucisad with dissolve
    lu "I really am sorry about that..."
    mc "It's okay! Let's just watch the movie."
    hide lucisad
    show lucinorm
    lu "Alright!"
    lu "So, this is actually a trilogy, called Final Girl Vs. MICHAEL"
    mc "Ohh, like..Michael Myers?"
    lu "Nope! Just MICHAEL."
    mc "Right.."
    lu "Apparently it's suuupeer spooky. You ready?"
    mc "Ready as I'll ever be!"
    scene black with fade
    "We finished the trilogy.."
    scene luciroom with fade
    stop music
    play music noonsong loop
    show lucismirk with dissolve
    lu "Woah! That was creepy."
    lu "I was a bit confused during the 3rd movie...it turns out that Final Girl is a long lost 'Killer Babe'?  What does that even mean?"
    lu "We still have some time before we should head out to the forest, anything you wanna talk about?"
    menu:
        "Talk about love":
            mc "Let's talk about love!"
            lu "Ooo, interesting topic."
            lu "What about love?"
            mc "Mmm..do you have a crush on anyone..?"
            lu "Hey, weren't we talking about this at the bar yesterday?"
            mc "We were...before Aphmau got drunk."
            hide lucismirk
            show lucisad
            lu "Right..."
            hide lucisad
            show lucinorm
            lu "Well....maybe I do...maybe I don't.."
            lu "There is definitely a person I know that's catching my eye~"
            "Is she talking about me? Or Teony...?"
            lu "What about you? Do you have anyone you like?"
            menu:
                "Yes":
                    $ luciflag +=1
                    mc "Haha...maybee..."
                    mc "There is someone I like more than others.."
                    $ renpy.notify("Lucinda's glad she has a chance with you!")
                    lu "Interesting...good to know."
                "No":
                    mc "No, don't think so."
                    lu "Oh...um. Alright.."
        "Talk about witchcraft":
            mc "Let's talk about witchcraft!"
            lu "Ooo! You know how I love my witchcraft."
            mc "Soo..how did you get into all that?"
            lu "Well, it was just something I was really into when I was younger."
            lu "I spent a lot of time practicing my spells and potions"
            mc "What do you use them for?"
            lu "Oh, nothing crazy. Just like, world domination, whatever,"
            lu "Hah! Just kidding. Yeah, I don't really do anything absurd."
            lu "Say, how would you like to learn some stuff under me?"
            menu:
                "Yes":
                    $ luciflag +=1
                    mc "I'd love to!"
                    hide lucinorm
                    show lucismirk
                    $ renpy.notify("Lucinda's excited to teach you!")
                    lu "Awesome! I'll be the greatest teacher ever, who knows, maybe you'll be naturally gifted?"
                    mc "We'll have to see~"
                "No":
                    mc "Oh fuck no I hate witchcraft"
                    lu "oh"
                    lu "Well, you were the one that wanted to talk about it..."
        "Talk about Teony":
            mc "Let's talk about Teony!"
            lu "Oh, Teony! She's so awesome."
            lu "I've really been catching up with her, I still really can't believe that she's here."
            mc "Uh huh..."
            lu "She is super nice! Man, I really wish she came with all of us when we moved here...but I guess she's living her own life."
            lu "Why are you asking about her?"
            menu:
                "I like her":
                    mc "I just think she's cool! We haven't talked much..but if she's a friend of yours, she's a friend of mine."
                    if teonytalk == False:
                        "Knowin i was frontin"
                    $ luciflag +=1 
                    $ renpy.notify("Lucinda's glad you like Teony!")
                    lu "She is great! I really think you'd guys would get along."
                    lu "I'd love it for my girls to be friends~"
                    "Hehe...I am her girl..."
                "I don't mind her":
                    mc "Just wanted to know. She's fine...I guess, I don't mind her."
                    hide lucismirk
                    show lucinorm
                    lu "...right."
                    lu "You always act weird when we talk about Teony.."
                    mc "..."
    lu "Anyway, I think this is a good time to head to that forest."
    lu "I told Dante where to go, he might be waiting there for us. Come on"
    jump forestbitch
label travnomovie:
    if teonytalk ==True:
        stop music
        play music daysong2 loop
    scene travroom with fade
    show travnorm with dissolve
    t "[mcname]! What's good?"
    mc "Hi Travis! What are you up to?"
    t "Nothing. I'm just planning how I'm gonna ask Katelyn out this week"
    mc "Oh? I didn't know you liked Katelyn!"
    t "Ya, I'm trying to optimize this ask-out. Everytime I try to ask her to go on a date, she always get's angry!"
    hide travnorm
    show travsad
    t "Makes me wonder...what is the common factor between everytime I've asked her out?"
    "Oh he doesn't know..."
    t "I've tried extravagant proposals and simple ones too. None of them seem to work, though."
    t "I even turned to Dante for advice, but he just said that I need to make myself more attractive for her."
    hide travsad
    show travflirt
    t "But, and I don't know if you know this, I'm already incredibly attractive! How does one get any hotter than this?"
    t "It's like saying the sun isn't warm enough, that's just not true"
    hide travflirt
    show travnorm
    mc "Right."
    t "[mcname], tell me, what do you think I should do?"
    menu:
        "Katelyn is not interested":
            mc "Travis, I don't know how to tell you this, but YOU'RE the common factor"
            hide travflirt
            show travshock
            t "Huh? What's that supposed to mean"
            mc "It means she does not like you AT ALL. There is nothing you could do that would make her agree to going out with you"
            t "...okay What would you know?? You don't know Katelyn like I do!"
            mc "No but Travis I can assure you on this"
            t "..."
            hide travshock
            show travsad
            play sound travcry
            t "WHYYYYYYYYYYYYYY. WHYY WON'T SHE LOVE MEEEEEEEE" with hpunch
            "Oh my god he's crying"
            mc "It's okay Travis! There are other people out there for you! I'm sure!"
            play sound travcry
            t "BUT I NEED KATELYYYNNNNNNN"
            mc "It's okay Travis you'll be fine"
            t "...*sniff*..*sniff*...."
        "Play hard to get":
            mc "You should try playing hard to get!"
            t "...keep going.."
            mc "What you need to do is get a partner, and make sure Katelyn knows about it, because she'll be super jealous!"
            t "Woah, you think that'd really work??"
            mc "Uh huh! I think she just doesn't realize how awesome you are, but she will once she sees you're in high demand.."
            t "Wow! You're right! That's an awesome plan.."
            t "You're quite the advice-giver, [mcname]! You give Dante a run for his money!"
            mc "Trust me. Katelyn won't stop thinking about you once she sees you're taken"
            t "Definitely. Now, where would I find someone willing to date me short-term..."
            hide travnorm
            show travflirt
            t "...I don't suppose you-"
            mc "no"
            hide travflirt
            show travshock
            t "Uh huh yeah I can respect that"
            hide travshock
            show travnorm
            t "You know what? Teony's back in town for a bit, I think I'll ask her to go out with me!"
            mc "That...works perfectly actually yeah I think you should try that"
            t "Thanks for your advice, [mcname]. You could start a business like this"
            mc "I don't think I will no"
    show lucitxt2 with easeinbottom
    "Whoops, looks like it's forest time.."
    mc "I gotta go, Travis. Let's talk again sometime."
    jump forestbitch
label katenomovie:
    if teonytalk==True:
        stop music
        play music daysong2 loop
    scene katroom with fade
    show katnorm with dissolve
    k "Oh, [mcname], hi. What's up?"
    mc "Hi Katelyn! What are you up to?"
    k "Ummm....it's nothing..."
    mc "Sounds like something's bothering you...everything okay?"
    k "Well..."
    k "You know Travis, right?"
    mc "Sometimes I wish I didn't"
    k "It's just..."
    k "He keeps asking me out and isn't getting the hint that I do not want him at all."
    mc "Can you not just tell him that you're not into him?"
    k "I've tried, but then he does this thing where he get's super sad and I feel bad.."
    mc "Has he been harrassing you??"
    k "No, not harrassment...it's just..I think he thinks I'm trying to play hard to get when really I just do not want this guy"
    mc "Hmm, that does sound pretty annoying.."
    k "It really is! I don't know how to hit it home for him that I don't like him that way without hurting his feelings."
    k "He's still my friend...somewhat.."
    k "You have any idea what I could do?"
    menu:
        "Be honest with him":
            mc "Katelyn, the best thing you can do is just be honest with him. Even if it hurts his feelings..."
            k "How would I even go about doing that?"
            mc "Well, I guess just...talk to him?"
            mc "Let him know that you're flattered but you only see him as a friend"
            mc "He'll be hurt for a bit, but it's better than him consistently thinking he has a shot with you."
            k "..."
            hide katnorm
            show katsmile
            k "You're right. I should just talk to him. Can't be that hard, right?"
            mc "Right!"
            k "I just hope we can continue being friends after. I'd hate to completely lose him over something stupid.."
            mc "Don't worry, he cares about you a lot, obviously. You won't lose him"
            k "Thanks, [mcname]"
            play sound katlaugh
            k "You're really good at giving advice, y'know? Hah! Maybe I could stop seeing my therapist now that you're here.."
            mc "No I really don't think you should do that"
        "Pity date him":
            mc "I think you're only option is to give in..."
            hide katnorm
            show katdis
            k "...really?"
            mc "You should date him out of pity, I think."
            mc "Just so that like...y'know....you don't hurt his feelings."
            k "..then what about me?"
            mc "...idk, suck it up?"
            hide katdis
            show katmad
            k "I'm not just gonna 'suck it up'!"
            mc "Well shit what do you wanna do"
            hide katmad
            show katdis
            k "Well, definitely not what you tell me, you suck with advice."
            mc "It's not that bad of an idea! Just pretend you like him, then break it off after a week."
            k "That's...that's awful."
            mc "Is it really?"
            k "YES yes it is. I don't want to hurt Travis.."
            mc "I mean hey it's your funeral"
            k "Genuinely you should never give anyone advice ever again like"
            mc "And you'll think back on this when you're 50 years old and Travis is still bothering you..."
            t "[mcname] I think you should go"
    show lucitxt2 with easeinbottom
    "Whoops, looks like it's forest time.."
    mc "Well, I gotta go, see ya around, Katelyn!"
    jump forestbitch
label aarnomovie:
    if teonytalk==True:
        stop music
        play music daysong2 loop
    scene aaroom with fade
    show aarnorm with dissolve
    ar "[mcname]? How'd you get into my house?"
    mc "Don't worry about it"
    play sound aarsure
    ar "Okay um. What's up?"
    mc "Just wanted to see what you were up to! I need to kill some time"
    ar "Ohhh...well, i'm just pondering.."
    mc "What are you thinking about?" 
    hide aarnorm
    show aarsad
    ar "Well...I'm just...a bit worried for Aphmau."
    ar "I'm not sure if you know, but she's been acting weird recently."
    ar "She keeps talking about how 'everything is fake'? That this world we're in isn't real and that we need to 'wake up'?"
    mc "Yeah I've seen it.."
    ar "Something about how i'm the Lord of Falcon Claw???"
    mc "What is Falcon Claw?"
    ar "It's the university we went to, I just...I don't know what she's talking about!"
    ar "And she seems very frantic too. She's just been acting very different."
    mc "That is really weird, I just assumed that was normal for her..."
    ar "No, it only started recently..."
    ar "I don't know what to do. Should I say something?"
    menu:
        "Leave her alone":
            mc "I think it's best if we just leave her alone for now..."
            ar "Really?"
            mc "I'm sure she'll go back to normal soon enough."
            mc "Maybe she's like, got something going on, we wouldn't want to bombard her during a hard time, y'know?"
            ar "You're right...I don't want to hurt Aphmau. I'm just worried, we all are, really"
            mc "I usually am right yea"
        "Confront Her":
            mc "I think you should confront and check in on her..."
            mc "If she's going through something, it's best that you're able to be there for her and show her she has people that care."
            ar "Yeah...that's what I was thinking.."
            mc "And you two are close, right? I'm sure she'll listen and talk to you"
            hide aarsad
            show aarsmile
            ar "You're right. Aphmau is one of my closest friends, I don't know why I'm so scared to talk to her."
    hide aarsad
    hide aarsmile
    show aarshock
    ar "But seriously, what could have caused this?"
    mc "Maybe it's her evil twin!"
    hide aarshock
    show aarmad
    ar "This isn't the time to joke..."
    hide aarmad
    show aarshock
    ar "It's weird, I know it's Aphmau, but it feels like...a different Aphmau. She talks like she's from another universe or something."
    ar "She keep's telling me to 'remember it all'. She's just been so weird around everyone!"
    show lucitxt2 with easeinbottom
    "Whoops, looks like it's forest time.."
    mc "I'd love to talk about this, Aaron, but I gotta go now. Good luck with Aphmau!"
    jump forestbitch
label forestbitch:
stop music
play music noonsong loop
if lucimovie ==True:
    scene darkforest with fade
    show danmad with dissolve
    show lucinorm at left with dissolve
    lu "We're heeerre~!"
else:
    scene darkforest with fade
    show danmad
    show lucinorm at left
    with dissolve
    lu "There you are, [mcname]"
d "Final-fucking-ly! I've been waiting here all day!"
mc "Oh, don't be dramatic"
d "no like I've literally been here since morning I had nothing to do"
mc "Oh wow I don't know what to say about that"
lu "Okay, now that we're all here, can we go in?"
hide danmad
show dannorm
d "Alright! Let's do this!"
scene darkforest2 with fade
stop music
play music eeriesong loop
show lucismirk with dissolve
lu "Wooahh...I'm already feeling the spirits..."
show danmad at left with dissolve
d "ARE YOU JOKING ?"
lu "Uhh...I guess?"
d "Right. Yeah cuz ghosts arent real right ahaha"
lu "Okay Dante"
mc "This place IS really creepy though.."
lu "But that's what's so cool about it!"
lu "So..you guys think we'll find anything creepy? Like a dead body or something...?"
d "Guys I think I just shit my pants"
mc "Oh my god Dante what the fuck"
d "I'm sorry guys I've never done this before"
hide lucismirk
show lucisad
lu "it's okay, Dante..let's just keep looking."
lu "And stay at least 6ft away from us two."
d "Uh huh.."
mc "Wait! Guys, I found something.."
mc "It's a letter!"
lu "Let me see?"
scene luci_forest_cg with fade
pause (2.0)
lu "The writing is a bit messy, like it was rushed..."
lu "This also looks like it was written with dirt? Or mud?"
mc "What does it say?"
d "Lucinda if you start speaking Latin I'm getting the fuck out of here"
lu "calm down Dante. Let's see.."
lu "It just says 'I cannot run' over and over again..."
d "Oohhmmy god we're gonna die"
mc "No one's dying, Dante!"
scene darkforest2 with fade
show lucismirk with dissolve
lu "[mcname], should we take this letter with us?"
menu:
    "Yes":
        mc "Absolutely! It's super cool!"
        $ luciflag +=1
        $ renpy.notify("Lucinda likes that you think it's cool!")
        lu "Exactly! I knew you'd get me."
    "No":
        mc "Absolutely not, thats either haunted or covered in STD's or both"
        hide lucismirk
        show lucisad
        lu "Ugh. You're boringg."
play sound wail
window hide
pause 
show danscare at left with dissolve
play sound dancry
d "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" with hpunch
hide lucismirk
hide lucisad
show lucinorm
lu "Dante! Why are you screaming!"
d "DID YOU NOT HEAR THAT??"
play sound wail
window hide
pause
d "OH MY FUCKING GOD WE'RE GONNA DIE"
d "I'M GONNA DIE WITHOUT TASTING PUUSSYYYYYYY"
mc "DANTE! NO ONE'S DYING!"
hide lucinorm
show lucievil
lu "Let's follow that sound!"
d "NOoOoOooOOoOOOoOoOOOO"
scene black with dissolve
lu "It sounded like it was coming from here?"
mc "Is this a good idea...?"
d "Guys the pee is trickling down my pants right now"
lu "Dante we're gonna leave you here"
play sound wail
mc "Hold on...I think I hear it here..behind this tree..."
scene garrancetree with fade
mc "GARROTH!? LAURANCE!?"
g "Errrr....Nope! You're hallucinating"
lu "I don't think we are?"
g "You're dreaming! This is a dream!"
la "Garroth...drop it..."
scene darkforest3 with fade
show garsad:
    xalign 0.0
    xpos 0.25 ypos 60
show laursad:
    xpos 0.4 ypos 60
with dissolve
g "Well...erm...this is awkward..."
show danmad at left with dissolve
d "Dude! Garroth! You told me you were busy today because of a date!"
show lucisad at right with dissolve
lu "Dante, I don't think he was lying about that..."
play sound danhuh
d "Huh..?"
d "OHhhhh"
la "Yeahh.."
d "...actually i'm not shocked at all honestly"
lu "Yeah now that I'm thinking about it this was kind of expected"
hide laursad
show laurshock:
    xpos 0.4 ypos 60
hide garsad
show garshock:
    xalign 0.0
    xpos 0.25 ypos 60
la "Wait, what?"
mc "Yeah no I'm seeing it now yea"
lu "Well like...you two are inseperable like we could tell"
d "Hey man I've been shipping you guys for a while now actually"
g "Wait, so you guys knew!?!"
mc "Well like...I guess we kind of just figured..."
play sound lauruhh
la "Wow. Uhh. Then yeah me and Garroth are dating I guess"
g "You guys don't care?"
hide danmad
show dannorm at left
d "Come on, why would we care?"
hide lucisad
show lucinorm at right
lu "Seriously why would I"
hide garshock
show garshock:
    xalign 0.0
    xpos 0.25 ypos 60