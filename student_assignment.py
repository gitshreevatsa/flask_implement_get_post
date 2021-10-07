
from flask import Flask, request 
import os , json
from copy import deepcopy
app = Flask(__name__)

@app.route('/studentsData', methods = ['GET', 'POST', 'PUT', 'DELETE'])

def get_method():
    if(request.method =='GET'):
        path = os.path.join(os.getcwd(),'student.json')
        f = open(path, 'r')
        f = f.read()
        f = json.loads(f)
        return f


#@app.route('/studentsData', methods = ['GET', 'POST', 'PUT', 'DELETE'])
    if(request.method == 'POST'):
        data = request.get_json()
        path = os.path.join(os.getcwd(),'student.json')
        f = open(path, 'r')
        f = f.read()
        f = json.loads(f)
        a = f['students']
        print(type(data))
        print(type(a))
        """
        def dict_of_dicts_merge(a, data):
            z = {}
            overlapping_keys = a.items() & data.items()
            if(a.items() == data.items()):
                return "Error"
            else:
                for key in overlapping_keys:
                    z[key] = dict_of_dicts_merge(a[key], data[key])
                for key in a.keys() - overlapping_keys:
                    z[key] = deepcopy(a[key])
                for key in data.keys() - overlapping_keys:
                    z[key] = deepcopy(data[key])
                    print(z)
                return z
        lam =  dict_of_dicts_merge(a, data)
        """
        lam = f | data
        new_path = os.path.join(path)
        with open(new_path, 'w') as file:  
            document = json.dump(lam, file)
        return "Updated Successfully"
        
    
    
        


    
        
            
            
            
            

        
    

if __name__ == '__main__':
    app.run(debug= True)