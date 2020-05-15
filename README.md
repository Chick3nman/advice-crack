# advice-crack
Bad Password Advice Leading to Targeted Cracking Methodologies


This repo is a collection of bad password advice, where it came from, and scripts/methods for attacking passwords generted following that advice. 

The idea to collect and organize the bad advice and cracking methods came up due to this tweet by [@hanno](https://twitter.com/hanno):

https://twitter.com/hanno/status/1249650832238424066
![@hanno's tweet showing the bad advice](https://i.imgur.com/HcfxqVY.png)

The advice that the above tweet is referencing comes from this How-To Geek article titled [__10 Ways to Generate a Random Password from the Linux Command Line__](https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/)

A Fellow cracker, [@Tychotithonous](https://twitter.com/TychoTithonus/) aka [@roycewilliams](https://github.com/roycewilliams), linked the tweet to me in a chat and the math immediately became apparent, there were few enough candidates in the possible keyspace that I could reasonably generate and test all of them with just my workstation. A few minutes and a quick python script later, I had 324million possible candidates spanning more than a decade, from 01-01-2010(the date i could first find the mentioned advice) to 4-13-2020. I moved them to my cracking folder and went to grab a list of hashes to try. The hashes I sourced were from the 32hex left list on [hashes.org](https://hashes.org/index.php), which collects public hash lists from breaches/leaks for researchers to crack and use for analytics.

https://twitter.com/Chick3nman512/status/1249769263302352897
![Hashcat running on my workstation](https://pbs.twimg.com/media/EVgRS-JX0AEpoNo?format=png&name=medium)

As you can see from the screenshot, I was able to test the 324million candidates against the 76million hashes running as MD5 in just under 30 seconds, immediately finding 4 hashes with passwords following that advice! Someone, somewhere, is using that bad password advice and is likely completely unaware that it now takes only seconds for an attacker to crack. 

Finding patterns based on bad advice given out about password generation is not new to the password cracking/research field, but this is a prime example of something that may _look_ secure to someone that is unaware of how advanced attacks have become. Use a password manager and let it generate long(12+ char), random, unique passwords, and enable multi-factor auth wherever possible.
