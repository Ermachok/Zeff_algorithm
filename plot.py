import matplotlib.pyplot as plt
import numpy as np

class SnaptoCursor:

    def __init__(self, ax, x, y):
        self.ax = ax
        self.lx = ax.axhline(color='k',linewidth = 0.4)  # the horiz line
        self.ly = ax.axvline(color='k',linewidth = 0.4)  # the vert line
        self.x = x
        self.y = y
        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        indx = min(np.searchsorted(self.x, x), len(self.x) - 1)
        x = self.x[indx]
        y = self.y[indx]
        # update the line positions
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        print('x=%1.2f, y=%1.2f' % (x, y))
        self.ax.figure.canvas.draw()

class Cursor:
    def __init__(self, ax):
        self.ax = ax
        #self.lx = ax.axhline(color='k', linewidth = 0.3 )  # the horiz line
        self.ly = ax.axvline(color='k', linewidth = 0.3 )  # the vert line

        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        # update the line positions
        #self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text('x=%1.2f' % (x))
        self.ax.figure.canvas.draw()

def interactive_legend(ax=None):
    if ax is None:
        ax = plt.gca()
    if ax.legend_ is None:
        ax.legend()

    return InteractiveLegend(ax.get_legend())

class InteractiveLegend(object):
    def __init__(self, legend):
        self.legend = legend
        self.fig = legend.axes.figure

        self.lookup_artist, self.lookup_handle = self._build_lookups(legend)
        self._setup_connections()

        self.update()

    def _setup_connections(self):
        for artist in self.legend.texts + self.legend.legendHandles:
            artist.set_picker(10) # 10 points tolerance

        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def _build_lookups(self, legend):
        labels = [t.get_text() for t in legend.texts]
        handles = legend.legendHandles
        label2handle = dict(zip(labels, handles))
        handle2text = dict(zip(handles, legend.texts))

        lookup_artist = {}
        lookup_handle = {}
        for artist in legend.axes.get_children():
            if artist.get_label() in labels:
                handle = label2handle[artist.get_label()]
                lookup_handle[artist] = handle
                lookup_artist[handle] = artist
                lookup_artist[handle2text[handle]] = artist

        lookup_handle.update(zip(handles, handles))
        lookup_handle.update(zip(legend.texts, handles))

        return lookup_artist, lookup_handle

    def on_pick(self, event):
        handle = event.artist
        if handle in self.lookup_artist:

            artist = self.lookup_artist[handle]
            artist.set_visible(not artist.get_visible())
            self.update()

    def on_click(self, event):
        if event.button == 3:
            visible = False
        elif event.button == 2:
            visible = True
        else:
            return

        for artist in self.lookup_artist.values():
            artist.set_visible(visible)
        self.update()

    def update(self):
        for artist in self.lookup_artist.values():
            handle = self.lookup_handle[artist]
            if artist.get_visible():
                handle.set_visible(True)
            else:
                handle.set_visible(False)
        self.fig.canvas.draw()

    def show(self):
        plt.show()

sht_num = 41567
ch_num = 1

with open ("D:\Ioffe\slowADC\calculations\sht%d\\%d_process_ADC_ch%d_data.txt" %(sht_num, sht_num, ch_num), "r") as file:
    lines = file.readlines()

y = []
x = []

for i in range(1, int(len(lines)/5)):
    line = lines[i*5].split(',')
    x.append(float(line[0]) + 3)

for j in range(1, 11):
    temp = []
    for i in range(1, int(len(lines)/5)):
        line = lines[i*5].split(',')
        temp.append(float(line[j]))
    y.append(temp)

fig, ax = plt.subplots()
for i in range(len(y)):
    ax.plot(x, y[i], label=r"poly %i".format(i) %(i+1), linewidth = 0.9 )

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1),
          ncol=2, borderaxespad=0)
fig.subplots_adjust(right=0.8)
fig.suptitle('Shot number %d' %sht_num,
             va='top', size='large')

leg = interactive_legend()
#cursor = Cursor(ax)
#fig.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)

#cursor = Cursor(ax)
#fig.canvas.mpl_connect('motion_notify_event', cursor.mouse_move)
plt.xlim(100,250)
ax.minorticks_on()
ax.grid()
ax.grid(which='minor', linestyle = '--')
plt.show()



#temp = lines[1].split(',')
#print(temp[0])

