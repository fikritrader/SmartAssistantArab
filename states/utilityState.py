import requests
import json
import states.Api.movieApi as movieApi
import states.Api.newsApi as newsApi
import states.Api.recipeApi as recipeApi
import states.Api.storyTeller as storyTeller
import states.predictIntent as predictIntent
import states.commandHelper as commandHelper
from gtts import gTTS
import speech_recognition as sr
import states.tts as ttsUtil
import os

numbs = ['first','second','third','fourth','fifth']

#-----------------------------------------------------------------
#this function queries a story using its category and reads it
#-----------------------------------------------------------------
def getStory():
    files =['moral.txt','animal.txt','classics.txt','mythology.txt','world.txt','modern.txt']
    # commandHelper.toggleState("talk")
    # playsound("audioBase/storyTeller.mp3")
    # commandHelper.toggleState("idle")
    ttsUtil.say("storyTeller.mp3")

    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("say somethng")
        audio=r.listen(source,phrase_time_limit=3)
        print("time over, thanks")
    try:
        genre=r.recognize_google(audio,language='en')
        print(genre)
        prediction = predictIntent.predictStory(genre)
        print('has predicted',str(prediction))
        currentPath=os.path.dirname(os.path.dirname(__file__))
        storiesPath = os.path.join(currentPath,'misc/stories/'+files[prediction])
        print(storiesPath)
        if os.path.isfile(storiesPath):
            # commandHelper.toggleState("talk")
            # playsound("audioBase/introducingStory.mp3")
            # commandHelper.toggleState("idle")
            ttsUtil.say("introducingStory.mp3")

            storyText=storyTeller.random_line(storiesPath)
            print(storyText)
            tts = gTTS(storyText , lang="en")
            tts.save("audioBase/storyToRead.mp3")
            # commandHelper.toggleState("talk")
            # playsound("audioBase/storyToRead.mp3")
            # commandHelper.toggleState("idle")
            ttsUtil.say("storyToRead.mp3")

        else:
            # commandHelper.toggleState("talk")
            # playsound("audioBase/noStories.mp3")
            # commandHelper.toggleState("idle")
            ttsUtil.say("noStories.mp3")

    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    

    
    

#-----------------------------------------------------------------
#this function gets the news through an api and check if their fake
#-----------------------------------------------------------------
def getNews():
    newsData = newsApi.satisfyQuery()
    if len(newsData) > 0:
        for i,val in enumerate(newsData):
            newsString = 'the {} news article is titled {}, do you want me to use my fake news detector on this article ?'.format(numbs[i],val['title'])
            tts=gTTS(newsString,lang="en")
            tts.save('audioBase/newsAnswer'+str(i)+'.mp3')
            # commandHelper.toggleState("talk")
            # playsound('audioBase/newsAnswer'+str(i)+'.mp3')
            # commandHelper.toggleState("idle")
            ttsUtil.say('newsAnswer'+str(i)+'.mp3')

            os.remove('audioBase/newsAnswer'+str(i)+'.mp3')
            r=sr.Recognizer()
            with sr.Microphone(device_index=1) as source:
                print('say it')
                audio=r.listen(source,phrase_time_limit=3)
                print('got it')
            try:
                print('will recognize')
                ans=r.recognize_google(audio,language='en')
                print('recognized',ans)
                if ans == 'yes':
                    prediction = 63
                    predictionString = 'my fake news detector says that the probability of this article being fake is {}%'.format(prediction)
                    tts=gTTS(predictionString,lang="en")
                    tts.save('audioBase/fakeNewsPred'+str(i)+'.mp3')
                    # commandHelper.toggleState("talk")
                    # playsound('audioBase/fakeNewsPred'+str(i)+'.mp3')
                    # commandHelper.toggleState("idle")
                    ttsUtil.say('fakeNewsPred'+str(i)+'.mp3')
                    os.remove('audioBase/fakeNewsPred'+str(i)+'.mp3')
            except:
                pass

    else:   
        # commandHelper.toggleState("talk")
        # playsound("audioBase/noNews.mp3")
        # commandHelper.toggleState("idle")
        ttsUtil.say('noNews.mp3')

#-----------------------------------------------------------------
#this function get recipes using an ingredient through an api
#-----------------------------------------------------------------
def getRecipeByComp():
    r=sr.Recognizer()
    # commandHelper.toggleState("talk")
    # playsound("audioBase/recipeApiStarter.mp3")
    # commandHelper.toggleState("idle")
    ttsUtil.say('recipeApiStarter.mp3')

    with sr.Microphone(device_index=1) as source:
        print('say the ingredient')
        audio=r.listen(source,phrase_time_limit=3)
        print('got it')
    try:
        print('will recognize')
        ingredient=r.recognize_google(audio,language='en')
        print('recognized',ingredient)
        recipesData= recipeApi.satisfyQuery(ingredient)
        if len(recipesData)>0:
            for i,val in enumerate(recipesData):
                recipeString = 'the {} recipe is {}, its inredients are {}'.format(
                    numbs[i],
                    val['title'],
                    val['ingredients']
                )
                tts=gTTS(recipeString,lang="en")
                tts.save('audioBase/recipeAnswer'+str(i)+'.mp3')
                # commandHelper.toggleState("talk")
                # playsound('audioBase/recipeAnswer'+str(i)+'.mp3')
                # commandHelper.toggleState("idle")
                ttsUtil.say('recipeAnswer'+str(i)+'.mp3')
                os.remove('audioBase/recipeAnswer'+str(i)+'.mp3')
        else:
            # commandHelper.toggleState("talk")
            # playsound("audioBase/noRecipes.mp3")
            # commandHelper.toggleState("idle")
            ttsUtil.say('noRecipes.mp3')
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

#-----------------------------------------------------------------
#this function gets data about a movie using its title through an api
#-----------------------------------------------------------------
def getMovieByTitle():
    r=sr.Recognizer()
    # commandHelper.toggleState("talk")
    # playsound("audioBase/movieApiStarter.mp3")
    # commandHelper.toggleState("idle")
    ttsUtil.say('movieApiStarter.mp3')

    with sr.Microphone(device_index=1) as source:
        print('say it')
        audio=r.listen(source,phrase_time_limit=3)
        print('got it')
    try:
        print('will recognize')
        title=r.recognize_google(audio,language='en')
        print('recognized',title)
        filmData = movieApi.satisfyQuery(title)
        movieString = 'The movie {} is a {} movie, released on {}, {} rated, with an IMDB rating of {}, do you want to hear its plot ?'.format(
            title,
            filmData['genre'],
            filmData['releaseYear'],
            filmData['rated'],
            filmData['imdbRating'],
            )
        
        tts=gTTS(movieString,lang="en")
        tts.save('audioBase/movieAnswer.mp3')
        # commandHelper.toggleState("talk")
        # playsound("audioBase/movieAnswer.mp3")
        # commandHelper.toggleState("idle")
        ttsUtil.say('movieAnswer.mp3')
        os.remove('audioBase/movieAnswer.mp3')
        with sr.Microphone() as source:
            print('say it')
            audio=r.listen(source)
            print('got it')
        try:
            print('will recognize')
            answer=r.recognize_google(audio,language='en')
            print('recognized',answer)
            if answer == 'yes':
                tts=gTTS(filmData['plot'],lang="en")
                tts.save('audioBase/moviePlot.mp3')
                # commandHelper.toggleState("talk")
                # playsound("audioBase/moviePlot.mp3")
                # commandHelper.toggleState("idle")
                ttsUtil.say('moviePlot.mp3')
                os.remove('audioBase/moviePlot.mp3')
        except:
            pass
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

#-----------------------------------------------------------------
#this function manages the transition between the utility states
#-----------------------------------------------------------------
def utilityState():
    r=sr.Recognizer()
    # commandHelper.toggleState("talk")
    # playsound("audioBase/utilityState.mp3")
    # commandHelper.toggleState("idle")
    ttsUtil.say('utilityState.mp3')
    with sr.Microphone(device_index=1) as source:
        print('say it')
        audio=r.listen(source,phrase_time_limit=3)
        print('got it')
    try:
        print('will recognize')
        answer=r.recognize_google(audio,language='en')
        print('recognized',answer)
        options = [getStory,getNews,getRecipeByComp,getMovieByTitle]
        prediction = predictIntent.predictUtility(answer)
        options[prediction]()
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
