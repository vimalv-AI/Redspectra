import glob
import shutil
for file in glob.glob('lose/*.png'):
    print(file)
    shutil.move(file, 'plot/')


