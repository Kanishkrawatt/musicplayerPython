scroll=Scrollbar(Player)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=loot.yview)
    loot.config(yscrollcommand=scroll.set)