# Think2Type
Code or the software part of T2T :)

# Academic Paper
https://www.ijert.org/research/think2type-thoughts-to-text-using-eeg-waves-IJERTV9IS060431.pdf

# Introduction

* Blind People have difficulties in using electronic devices. 
* Often they have to rely on helpers or other softwares which may not be very helpful for critical information passwords/bank accounts/etc.
* This causes privacy and security conserns.
* We aim to build a device which will help them to input all the required information without any external help.
* Directly capturing thoughts is hard as diffferent people think of same things differently and is computationaly difficult.
* Simplifying this issue by asking users to think in morse code and using motor signals to signify 0, 1 and /.
* This reduces complexity and generalize the model(As motor signals for same purpose do not vary much for different people)

# TODO:
1. Make a continuous csv writing data collection script --asd1299
2. Write a script to read the csv and feed into model (take care of freq, etc)
3. Get ready with a deployable model,
             input (csv's data) ==> model ==> prediction  
(Note : Whether to have this process done char by char or word by word or however is totally the coders decision) 


# H/W TODO:

1. Test voltage divider
2. Test kit with simulation voltage
3. Visualize signal from human (dso? idk)
4. Connect electrodes to kit and visualize on ADS software.
