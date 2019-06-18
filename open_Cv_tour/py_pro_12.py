import vlc
import time
instance = vlc.Instance()
media = instance.media_new('music.MP4')
player = instance.media_player_new()
player.set_media(media)



#set the player position to be 50% in
player.set_position(50)

#Reduce the volume to 70%
player.audio_set_volume(50)
#player.play()
#

#Build vlc option string
options = 'sout=#duplicate{dst=rtp{access=udp,mux=ts,dst=224.0.0.1,port=1233},dst=display}'

#Load media with streaming options
media = instance.media_new('test.mp3', options)

player.play()
time.sleep(10)
