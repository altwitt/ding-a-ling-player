from mutagen.mp3 import MP3
import os






p = [
"1AesopRockIntegratedTechSolutions.mp3",
"1BeautifulPeople.mp3",
"2GrapeLady.mp3",
"2MrBungleQuietDontTellAnybody.mp3",
"3RickAndMortyWubbaLubaDubDub.mp3",
"5BustaOhMyGod.mp3",
"6BreakmasterCylinderMeowMeow.mp3",
"7KeepBouncing.mp3",
"8MrBungleGeetar.mp3",
"8TomZombieOneBigCrunch.mp3",
"BreakmasterCylinderBlinkStatement.mp3",
"Donkey.mp3",
"DuckHunt.mp3",
"FrenchBulldog.mp3",
"Goat.mp3",
"HarryMackShortQuickDistorted.mp3",
"IBeOnThatKryptonite.mp3",
"ILikeRocks.mp3",
"LilJonOk.mp3",
"LogicPerfect.mp3",
"Mail.mp3",
"Makeitso.mp3",
"MarcRebellitHahhh.mp3",
"MrBungleNip.mp3",
"Parrot2.mp3",
"ParrotLetTheBodiesHitTheFloorShort.mp3",
"Piglet.mp3",
"Possum.mp3",
"RobSchneiderYouCanDoIt.mp3",
"SciFiConfirmation.mp3",
"SoundOfPolice.mp3",
"SpaceAlert.mp3",
"SwishaReverb.mp3",
"TazmanianDevil1.mp3",
"TenaciousYouEffinBMA.mp3",
"TomZombieThunderKiss65.mp3",
"TooManyZoosWarriors.mp3",
"VulfRelease.mp3",
"WuTangFightFast.mp3",
]





player = []
proot = r'E:/Code/musicplayers/ding-a-ling-player/public/audio'


for x in range(1, len(p)):
    fpath = os.path.join(proot, p[x])

    audio = MP3(fpath)
    dur = round(audio.info.length, 2)

    player.append({
    "id": str(x),
    "name": p[x][:-4],
    "duration": dur,
    "audio": "/audio/" + p[x],
  })

print(player)