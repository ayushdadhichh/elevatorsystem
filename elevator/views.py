from django.shortcuts import render
import time
class elevate:
    def __init__(self, name, status, work, floor_status):
        self.name = name
        self.status = status
        self.work = work
        self.floor_status=floor_status
    def start(self):
        self.status='busy'
        self.work='start'
    def stop(self,point):
        self.floor_status=point
        self.work='stop'
    def up(self):
        self.status='busy'
        self.work='moving up'
    def down(self):
        self.status='busy'
        self.work='moving down'
    def open(self):
        self.status='busy'
        self.work='open'
    def close(self):
        self.status='available'
        self.work='close'
    


def home(request):
    return render(request,"status.html")

def display(request):
    num_elevators = request.GET.get('elevator')
    num_floors = request.GET.get('floor')
    fnum=request.GET.get('vfloor',0)
    
    print("\nSelect floor:")
    choice = int(fnum)
    
    ele1=elevate('Elevator 1', 'available','stop',0)
    ele2=elevate('Elevator 2', 'available','stop',0)

    if choice ==ele1.floor_status or choice==ele2.floor_status:
        params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
        return render(request,"status copy.html",params)
    if ele1.status=='available':
        while True:
            ele1.start()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            if choice>ele1.floor_status:
                ele1.up()
            else:
                ele1.down()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele1.stop(choice)
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele1.open()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele1.close()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            return render(request,"status copy.html",params)
            
    elif ele2.status=='available':
        while True:
            ele2.start()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            if choice>ele2.floor_status:
                ele2.up()
            else:
                ele2.down()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele2.stop(choice)
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele2.open()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            render(request,"status copy.html",params)
            time.sleep(1)
            ele2.close()
            params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
            return  render(request,"status copy.html",params)
            
    

    params={'floor':num_floors,'elevator':num_elevators,'name':ele1.name,'status':ele1.status,'work':ele1.work, 'vfloor':ele1.floor_status,'name2':ele2.name,'status2':ele2.status,'work2':ele2.work, 'vfloor2':ele2.floor_status}
    return render(request,"status copy.html",params)
