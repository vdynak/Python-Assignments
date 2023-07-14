#victoria dynak
#victoria.dynak61#login.cuny.edu
#november 27 2022
#unix cloning

#!/bin/bash
git clone https://github.com/HunterCSci127/CSci127
cd CSci127
mkdir projects
mv averageImage.py projects
mkdir pictures
mv *.png pictures
ls |grep ".py" | wc-l
