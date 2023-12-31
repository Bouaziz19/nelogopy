
# Project  nelogopy 

nelogopy : Usage netlogo by python


## Developer by

- BOUAZIZ Nourddine : [@Bouaziz19](https://github.com/Bouaziz19)


## Installation



1- install netlogo 🔗
 
[![Netlogo](https://ccl.northwestern.edu/netlogo/images/netlogo-title-wide-60.jpg)](https://ccl.northwestern.edu/netlogo/download.shtml)

2-install nelogopy
```bash
conda install openjdk -y
pip install nelogopy
pip install nelogopy --upgrade
```
3- VS Code

Set Default Terminal In VS Code :Command Line Interface (CLI)
[🔗](https://www.w3schools.io/editor/vscode-change-default-terminal/)
[🔗](https://stackoverflow.com/questions/44435697/change-the-default-terminal-in-visual-studio-code)

## Example TEST

 
```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()

```
## Colors

Colors 

![Colors](https://ccl.northwestern.edu/netlogo/docs/images/colors.jpg)


## Usage/Examples
 
1- pyturtle
 
```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()

```
2-set_background
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    path_image ="path/to/image/nelogopy.png"
    # path_image= "C:/Nouveau dossier/nelogopy/Examples/nelogopy.png"
    set_background(n,path_image)
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()
```
3-street
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()
```
4-Fd
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
    n.close_model()
```
5-netlogoshow
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")
        word=str(car01.id) +"  " +str(i)
        netlogoshow(n,word)  
        print(word)
        car01.fd(1)
    n.close_model()
```
6-distanceto
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        word=car01.distanceto(car02)
        print(word)
        netlogoshow(n,word)
    n.close_model()
```
7-face_to
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i==5:
            car01.face_to(car02)
    n.close_model()
```
8-move_to
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i==5:
            car01.move_to(car02)
            
    n.close_model()
```
9-hideturtle
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i==5:
            car01.hideturtle()
            
    n.close_model()
```
10-set_shape
 ```python
 import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,100):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i==5:
            car01.set_shape('default')
            
    n.close_model()
```

11-getxyturtle
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        xy=getxyturtle(n,car01)
        x=xy[0]
        y=xy[1]
        print("xy : ",xy)
        print("x : ",x)
        print("y : ",y)
    n.close_model()
```
12-setxy
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,100):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i==5:
            car01.setxy(10,10)
            
    n.close_model()
```
13-distancebetween
 ```python
import time
from nelogopy.nelogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        word=distancebetween(n,car01,car02)
        print(word)
    n.close_model()
```
