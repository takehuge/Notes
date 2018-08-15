import matplotlib
matplotlib.use('tkAgg')  # bring upfront
import matplotlib.pyplot as plt
from IPython.terminal.embed import InteractiveShellEmbed

shell = InteractiveShellEmbed()
shell.enable_matplotlib()

fig, axes = plt.subplots()
axes.plot([1, 2, 3, 4, 5], [1, 2, 1, 2, 1])
plt.show(block=False)

shell()
