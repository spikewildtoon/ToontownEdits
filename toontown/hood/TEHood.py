from pandac.PandaModules import *
import ToonHood
from toontown.town import TETownLoader
from toontown.safezone import TESafeSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class TEHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = Test
        self.townLoaderClass = TETownLoader.TETownLoader
        self.safeZoneLoaderClass = TESafeZoneLoader.TESafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_DL.dna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_8/dna/winter_storage_DL.dna'],
         WACKY_WINTER_DECORATIONS: ['phase_8/dna/winter_storage_DL.dna'],
         HALLOWEEN_PROPS: ['phase_8/dna/halloween_props_storage_DL.dna'],
         SPOOKY_PROPS: ['phase_8/dna/halloween_props_storage_DL.dna']}
        self.skyFile = 'phase_8/models/props/DL_sky'
        self.titleColor = (1.0, 0.9, 0.5, 1.0)

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('TEHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('TEHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)

