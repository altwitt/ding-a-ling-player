from mutagen.mp3 import MP3
import os

def get_mp3_duration(filepath):
  """
  This function attempts to get the duration of an mp3 file using Mutagen.

  Args:
      filepath (str): Path to the mp3 file.

  Returns:
      float: Duration of the mp3 file in seconds, or None if information is unavailable.
  """
  try:
    audio = MP3(filepath)
    return audio.info.length
  except (IOError, mutagen.error):
    print(f"Error getting duration for {filepath}")
    return None

# Example usage
filepath = "E:\\Code\\musicplayers\\svelte-music-player\\public\\audio\\LilJonOkDing.mp3"
duration = get_mp3_duration(filepath)
if duration:
  print(f"File: {filepath}, Duration: {duration} seconds")
else:
  print("Could not get duration information for the file.")


p = ['AesopRockHuhWhosThereDing.mp3', 'AesopRockIntegratedTechSolutionsDing.mp3', 'AnimalAngryCatDing.mp3', 'AnimalBabyGoatsDing.mp3', 'AnimalCat1Ding.mp3', 'AnimalDonkeyDing.mp3', 'AnimalFrenchBulldogDing.mp3', 'AnimalGoatDing.mp3', 'AnimalHonkForTurkeysDing.mp3', 'AnimalLabradorNoVetDing.mp3', 'AnimalLambDing.mp3', 'AnimalLaughingKookaburra1Ding.mp3', 'AnimalParrot2Ding.mp3', 'AnimalParrotLetTheBodiesHitTheFloorShortDing.mp3', 'AnimalPigletDing.mp3', 'AnimalPossumDing.mp3', 'AnimalTazmanianDevil1Ding.mp3', 'BreakmasterCylinderBlinkStatementDing.mp3', 'BreakmasterCylinderMeowMeowDing.mp3', 'DuckHuntDing.mp3', 'EminemAhhAhhAhhDing.mp3', 'EminemTouchMyBodyDing.mp3', 'EuroTripMailMFerFastDingMA.mp3', 'FlightOfTheConchordsHumansAreDeadFastDing.mp3', 'GirlTalkAhAhAhAhAhAhDing.mp3', 'GirlTalkIBeOnThatKryptoniteDing.mp3', 'GirlTalkSoundOfPoliceDing.mp3', 'GrapeLady2CantbreathDing.mp3', 'GrapeLadyFastDing.mp3', 'HarryMackShortQuickDistortedDing.mp3', 'JurassicFiveContactDing.mp3', 'JurassicFiveContactInterplanetaryContactWithEarthDing.mp3', 'LilJonOkDing.mp3', 'LogicPerfectDing.mp3', 'MarcRebellitHahhhDing.mp3', 'MrBungleCarryStressInTheJawGeetarDing.mp3', 'MrBungleCarryStressInTheJawNipDing.mp3', 'MrBungleCarryStressInTheJawQuietDontTellAnybodyDing.mp3', 'MrBungleViolenciaDomestica1Ding.mp3', 'RickAndMortyWubbaLubaDubDubDing.mp3', 'RobSchneiderYouCanDoItDing.mp3', 'SciFiConfirmationDing.mp3', 'SpaceAlertDing.mp3', 'STNGMakeitsoDing.mp3', 'STNGTransporterBeamingInDing.mp3', 'SwishaReverbDing.mp3', 'TenaciousYouEffinBDingMA.mp3', 'ThreeStoogesCurlyDing.mp3', 'TibetanBellsDing.mp3', 'TomZombieOneBigCrunchDing.mp3', 'TomZombieThunderKiss65Ding.mp3', 'TooManyZoosWarriorsDing.mp3', 'TooManyZoosWarriorsFastDing.mp3', 'TribeCalledQuestBustaOhMyGodDing.mp3', 'TribeCalledQuestKeepBouncingDing.mp3', 'VulfBreatheReleaseDing.mp3', 'WuTangFightFast.mp3', 'WuTangFightReverse.mp3']

i = ['cover30.jpg', 'cover12.png', 'cover34.jpg', 'cover36.jpg', 'cover37.jpg', 'cover38.jpg', 'cover14.png', 'cover5 (2).jpg', 'cover7 (2).jpg', 'cover9 (2).jpg', 'cover11 (2).jpg', 'cover2.png', 'cover15 (2).jpg', 'cover16 (2).jpg', 'cover17 (2).jpg', 'cover6.png', 'cover0.jpg', 'cover1.jpg', 'cover2.jpg', 'cover3.jpg', 'cover4.jpg', 'cover5.jpg', 'cover6.jpg', 'cover7.jpg', 'cover8.jpg', 'cover9.jpg', 'cover10.jpg', 'cover11.jpg', 'cover12.jpg', 'cover13.jpg', 'cover14.jpg', 'cover21.jpg', 'cover22.jpg', 'cover23.jpg', 'cover24.jpg', 'cover25.jpg', 'cover26.jpg', 'cover27.jpg', 'cover31.jpg', 'cover32.jpg', 'cover13 (2).jpg', 'cover3.webp', 'cover15.jpg', 'cover16.jpg', 'cover8.png', 'cover33.jpg', 'cover39.jpg', 'cover1 (2).jpg', 'cover17.jpg', 'cover10.png', 'cover18.jpg', 'cover19.jpg', 'cover20.jpg', 'cover28.jpg', 'cover29.jpg', 'cover0.jpeg', 'cover35.jpg', 'cover4.jpeg']



player = []
proot = r'E:\\Code\\musicplayers\\svelte-music-player\\public\\audio'


for x in range(1, len(p)):
    fpath = os.path.join(proot, p[x])

    audio = MP3(fpath)
    dur = round(audio.info.length, 2)

    player.append({
    "id": str(x),
    "name": p[x][:-8],
    "duration": dur,
    "image": "/images/" + i[x],
    "audio": "/audio/" + p[x],
  })

for p in player:
    print(p)