"""rt (i.e. Radio Telescopes) module is for handling real telescope meta-data."""
import os
import pickle
import dreambeam.telescopes

class TelescopeStnBnd(object):
    """Model of one station and one band of a telescope."""
    feed_pat = None
    def __init__(self, stnPos, stnRot):
        """Set the station's position and attitude.""" 
        self.stnPos = stnPos
        self.stnRot = stnRot
    
    def getEJones(self):
        """Create ejones for station based on antenna patterns."""
        ejones = None
        return ejones


class TelescopeWiz():
    """Database over available telescopes patterns."""
    def getTelescope(self, tscopename, beammodel):
        teldatapath = self.tel2path(tscopename, beammodel)
        with open(teldatapath,'rb') as f:
            telescope = pickle.load(f)
        return telescope
    
    def tel2path(self, tscopename, beammodel):
        #Currently it only maps requests to filename
        filename = "teldat_"+tscopename+"_"+beammodel+".p"
        teldatdir = os.path.dirname(dreambeam.telescopes.__file__)+"/"+tscopename+"/data/"
        teldatapath = teldatdir+filename
        return teldatapath
