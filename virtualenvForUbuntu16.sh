#Step #1: Install OpenCV dependencies on Ubuntu 16.04

#to refresh and upgrade and pre-installed packages/libraries:
sudo apt-get update
sudo apt-get upgrade

#The cmake  program is used to automatically configure our OpenCV build:
sudo apt-get install build-essential cmake pkg-config

#the name of the module that handles OpenCV GUI operations is highgui
sudo apt-get install libgtk-3-dev

#to optimize various functionalities inside OpenCV
sudo apt-get install libatlas-base-dev gfortran

#Python development headers and libraries for both 
sudo apt-get install python2.7-dev python3.5-dev


#Step #2: Download the OpenCV source
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip
unzip opencv.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
unzip opencv_contrib.zip

#Step #3: Setup your Python environment
cd ~
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

source ~/.bashrc

#Creating your Python virtual environment

mkvirtualenv cv -p python3
workon cv

pip install numpy

#Step #4: Configuring and compiling OpenCV on Ubuntu 16.04

#workon cv
#cd ~/opencv-3.4.1/
#mkdir build
#cd build
#cmake -D CMAKE_BUILD_TYPE=RELEASE \
	#-D CMAKE_INSTALL_PREFIX=/usr/local \
    #-D INSTALL_PYTHON_EXAMPLES=ON \
    #-D INSTALL_C_EXAMPLES=OFF \
    #-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    #-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
    #-D BUILD_EXAMPLES=ON ..

#make -j4

#sudo make install
#sudo ldconfig

#cd /usr/local/lib/python3.5/site-packages/
#sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so

#cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
#ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so


