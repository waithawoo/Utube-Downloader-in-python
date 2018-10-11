from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))

choice = input('1.Audio\n2.Video\n')
if (choice == '2'): 
      name = yt.title
      print(name)
      videos = yt.streams.filter(only_video=True).all()

      s = 1
      for v in videos:
         print(str(s)+". "+str(v.resolution)+" "+str(v.subtype))
         s += 1
      n = int(input('Enter the Type Number to be Downloaded:'))   
      down = videos[n-1]

elif (choice == '1'):
      name = yt.title
      print(name)

      audios = yt.streams.filter(only_audio=True).all()
      
      s = 1
      for a in audios:
         print(str(s)+". "+str(a.subtype))
         s += 1
            
      n = int(input('Enter the Type Number to be Downloaded:'))   
      down = audios[n-1]
      
#n =int(input('Enter the Type Number to be Downloaded:')

destination = str(input('Enter the destination:'))
down.download(destination)
print('Download is complete!')