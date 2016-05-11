from pylab import *
import os

WOCE_Slevs = array([34.0, 34.4, 34.66, 34.68, 34.7, 34.74, 35.])
WOCE_Tlevs = array([-0.8, -0.4, 0., 1., 2., 3., 12.])

WOCE_Slevs_fine = hstack( [ arange(33.0, 34.0, 0.2),
                            arange(34.0, 34.4, 0.1), 34.4,
                            arange(34.62,34.68, 0.02),
                            arange(34.68,34.70, 0.005),
                            arange(34.70,34.80, 0.02),
                            arange(34.8, 35.0, 0.05),
                            arange(35.0, 36.0, 0.25)
                        ] )
                        
WOCE_Tlevs_fine = hstack( [ arange(-2.,1.,0.1),
                            arange(1.,3.,0.2),
                            arange(3.,4.,0.5),
                            arange(4.,26.,1.)
                        ] )


def generate_custom_colormaps():
    # balanced postive definite colormap
    pos_cdict = {'red': (   (0.0, 1.0, 1.0),
                        (0.05, 1.0, 1.0),
                        (0.2, 1.0, 1.0),
                        (0.4, 1.0, 1.0),
                        (0.6, 0.909, 0.909),
                        (0.8, 1.0, 1.0),
                        (1.0, 0.6, 0.6)  ),

             'green': ( (0.0, 1.0, 1.0),
                        (0.05, 1.0, 1.0),
                        (0.2, 0.827, 0.827),
                        (0.4, 0.545, 0.545),
                        (0.6, 0.345, 0.345),
                        (0.8, 0.196, 0.196),
                        (1.0, 0.196, 0.196)  ), 

            'blue': ( (0.0, 1.0, 1.0),
                       (0.05, 1.0, 1.0),
                       (0.2, 0.0, 0.0),
                       (0.4, 0.0, 0.0),
                       (0.6, 0.047, 0.047),
                       (0.8, 0.051, 0.051),
                       (1.0, 0.051, 0.051) )
            }
        
    # blue for negative red for positive white in the middle
    # balanced postive definite colormap
    posneg_cdict={'red':(
                        (0.0, 0.0, 0.0),
                        (0.1, 0.0, 0.0),
                        (0.2, 0.0, 0.0),
                        (0.3, 0.047, 0.047),
                        (0.4, 0.0, 0.0),
                        (0.475, 1.0, 1.0),                    
                        (0.5, 1.0, 1.0),
                        (0.525, 1.0, 1.0),
                        (0.6, 1.0, 1.0),
                        (0.7, 1.0, 1.0),
                        (0.8, 0.909, 0.909),
                        (0.9, 1.0, 1.0),
                        (1.0, 0.6, 0.6)  ),

             'green': (
                         (0.0, 0.2, 0.2),
                         (0.1, 0.2, 0.2),
                         (0.2, 0.717, 0.717),
                         (0.3, 0.886, 0.886),
                         (0.4, 1.0, 1.0),
                         (0.475, 1.0, 1.0),
                        (0.5, 1.0, 1.0),
                        (0.525, 1.0, 1.0),
                        (0.6, 0.827, 0.827),
                        (0.7, 0.545, 0.545),
                        (0.8, 0.345, 0.345),
                        (0.9, 0.196, 0.196),
                        (1.0, 0.196, 0.196)  ), 

            'blue': (
                        (0.0, 0.6, 0.6),
                        (0.1, 1.0, 1.0),
                        (0.2, 1.0, 1.0),
                        (0.3, 0.909, 0.909),
                        (0.4,  0.749,  0.749),
                        (0.475, 1.0, 1.0),        
                        (0.5, 1.0, 1.0),
                       (0.525, 1.0, 1.0),
                       (0.6, 0.0, 0.0),
                       (0.7, 0.0, 0.0),
                       (0.8, 0.047, 0.047),
                       (0.9, 0.051, 0.051),
                       (1.0, 0.051, 0.051) )
            }
            
    # trying to copy the WOCE salinity colormap
    # 0 -> 1 === 34 -> 35
    Slevs = WOCE_Slevs - 34.
    Wblue = array([ [1,146,191], [65,171,206], [127,198,222], [191,226,238]]) / 255.
    Worange = array([ [255,158,15], [254,182,64], [254,207,122], [254,231,186]]) / 255.
    # remember first and last values are ignored, so have to use a hack to get them to show
    eps = 1e-4
    WOCE_sal_cdict = {
            'red': (    (Slevs[0], Wblue[0,0], Wblue[0,0]),
                        (Slevs[0]+eps, Wblue[0,0], Wblue[1,0]),
                        (Slevs[1], Wblue[1,0], Wblue[2,0]),
                        (Slevs[2], Wblue[2,0], Wblue[3,0]),
                        (Slevs[3], Wblue[3,0], Worange[3,0]),
                        (Slevs[4], Worange[3,0], Worange[2,0]),
                        (Slevs[5], Worange[2,0], Worange[1,0]),
                        (Slevs[6]-eps, Worange[1,0], Worange[0,0]),
                        (Slevs[6], Worange[0,0], Worange[0,0])),

             'green': ( (Slevs[0], Wblue[0,1], Wblue[0,1]),
                        (Slevs[0]+eps, Wblue[0,1], Wblue[1,1]),
                        (Slevs[1], Wblue[1,1], Wblue[2,1]),
                        (Slevs[2], Wblue[2,1], Wblue[3,1]),
                        (Slevs[3], Wblue[3,1], Worange[3,1]),
                        (Slevs[4], Worange[3,1], Worange[2,1]),
                        (Slevs[5], Worange[2,1], Worange[1,1]),
                        (Slevs[6]-eps, Worange[1,1], Worange[0,1]),
                        (Slevs[6], Worange[0,1], Worange[0,1])),

            'blue':  ( (Slevs[0], Wblue[0,2], Wblue[0,2]),
                       (Slevs[0]+eps, Wblue[0,2], Wblue[1,2]),
                       (Slevs[1], Wblue[1,2], Wblue[2,2]),
                       (Slevs[2], Wblue[2,2], Wblue[3,2]),
                       (Slevs[3], Wblue[3,2], Worange[3,2]),
                       (Slevs[4], Worange[3,2], Worange[2,2]),
                       (Slevs[5], Worange[2,2], Worange[1,2]),
                       (Slevs[6]-eps, Worange[1,2], Worange[0,2]),
                       (Slevs[6], Worange[0,2], Worange[0,2]) )
            }


    my_cmap = matplotlib.colors.LinearSegmentedColormap('sun', pos_cdict, 1024)
    register_cmap(name='sun', cmap=my_cmap)

    pn_cmap = matplotlib.colors.LinearSegmentedColormap('posneg', posneg_cdict, 1024)
    register_cmap(name='posneg', cmap=pn_cmap)
    
    WOCE_sal_cmap = matplotlib.colors.LinearSegmentedColormap('WOCE_sal', WOCE_sal_cdict, 1024)
    register_cmap(name='WOCE_sal', cmap=WOCE_sal_cmap)

    # SST
    cpt = cpt2seg(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cpt','sst.cpt'))
    sst_palette = matplotlib.colors.LinearSegmentedColormap('palette', cpt, 100)
    register_cmap(name='sst', cmap=sst_palette)

def make_WOCE_salinity():
    set_cmap(get_cmap('WOCE_sal'))
    clim([34.,35.])

    
def cpt2seg(file_name, sym=False, discrete=False):
    """Reads a .cpt palette and returns a segmented colormap.

    sym : If True, the returned colormap contains the palette and a mirrored copy.
    For example, a blue-red-green palette would return a blue-red-green-green-red-blue colormap.

    discrete : If true, the returned colormap has a fixed number of uniform colors.
    That is, colors are not interpolated to form a continuous range. 

    Example :
    >>> _palette_data = cpt2seg('palette.cpt')
    >>> palette = matplotlib.colors.LinearSegmentedColormap('palette', _palette_data, 100)
    >>> imshow(X, cmap=palette)
    """

    dic = {}
    f = open(file_name, 'r')
    rgb = loadtxt(f)
    rgb = rgb/255.
    s = shape(rgb)
    colors = ['red', 'green', 'blue']
    for c in colors:
        i = colors.index(c)
        x = rgb[:, i+1]

        if discrete:
            if sym:
                dic[c] = zeros((2*s[0]+1, 3), dtype='float32')
                dic[c][:,0] = linspace(0,1,2*s[0]+1)
                vec = concatenate((x ,x[::-1]))
            else:
                dic[c] = zeros((s[0]+1, 3), dtype='float32')
                dic[c][:,0] = linspace(0,1,s[0]+1)
                vec = x
            dic[c][1:, 1] = vec
            dic[c][:-1,2] = vec

        else:
            if sym:
                dic[c] = zeros((2*s[0], 3), dtype='float32')
                dic[c][:,0] = linspace(0,1,2*s[0])
                vec = concatenate((x ,x[::-1]))
            else:
                dic[c] = zeros((s[0], 3), dtype='float32')
                dic[c][:,0] = linspace(0,1,s[0])
                vec = x
            dic[c][:, 1] = vec
            dic[c][:, 2] = vec

    return dic



