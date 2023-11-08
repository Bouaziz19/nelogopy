import os ,time
from nelogopy import *
os.system("cls")

if __name__ == "__main__" :
    n=run_netlogo("C:/Program Files/NetLogo 6.2.2")
    resize_world(n,0,60,0,60)
    set_background(n,"nelogopy.png")
    tr=pyturtle(n,x=20,y=5,id=0,shape="machine",size_shape=4,color=0,name="zn",labelcolor=0)
    tr2=pyturtle(n,x=5,y=5,id=1,shape="car",size_shape=4,color=0,name="zn",labelcolor=0)
    street( n,fromm=tr,too=tr2,label="street",id_s=0,labelcolor=0,color=0,shape="aa",thickness=0.5)

    # print(distancebetween(n,tr,tr2))
    # print(getxyturtle(n,tr)[1])
    # tr.setxy(4,8)
    for i in range(0,10):
        time.sleep(1)
        tr.fd(1)
        print(tr.distanceto(tr2))
        if i==5:
            # tr.move_to(tr2)
            tr.face_to(tr2)
            tr.set_shape('car')
            tr.hideturtle()
        print("***********  ",i,"  ********")  
        
        
    # n.close_model()
time.sleep(100000000)
