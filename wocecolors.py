# module for working with WOCE colors
from pylab import array, hstack, vstack, arange, contour, contourf, clim, gca

Slevs = array([34.0, 34.4, 34.66, 34.68, 34.7, 34.74, 35.])

Slevs_fine = hstack( [ arange(33.0, 34.0, 0.2),
                            arange(34.0, 34.4, 0.1), 34.4,
                            arange(34.62,34.68, 0.02),
                            arange(34.68,34.70, 0.005),
                            arange(34.70,34.80, 0.02),
                            arange(34.8, 35.0, 0.05),
                            arange(35.0, 36.0, 0.25)
                        ] )

Tlevs = array([-0.8, -0.4, 0., 1., 2., 3., 12.])
                        
Tlevs_fine = hstack( [ arange(-2.,1.,0.1),
                            arange(1.,3.,0.2),
                            arange(3.,4.,0.5),
                            arange(4.,26.,1.)
                        ] )
                        
# colors
blue = array([ [1,146,191], [65,171,206], [127,198,222], [191,226,238]]) / 255.
orange = array([ [255,158,15], [254,182,64], [254,207,122], [254,231,186]]) / 255.
red = array([[251,0,38],[250,66,75],[250,128,124],[252,192,184]]) / 255.

Scolors = vstack([blue, orange[::-1]])
Tcolors = vstack([blue, red[::-1]])

def contourS(X,Z,S, fine=False, **kwargs):
    """Make a contour plot of S that looks like WOCE"""
    c=contourf(X, Z, S,
        Slevs, colors=Scolors[1:], extend='both', **kwargs)
    c.cmap.set_under(Scolors[0])
    c.cmap.set_over(Scolors[-1])
    clim((Slevs[0],Slevs[-1]))
    gca().set_axis_bgcolor('k')
    if fine:
        cf=contour(X,Z,S, Slevs_fine, colors='k', linewidths=0.25)
        return c,cf
    else:
        return c
        
def contourT(X,Z,T, fine=False, **kwargs):
    """Make a contour plot of S that looks like WOCE"""
    c=contourf(X, Z, T,
        Tlevs, colors=Tcolors[1:], extend='both', **kwargs)
    c.cmap.set_under(Tcolors[0])
    c.cmap.set_over(Tcolors[-1])
    clim((Tlevs[0],Tlevs[-1]))
    gca().set_axis_bgcolor('k')
    if fine:
        cf=contour(X,Z,T, Tlevs_fine, colors='k', linewidths=0.25, linestyles='solid')
        return c,cf
    else:
        return c
