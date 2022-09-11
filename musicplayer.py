#THIS IS MY FIRST PROJECT GONNA MAKE BY MYSELF
#IN THIS I AM GOING TO MAKE A MUSIC PLAYER 
from tkinter import*
from tkinter import ttk
import os 
from pygame import mixer
from mutagen.mp3 import MP3
Player=Tk()


if __name__=='__main__':
    #DEVELOPINFG THE STRUCTURE
    Player.geometry("450x600")
    Player.title("FreshTune")
    Player.configure(bg='light blue')
    mixer.init()
    #MAKING A FRAME
    strut=Frame(Player,)
    strut.pack(padx=20,pady=20)
    
    songs=Frame(Player)
    songs.pack()
    
    play=Frame(Player)
    play.pack()
    
    switch=Frame(Player)
    switch.pack()
    #CREATING A SCROLLBAR ATTACH WITH LISTBOX
    scroll=Scrollbar(strut)
    scroll.pack(side=RIGHT,fill=Y)

    
    #BUILDING A LISTBOX FOR DISPLAYING SONGS AND STORING
    loot=Listbox(strut,height=20,width=200)
    
    
    #adding songs in lsitbox
    path=r'C:\Users\hp\OneDrive\Desktop\New folder'
    index=0
    playlist=[]
    for i in os.listdir(path):
        loot.insert(index,i)
        new_path=path + '/'+ i
        playlist.insert(index,new_path)
        index+=1
    loot.pack()
    scroll.config(command=loot.yview)
    loot.config(yscrollcommand=scroll.set)
    
    #SONG DETAITLS
    song_name=ttk.Label(songs,text='songs playing')
    song_name.pack(padx=150,pady=10,)
    
    start=ttk.Label(play,text="00:00:00")
    start.grid(row=0,column=0)
    
    end=ttk.Label(play,text="00:00:00")
    end.grid(row=0,column=5)
    
    #CREATING A STATUS BAR
    statbar=ttk.Progressbar(play,orient=HORIZONTAL,mode='determinate',value=0)
    statbar.grid(row=0,column=1,columnspan=4,ipadx=40,pady=10,padx=50)
    
    #FOR BUTTONS
    #function for playing song
    def play_song():
        select=loot.curselection()
        select=int(select[0])
        playit=playlist[select]
        song_name.config(text=loot.get("anchor"))
        mixer.music.load(playit)
        mixer.music.play()
        
    def pause_song():
        pause_song.grid_remove()
        play.grid()
        song_name.config(text=loot.get("anchor"))
        mixer.music.pause()
        
    def prev_song():
        prev_music=loot.curselection()
        prev_music=int(prev_music[0]) - 1
        playit=playlist[prev_music]
        prev_song_name=loot.get(prev_music)
        song_name.config(text=prev_music)
        mixer.music.load(playit)
        mixer.music.play()
        
        loot.select_clear(0,'end')
        loot.activate(playit)
        loot.select_set(playit)
    
    def next_song():
        next_music=loot.curselection()
        next_music=int(next_music[0])+1
        playit=playlist[next_music]
        next_song_name=loot.get(next_music)
        song_name.config(text=next_song_name)
        mixer.music.load(playit)
        mixer.music.play()
        
        loot.select_clear(0,'end')
        loot.activate(playit)
        loot.select_set(playit)
    
    def base(val):
        global voll
        voll=float(val)/100
        mixer.music.set_volume(voll)
    
    ###########################################################################################################
    play=Button(switch,text="⏯️",width=4,height=2,bg='light blue',fg='orange',command=play_song)
    play.grid(row=1,column=3,padx=10,pady=10)
    
    pause_song=Button(switch,text="⏯️",width=4,height=2,bg='light blue',fg='orange',command=pause_song)
    pause_song.grid(row=1,column=3,padx=10,pady=10)
    
    pre=Button(switch,text="⏮️",width=4,height=2,bg='light blue',fg='orange',command=prev_song)
    pre.grid(row=1,column=2,padx=10,pady=10)
    
    next=Button(switch,text="⏭️",width=4,height=2,bg='light blue',fg='orange',command=next_song)
    next.grid(row=1,column=4,padx=10,pady=10)
    
    #FOR VOLUME
    speaker=Button(switch,text="🔊",width=4,height=2,bg='light blue',fg='orange',)
    speaker.grid(row=2,column=2,)
    
    vol=Scale(switch,from_=0 ,to=100,orient=HORIZONTAL,bg="light blue",length=150,width=3,sliderlength='5',command=base)
    vol.set(30)
    vol.grid(row=2,column=3)
    
    Player.mainloop()