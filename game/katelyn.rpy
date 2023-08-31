label katroutestart:
$ persistent.ending_katelyn_good = False
$ persistent.ending_katelyn_bad = False
$ persistent.ending_katelyn_secret = False
scene bedroomday with fade
stop music
play music daysong1 loop
"What a beautiful morning!"
play sound phonecall
"Oh...someone's calling me?"
show katphonecall with easeinright
k "[mcname]! You busy today?"
mc "Oh, Katelyn! Hey! Not really, I was just gonna-"
k "Forget about it! You're coming over"
mc "Huh? Did something happen?"
k "Nope. Just wanna hang out, that's all"
mc "Oh! Alright, I'm coming over!"
play sound hangup
hide katphonecall with easeoutright
"Looks like I'm hanging out with Katelyn today! Awesome!"
"I should head over right now."
scene aphdoor with fade
play sound doorbell
pause (1.0)
show katnorm with dissolve
k "Awesome! You're here! Come on in."
scene katroom with fade
show katsmile with dissolve
mc "Soo..any specific reason I'm here?"
k "Nope. Just wanted to hang. What, is that illegal?"
mc "No! No no. I'm perfectly fine with this, just curious"
k "Great, well, I-"
play sound phonecall
k "Oh, sorry, gotta take this"
hide katsmile with easeoutright
"Huh. Guess it's just me in here.."
"Man. Katelyn has a really nice room. I shouldn't snoop around, though. That's not nice.."
show katsmile at center with easeinright
k "[mcname!u]! [mcname!u]! OH MY GOD!!"
mc "WHAT? WHAT?"
k "Okay, so, 2 weeks ago, I was the lead role for this musical, and apparently, there was a talent agent in the audience!"
k "She said she loved my work and is considering scouting me!"
mc "OH MY GOD! Katelyn, that's awesome!!"
k "Yes! Oh my god, I worked so hard for this, they're saying we're gonna perform it again soon in a much bigger venue!!"
mc "Seriously, Katelyn, I'm so happy for you! What's the play about?"
k "It's a musical adaptation of the Midnight saga!"
mc "Do you mean Twilight..?"
k "Nope, Midnight."
k "But I can't believe it, I might get scouted!"
mc "That's so awesome, Katelyn! Y'know what? We should go out to dinner tonight to celebrate!"
k "That sounds fun! Just us two?"
$ katdine =False
menu:
    "Just us two":
        $ katdine =True
        mc "Just us two! It's my treat to you."
        $ katflag +=1
        $ renpy.notify("Katelyn's excited to dine alone!")
        k "Awesome. Wow! I just can't believe it!"
    "We'll invite others":
        mc "Um..we can invite the girls too! Aphmau, Lucinda, Kawaii-chan, maybe your friend Nicole?"
        hide katsmile
        show katnorm
        k "Oh, sure..we can do that.."
k "Hold, give me a second, I need to go call my dad and tell him."
hide katnorm with easeoutright
hide katsmile with easeoutright
"I'm so happy for Katelyn! This is an amazing opportunity for her! I just wish I could've seen a performance of hers.."
"Wait...if they're performing it again, maybe I can come see it..?"
"I'd love to be able to support Katelyn and see her art."
show katnorm with easeinright
k "Just told my dad, he's estatic!"
k "Come on, I think Aphmau and Kawaii-chan are home now. Let's go tell them!"
scene aphhouse with fade
show aphnorm at left with dissolve
a "Lucinda's magic is strong, Kawaii-chan, but yours is just as good! No need for rivalry!"
show kcconf at right with Dissolve
kc "Kawaii-chan doesn't quite understand but...thank you?"
show katsmile with dissolve
mc "Aphmau! Kawaii-chan! Guess what!"
hide kcconf
show kcnorm at right
kc "[mcname]-san! Hi! What's going on?"
k "A talent agent watched my peformance in Midnight, they want me to do another show and are considering hiring me!!"
hide kcconf
show kcstar at right
hide aphnorm
show aphlove at left
a "Katelyn! That's awesome!!"
k "We're so proud of you Katelyn-sama!"
k "Thanks!"
hide kcstar
show kcnorm at right
hide aphlove
show aphnorm at left
if katdine==True:
    k "And to celebrate, [mcname] is taking me out to dinner tonight!"
    a "Oo, that sounds fun!"
else:
    k "And to celebrate, we're all going to dinner tonight! We'll invite Lucinda and Nicole as well."
    a "Awesome!"
    k "Hmmm, Kawaii-chan might have plans with Zane-kun tonight, but he hasn't been responding, so..we'll see!"
mc "We're all so proud of you, Katelyn."
k "Thank you, thank you, thank you!"
k "I'm gonna go see if I can find my old script and rehearse. I hope I didn't lose it like I lost my Shakespeare book..."
hide katsmile with dissolve
mc "Oh, well, I guess I'll leave then. See ya both!"
scene streetday with fade
"I'm really excited for Katelyn's musical! I wonder when they'll be performing it?"
"I'm assuming it takes a while for theatre productions to..well...produce.."
show tylerpizza with dissolve
ty "Well well well. What do we have here."
mc "I really wish we never met"
ty "Yknow you sound a lot like my family when you talk like that"
mc "Are you? Actively delivering pizzas right now?"
ty "Uh huh? What's wrong with that fuckface?"
mc "WOAH that was uncalled for"
ty "sorry i had a rough morning"
mc "Awesome, I think you should go back to your job"
ty "At least I have a job"
hide tylerpizza with dissolve
"...I mean, I have to give it to him, I actually am unemployed.."
"Whatever. I need breakfast."
"And where better to get breakfast then the Creamy Dreamy Coffee Co?"
scene coffeeshop with fade
"Hmmm...I think i'm in a croissant mood right now..."
"It's kinda like toast if you think about it"
show zanenorm with dissolve
"Woah? Is that Zane?"
mc "Zane, Hi!"
z "!!!"
hide zanenorm with easeoutleft
"..did he..run  away from me?"
show aarshock with dissolve
ar "...did you also see Zane run out of here?"
mc "Yeah..I did..."
ar "Did he run because of you...?"
mc "no! I just said hi! Then he dashed off..."
ar "Yeah he can be like that sometimes"
hide aarshock
show aarsmile
ar "But! It's nice to see you, [mcname]. You also grabbing breakfast?"
mc "I am, actually, yeah. I was thinking of grabbing a croissant."
ar "Hey, why don't you sit down and I grab us both food?"
mc "What? I couldn't ask you to do that.."
ar "Well, I have this Buy 1-Get 1 free coupon that expires soon, I might as well.."
mc "If you insist!"
ar "I'll go order for us."
hide aarsmile with dissolve
show aarnorm with dissolve
ar "Okay so it turns out the barista heard our conversation and also wired the money straight out of my bank account somehow so"
mc "...okay"
ar "Anyway..anything new with you?"
mc "Not much..oh! Not sure if you've heard, but Katelyn's performing in Midnight again soon!"
hide aarnorm
show aarsmile
ar "Really? That's great!"
mc "Mhm! And she even got noticed by a talent agency!"
ar "Of course she did, her performance in Midnight as Nutella Swan was spectacular."
ar "For being such a silly role, she really put her whole heart into it. The whole musical was amazing, really."
mc "Wow...I wish I could have seen it.."
ar "It really was spectacular, whatever you think you know of Katelyn's talent, seriously, it's nothing compared to Midnight."
mc "That's awesome! I didn't know Katelyn was that good.."
ar "Quite frankly, me neither. I was worried what a food-based Twilight parody would do to her career."
ar "I used to think Katelyn might only be able to stick to acting as a hobby but after Midnight, she could honestly go professional."
mc "Lord. Now i'm even more excited to see her performance, hopefully it's soon!"
ar "They probably still have all the old sets and costumes, and the first performance wasn't that long ago, so it's just a matter of making sure the actors still remember their lines. Shouldn't take too long."
ar "Oh, shoot, gotta run. This was a nice talk, though! Let me know when Katelyn performs!"
mc "I will! And thanks for the croissant!"
ar "See you later!"
hide aarsmile with dissolve
"That was fun. What to do now.."
show kattxt with easeinbottom
"Oo! I'm invited to see her rehearse!!"
"Do I wanna see that? Or do I wanna hang out with someone else, and go into the performance blind.."
$ katrehearse = False
$ laurhang = False
$ danhang = False
$ lucihang = False
menu:
    "Go to the rehearsal":
        $ katrehearse = True
        "Seeing her rehearse would be so awesome!"
        show mcreplykatgood with easeinbottom
        pause (1.0)
        show katreplygood with easeinbottom
        "I should shuffle on over there now..."
        jump katrehearsal
    "Don't go to the rehearsal":
        "I think I'd rather do something else..."
        show mcreplykatbad with easeinbottom
        pause (1.0)
        show katreplybad with easeinbottom
        "She doesn't seem too pleased.."
        "What should I do instead?"
        menu:
            "Hang out with Laurance":
                $ laurhang = True
                "Let's go see what Laurance is up to. Intuition tells me he's at the park"
                jump laurpark
            "Hang out with Dante":
                $ danhang = True
                "Let's go see what Dante is up to. Intuition tells me he's at MaccyDonald's."
                jump dandonald
            "Hang out with Lucinda":
                $ lucihang = True
                "Let's go see what Lucinda is up to. Intuition tell me she's at her house."
                jump lucihomehang
label laurpark:
    scene park with fade
    show laursad with dissolve
    mc "Hi Laurance!"
    la "Oh, hey, [mcname]"
    mc "Are you alright? You sound sad."
    la "I'm fine...it's just, it's nothing..."
    menu:
        "Pressure him":
            mc "TELL ME NEOW"
            hide laursad
            show laurshock
            la "What?"
            mc "TELL ME WHAT IS HAPPENING"
            la "I-I don't want to...?"
            mc "YOU ARE GOING TO TELL ME WHAT IS GOING ON RIGHT NOW!!!"
            la "NO!"
            mc "ok"
        "Leave it alone":
            mc "I mean if you say so"
    mc "..."
    mc "Well now I don't want to talk to you if you're sad"
    hide laursad
    hide laurshock
    show laurnorm
    la "I'm sorry, i'm sorry, it's really nothing."
    la "So, what's up?"
    mc "Not much. Oh! Y'know? Katelyn's gonna reperform Midnight soon! Her musical!"
    hide laurnorm
    show laursmile
    la "Oh right! Katelyn told us in the groupchat."
    hide laursmile
    show laursad
    la "Speaking of, we should probably add you to it..."
    mc "I'd enjoy that yeah"
    mc "But yeah, I'm very excited to see Katelyn perform."
    hide laursad
    show laursmile
    la "Haha, of course you are."
    mc "What does that mean?"
    hide laursmile
    show laursad
    la "Well..you know.."
    la "You're much more interested in Katelyn than the rest of us.."
    mc "W-what?? Well....Whaat? Weelll..."
    hide laursmile
    show laurnorm
    la "It's okay [mcname] it's alright"
    la "If it makes you feel any better, everyone already knows you like Katelyn"
    mc "How would that make me feel better"
    la "Sorry"
    mc "Does Katelyn know...?"
    la "I doubt it. She'd probably act a lot more different if she did know."
    la "But...it seems she really likes you too."
    mc "Really!?"
    la "I'm just saying what i've noticed! I could be wrong, but, she definitely likes you more than some of us, I'd say..."
    mc "Really..."
    la "Man, isn't this park so nice?"
    mc "It is! I really should be coming out here more often."
    la "Me and Katelyn actually like to play soccer out here on weekends, along with Garroth and Aaron sometimes."
    la "Would you be interested in joining us some day?"
    menu:
        "Sure":
            mc "Sure! Soccer sounds fun."
            la "Great! Let's see if there's anything we could organize this weekend."
        "No":
            mc "Nah, soccer sucks. Not a fan"
            la "Oh, that's alright"
            mc "Seriously it sucks"
            hide laurnorm
            show laurdis
            la "Alright"
            mc "No like really I hate it"
            la "That's a shame"
            mc "I actually cannot believe anyone would enjoy soccer"
            la "Okay I get it [mcname]"
    la "Oh, right, I do have to go now. I have some plans."
    hide laurdis
    hide laurnorm
    show laursmile
    la "It was great talking to you, [mcname]!"
    mc "Great talking to you too!"
    hide laursmile with dissolve
    "I guess I'll just sit on this bench for a bit, admire the scenery."
    "Man, this bench is nice and warm. Kind of want to lay down.."
    "..man..this bench is really comfy...kinda wanna close my eyes..."
    scene black with dissolve
    play sound snore
    "zzzz..z....."
    scene parknoon with fade
    stop music
    play music noonsong loop
    "Mmmvffhh...? Looks like I fell asleep.."
    "Oh my god, tons of missed calls from Katelyn, I'm late for dinner!"
    "I should run over right now."
    jump katdinner
label dandonald:
    scene alley with fade
    show dannorm with dissolve
    mc "Hey Dante! Umm...what're you doing in this alleyway?"
    d "Heyy, [mcname]!"
    d "Hey, you know what? You just caught me at a good time!"
    d "You ever heard of Skin Milk?"
    mc "Skim milk? Oh, yeah, my family and I used to drink it all the time when I was young."
    d "Nonono, not Skim milk, SKIN milk"
    mc "Skin milk...?"
    d "Yeah, it's made from like, angel skin. And they squeeze the milk out and it's suuuper good!"
    mc "Dante am I walking in on a weed session or"
    d "No I'm serious! And it lasts for super long, I've had mine for like, 4 years. Bought it in bulk"
    mc "WHAT? Dante you cannot drink 4 year old milk that's not good"
    d "No no no it's good! Like it tastes like mold and your stomach hurts a bit after but it's like, really good for you apparently."
    hide dannorm
    show dansmirk
    d "You know, sources say for each cup of Skin Milk you drink, you gain a little more angelic power."
    mc "Okay who are these sources? Where are you getting this milk from?"
    hide dansmirk
    show dannorm
    d "Right here, MaccyDonald's!"
    mc "This isn't MaccyDonald's this is the alley behind MaccyDonald's"
    d "Well like, there's a guy here who sells the milk, and says he's from MaccyDonald's, and he seems pretty honest idk"
    mc "Dante...how much are you paying for this milk"
    hide dannorm
    show danmad
    d "Liikeeee....$300? Per bag? It's actually not that much if you think about it-"
    mc "Dante you are getting scammed I'm so sorry to tell you!"
    d "Uhh, nuh uh!"
    mc "Dante, you're being sold expired milk for $300. Milk that is supposedly from Angel Skin. Just think about it."
    d "...."
    d "Yeah it does sound a little fake"
    mc "Are you meeting this seller today?"
    d "Yup, he should be here any minute now.."
    mc "Alright, let's confront this guy."
    show tylernorm at left with easeinleft
    show danmad at right with ease
    ty "Hey dude, got the money?"
    mc "YOU????????"
    ty "You want some milk too?"
    d "Actually, dealer, we'd like to talk to you!"
    ty "Make this quick I've got costumers at the MaccyDonald's down the street"
    mc "Look, Tyler, what you're doing is wrong. You're scamming Dante here and tons of other innocent people for their money!"
    mc "You're also putting them in danger by selling expired milk!"
    ty "Yeah I think I know all of that"
    mc "It's wrong! And you need to stop!"
    ty "Hey man are you buying the milk or not"
    d "No! No I am not!"
    ty "Fine but then you have to pay the cancellation fee"
    d "Oh, yeah sure, how much"
    hide tylernorm
    show tylergun at left
    ty "Your life"
    hide danmad
    show danscare at right
    play sound dancry
    d "WHAAAT"
    mc "WOAH LET'S CALM DOWN"
    ty "I have to kill everyone who knows the truth about Skin Milk!"
    d "YOU DO NOT NEED TO TRUST"
    ty "No no I have to"
    d "[mcname!u] WHAT DO WE DOO"
    menu:
        "Run away":
            mc "DANTE RUN"
            d "ON IT CAPTAIN"
            ty "WAIT GUYS-"
            scene Old_Street with fade
            show danmad with dissolve
            play sound breathe
            d "Man! I am WINDED!"
            mc "That was crazy..."
            d "But was running away a good idea? What if we bump into him again??"
            mc "Trust me I don't think he's going to remember this moment"
            d "Hm..."
            hide danmad
            show dannorm
        "Stand your ground":
            mc "...No! No you will NOT kill us!"
            ty "Oh yea?"
            mc "Yes! This is a free country! You will not shoot us!"
            d "Y...yeah!!"
            ty "Aww shucks really I didn't know this was a free country guess I'll go-I'M GONNA KILL YOU"
            mc "TYLER. STOP. THIS ISN'T YOU."
            mc "Look me in the eye Tyler. This isn't you. Please."
            ty "???"
            hide danscream
            show danmad
            d "Come on...Tyler...we know you're better than this..."
            ty "Alright fine I won't kill you guys you two are weirding me out"
            hide danmad
            show dannorm
            d "WOOHOO!!"
            ty "Well you two have really inspired me and i'm gonna quit my life of crime i'm gonna become a pro league baseball player like i've always dreamed of."
            hide tylergun with easeoutleft
            show dannorm at center with dissolve
            d "Man. That guy. Am I right?"
            mc "He's a weird one"
    d "Welp, thanks for helping me out, [mcname]!"
    d "I'm now $300 richer!"
    mc "Yeah...!"
    d "Oh, I should tell you, Katelyn's doing this performance thing soon, it's gonna be sick, you should come!"
    mc "Oh! I know already. Wait, how did you know?"
    d "Katelyn put it in the groupchat!"
    hide dannorm
    show danmad
    d "Oooff....you're not in the groupchat..."
    d "Don't worry bro we'll add you"
    mc "Thanks Dante"
    hide danmad
    show dannorm
    d "Well, I should go and buy some normal milk. Hopefully I'll see you around, [mcname]?"
    mc "Yup! See ya Dante!"
    d "Bye byeee!"
    hide dannorm with dissolve
    "Hmm..looks like I have some missed calls from Katelyn.."
    "Oh right! Dinner! I should probably head over there right now."
    jump katdinner
label lucihomehang:
    scene luciroom with fade
    show lucisad with dissolve
    mc "Hi Lucinda!"
    lu "[mcname]! How did you...get in here?"
    mc "Don't worry, what are you up to?"
    lu "Weelll...I've been working on this potion, but it's not really working."
    lu "It's supposed to be a hyper-focus potion. Something to heighten all of your senses. Because I haven't found anyone to help me, I've been testing it on this ant."
    lu "With every batch I make, this ant seems to have no visible affect! I have no idea what I'm doing wrong?"
    mc "How would you know if it's working on the ant?"
    lu "Well...the ant would probably start moving super fast, but it's just been... normal."
    lu "It seems like what's wrong is that i'm missing an additional ingredient, and I've narrowed it down to either Man Tears or Fungus."
    mc "man tears or fungus...?"
    hide lucisad
    show lucinorm
    lu "They have a lot more magical properties than you'd think"
    mc "Okay...have you tried either?"
    lu "That's the thing...I only have enough material left to test out one, and this stuff is kinda rare, so I really need to make this last one count."
    lu "Help me, [mcname], which one should I choose?"
    mc "Hmmmm..."
    menu:
        "Man Tears":
            mc "Hmmm...try the man tears?"
            lu "Alright.."
            lu "These are tears I collected from Garroth, he stubbed his toe and started crying and I noticed a sparkle in his eyes..."
            lu "That's when I knew I had to whip out my mason jar"
            mc "Definitely"
            play sound pour
            lu "Pouring..."
            mc "It's bubbling!"
            lu "Mixing it around...alright. Let's feed it to this ant."
            "Let's hope this works...it'd be embarassing if it didn't."
            hide lucinorm
            show lucismirk
            lu "Woah! Look! It's running super fast now!"
            mc "Yay! It worked!"
            lu "Awesome! Man, I've been working on this for a while..thankfull you chose the right one. Great job, [mcname]"
            mc "Haha, thanks."
        "Fungus":
            mc "Hmmm...try the fungus?"
            lu "Alright.."
            lu "This is a fungus I collected from Aaron's house. He went on this short vacation for a bit but must've left something weird in his house, because when he came back, major mold infestation!"
            mc "Woaah..!"
            lu "At the time, he couldn't afford professional mold cleaners since the mess was so huge, so we all helped out with the cleaning. I found this weird fungus growing in the corner, and took it since I felt a magical aura coming from it."
            lu "To this day, we still don't know how it happened."
            mc "That's awful...I don't think I could ever leave my home ever again now that you told me that"
            play sound pour
            lu "Pouring..."
            mc "It's bubbling!"
            lu "Mixing it around...alright. Let's feed it to this ant."
            "Let's hope this works...it'd be embarassing if it didn't."
            hide lucinorm
            show lucisad
            lu "Ugh...still nothing. It was the man tears this whole time."
            mc "Aww man, Lucinda, I'm sorry..."
            lu "It's okay, not your fault, you wouldn't have known. It's not too serious, I suppose."
    mc "Soo..any specific reason you needed this potion?"
    hide lucisad
    hide lucismirk
    show lucinorm
    lu "I just felt like it'd be useful to have. You see, I normall make potions with much more drastic effects, and those come naturally to me! But something basic like this, I don't know, I always find myself having a hard time."
    mc "Well, I think potion making in general is very impressive."
    lu "Haha, thank you, [mcname]."
    lu "So? Why are you here?"
    mc "No reason, just bored. Oh! Katelyn's actually going to be reprising her role in Midnight soon! I was thinking we should all go and watch!"
    lu "Oh, right! I already know."
    mc "Oh?"
    lu "Yeah, she put it in the groupchat."
    mc "Groupchat?"
    lu "You know? The groupchat? Oh, right, we never added you. I'll do that right now."
    mc "That would be appreciated.."
    if katdine == False:
        mc "Also, not sure if she put this in the groupchat, but Katelyn and I were thinking of having dinner with the girls to celebrate!"
        lu "Oh yeah, she did mention that. I'll be there. I have some stuff to do first, though, so tell everyone I'll be a bit late."
        mc "Will do!"
    hide lucinorm
    show lucismirk
    lu "So, I'm sure you're very excited to see Katelyn's performance~?"
    mc "Very! I'd love to see her work. I heard she's a great actor and I know how passionate she is about theatre so I'm really looking forward to- hey why did you say it like that"
    lu "Hehe, you know~~~"
    mc "?"
    lu "Because you're head over heels for Katelyn??"
    mc "WHAT? No.....WHAT? Noooo...."
    lu "You can't fool me, [mcname], I know. We all do, actually."
    mc "Ugh...really?"
    lu "Haha, yeah."
    hide lucismirk
    show lucisad
    lu "I mean, it's not a big deal, you might have to fight off Travis but..."
    hide lucisad
    show lucismirk
    lu "Don't worry, I think she likes you more than him, so you'll be fine."
    mc "Uh huh..."
    hide lucismirk
    show lucinorm
    lu "Well, I really need to get back to work, so could you.....leave"
    mc "Oh right yeah no that's alright i'll go"
    "Might as well head to the dinner..."
    jump katdinner
label katrehearsal:
    








