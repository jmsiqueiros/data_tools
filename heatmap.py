import argparse
import numpy as np
import matplotlib.pyplot as plt

X = [[0,0,0,2,0,0,0,0,1,0,0,1,0,1,2,2,1,0,1,0,0,0,0,0,0,0,0,2,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[1,2,2,0,2,0,0,0,2,1,0,0,0,0,0,0,1,0,0,0,2,2,0,2,1,2,0,0,2,2,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,0,0,1,0,1,2,2,2,2,0,2,1,1,1,0,2,1,2,1,0,0,0,2,2,0,0,0,0,2,0],
[1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,2,0,0,0,0,1,0,0,1,0,0,0,1,0],
[0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,2,0]]

# [[0,0,5,3,1,0,14,2,6,4,0,4,0,4,26,9,1,0,2,0,5,4,0,1,6,5,1,6,1,4,1],
# [0,1,5,4,1,0,6,0,2,5,0,3,0,0,0,0,2,5,0,0,2,0,0,0,0,1,0,0,1,0,1],
# [0,0,1,0,1,0,9,1,0,0,1,4,0,3,0,0,1,1,0,0,1,2,1,0,1,7,0,0,2,8,0],
# [3,26,18,0,12,0,15,4,11,9,0,2,1,0,0,0,1,0,1,1,20,16,0,7,26,27,0,0,12,10,0],
# [1,0,3,0,2,2,3,3,2,1,0,1,0,0,0,0,2,2,0,0,0,1,0,0,2,11,1,1,6,3,0],
# [0,0,1,0,0,0,7,4,0,0,0,0,1,3,0,0,0,0,0,0,0,3,0,1,3,3,0,0,0,0,0],
# [9,1,3,2,0,2,45,17,13,15,0,11,11,5,11,2,2,4,5,7,4,5,0,9,53,8,3,0,2,14,0],
# [3,2,7,2,3,0,2,5,3,6,0,1,2,0,2,5,1,7,0,0,0,4,3,0,2,15,0,0,0,8,0],
# [1,1,6,2,0,0,4,6,1,5,0,0,5,1,1,0,0,4,0,0,0,0,0,1,6,8,1,0,9,12,0]]


data = np.array( X )

rows = list(range(1,32))

#rows = ["acceso","accion","actividad","acuerdo","administracion","agricultura","agua","alcald","almorzadero","ambient","andres","animales","apoy","arboles","asociacion","asomoarce","beneficio","bomberos","calidad","campanias","campesino","carbon","cas","centro","cerrito","comunidad","concepcion","conciencia","conocimiento","conserv","contaminacion"]


columns = ['E1','E2','E3','E4','E5','E6','E7','E8','E9']




#  Finishing Touches
fig,ax=plt.subplots()
# using the ax subplot object, we use the same
# syntax as above, but it allows us a little
# bit more advanced control
ax.pcolor(data,cmap=plt.cm.OrRd,edgecolors='k')
ax.set_xticks(np.arange(0,31)+0.5)
ax.set_yticks(np.arange(0,9)+0.5)
 
# Here we put the x-axis tick labels
# on the bottom of the plot.  The y-axis
# command is redundant, but inocuous.
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
# similar syntax as previous examples
ax.set_xticklabels(rows,minor=False,fontsize=20)
ax.set_yticklabels(columns,minor=False,fontsize=20)

ax.autoscale(tight=True) # get rid of whitespace in margins of heatmap

# Here we use a text command instead of the title
# to avoid collision between the x-axis tick labels
# and the normal title position
plt.text(0.5,1.08,'Cerrito word use intensity',
         fontsize=25,
         horizontalalignment='center',
         transform=ax.transAxes
         )
 
# standard axis elements
plt.ylabel('Interviewees',fontsize=20)
plt.xlabel('Words',fontsize=20)
    

plt.show()

