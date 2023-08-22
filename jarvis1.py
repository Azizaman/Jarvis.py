import pyttsx3
import speech_recognition as sr
import subprocess
#import espeak_phonemizer
import playsound
from gtts import gTTS
import pyaudio
import webbrowser 
import pywhatkit
import wikipedia
import pyautogui
import os
#import keyboard 
from PyDictionary import PyDictionary as Diction
import datetime
import playsound
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import PyPDF2
from pywikihow import search_wikihow 
#subprocess.run('clear')
#engine=pyttsx3.init('espeak')
#voices=engine.getProperty("voices")
#print(voices[14])
#engine.setProperty("voices",voices[14].id)

'''def speak(audio):
    print(' ')
    
    engine.say(audio)
    print(' ')
    engine.runAndWait()'''

def speak(text):
    tts=gTTS(text=text,lang='en')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    print(f':{text}')

#import subprocess



'''def speak(text):
   result= subprocess.run(['espeak', '-ven+m7', '-k5', '-s150', text], capture_output=True,text=True)
   print(result.stdout)
'''





#speak('hello sir i am jarvis.,nice to meet u tony stark. ,i am a your virtual assistant .,  ready to help u any time')


def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        command.pause_threshold=1
        audio=command.listen(source)

        try:
            print("Recognizing......")
            query=command.recognize_google(audio,language='en-in')
            print(f'u said : {query}')

        except Exception as Error:
            return 'none'
        
        return query.lower()

#speak('hello sir i am jarvis nice to meet u ')

#takecommand()


'''query=takecommand()
if 'hello'in query:
    speak('hello sir how can i help u')
else:
    speak('no command found')'''
speak('Hello sir how may i help you')
def taskexe():
    def whatsapp():
        speak('Tell me the name of the person!')
        name=takecommand()
        if 'aman' in name:
            speak('tell me the message')
            msg=takecommand()
            speak('tell me the time sir')
            speak('time in hour')
            hour=int(takecommand())
            speak('time in minute')
            minute=int(takecommand())
            pywhatkit.sendwhatmsg('+918600073906',msg,hour,minute,1)
            
            time=takecommand()
            speak('ok sir sending the message')
        else:
            speak('tell me phone number sir')
            phone=int(takecommand())
            ph='+91'+phone
            speak('tell me the message')
            msg=takecommand()
            speak('tell me the time sir')
            speak('time in hour')
            hour=int(takecommand())
            speak('time in minute')
            minute=int(takecommand())
            pywhatkit.sendwhatmsg('ph',msg,hour,minute,1)
            
            time=takecommand()
            speak('ok sir sending the message')
    def openapps():
        speak('ok sir,wait a second')
        if 'vscode' in query:
            os.system('/home/azizamam/Downloads/VisualStudioSetup.exe')
        
    def closeapps():
        if 'vscode' in query:
            os.system("TASKKILL /F /im VisualStudioSetup.exe")
    ''' def youtubeAutomation():
        speak('whats your command')
        comm=takecommand()
        if 'pause' in comm:
            Keyboard.is_pressed('space bar')'''
    def chromeAutomation():
        #left for later
        pass
    def dict():
        speak('dictionary activated')
        speak('tell me the problem')
        prob1=takecommand()
        if 'meaning' in prob1:
            prob1=prob1.replace('what is the',' ')
            prob1=prob1.replace('jarvis','')
            prob1=prob1.replace('of','')
            prob1=prob1.replace('meaning of',' ')
            result=Diction.meaning(prob1)
            speak(f'the meaning of {prob1} is {result}')
        speak('dictionary exited')
    def videoDownloader():
        '''do it later 
        present with GUI'''
    def takehindi():
        command=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening.....')
            command.pause_threshold=1
            audio=command.listen(source)

        try:
            print("Recognizing......")
            query=command.recognize_google(audio,language='en-in')
            print(f'u said : {query}')

        except Exception as Error:
            return 'none'
        
        return query.lower()
        
    def trans():
        speak('tell me the line')
        line=takehindi()
        translate=Translator()
        result=translate.translate(line)
        Text=result.text
        speak('the translation for this line is:'+Text)
    def temperature():
        search='temperature in nagpur'
        
        URL='https://www.google.com/search?q='+search
        r=requests.get(URL)
        data=BeautifulSoup(r.text,'html.parser')
        temperature=data.find('div',class_='BNeawe').text 
        speak(f'the temperature outside is {temperature} celcius')
        

    def Reader():
        speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'atomic habits' in name:

            os.startfile('/home/azizamam/Documents/atomic-habits (copy).pdf')
            book = open('/home/azizamam/Documents/atomic-habits (copy).pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)

        elif 'automate with python' in name:
            os.startfile('/home/azizamam/Documents/automate the boring stuff with python.pdf')
            book = open('/home/azizamam/Documents/automate the boring stuff with python.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)
        
        
        
        
            
              
            
        
            
            
        
        
                  
    while True:
        query = takecommand()
        if 'hello' in query:
            speak('hello sir, I AM jarvus.')
            speak('your personal assistant')
        elif 'how are you' in query:
            speak('I am fine sir')
        elif 'go jarvis' in query:
            speak('ok sir bye')
            break  # This line should be indented to be inside the while loop
        elif 'youtube search' in query:
            query=query.replace('jarvis', '')
            query=query.replace('youtube search', '')
            web='https://www.youtube.com/results?search_query= ' + query
            webbrowser.open(web)
            speak('ok done sir')
        elif 'search' in query:
            query=query.replace('jarvis', '')
            query=query.replace('search', '')
            pywhatkit.search(query)
            speak('i found these results')
        elif 'site' in query:
            query=query.replace('jarvis','')
            query=query.replace('open', '')
            query=query.replace(' ', '')
            web1=query.replace('website', '')
            web2='https://www.'+web1+'.com'
        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('search', '')
            query=query.replace('jarvis', '')
            query=query.replace('wikipedia', '')
            wiki=wikipedia.summary(query,4)
            speak('according to Wikipedia',wiki)
        elif 'whatsApp message' in query:
            whatsapp()
        elif 'screenshot' in query:
            speak('ok sir what should i name the screenshot')
            s_name=takecommand()
            sc_name=s_name+".png"
            path1="/home/azizamam/codes"+sc_name
            
            kk=pyautogui.screenshot()
            kk.save(path1)
            speak('screen shot captured sir')
            os.system('/home/azizamam/codes')
        elif 'thank you' in query:
            speak('welcome sir')
            speak('anything else sir!')
        elif 'thanks' in query:
             speak('welcome sir')
             speak('anything else sir!')
        elif 'open vs code' in query:
            openapps()
        elif 'close vscode ' in query:
            closeapps()
        elif 'dictionary' in query:
            dict()
        elif 'alarm' in query:
            speak('enter the time')
            time=int(input('enter the time'))
            while True:
                time_AC=datetime.datetime.now()
                now=time_AC.strftime('%H:%H:%S')
                
                if now ==time:
                    speak('time to wake uo sir')
                    playsound('')
                    speak('alarm closed')
                elif now>time:
                    break       
        elif  'video download' in query:
            #do it later
            videoDownloader()
            
            pass
            
        elif 'translate' in query:
        
            trans()
        elif 'google' in query:
            import wikipedia as googlescrap
            query=query.replace('jarvis','')
            query=query.replace('google search','')
            query=query.replace('google','')
            speak('this is what i found in the web!')
            pywhatkit.search(query)
            
            try:
                
                result=googlescrap.summary(query,3)
                speak(result)
            except:
                speak('no speakable data available!')
        elif 'temperature' in query:
            temperature()
        elif 'how to' in query:
            speak('getting data from internet')
            op=query.replace('jarvis','')
            max_result=1
            how_to_func=search_wikihow(op,max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
                        
            

            
        
        
        
            
        
        
            
            
        
            
            
            
            
taskexe()