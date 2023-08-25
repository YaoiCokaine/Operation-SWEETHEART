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
menu:
    "Go to the rehearsal":
        $ katrehearse = True
    "Don't go to the rehearsal":

