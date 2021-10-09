from flask import Flask, request 
import os , json
app = Flask(__name__)

@app.route('/studentsData', methods = ['GET', 'POST', 'PUT', 'DELETE'])

def get_method():
    if(request.method =='GET'):
        path = os.path.join(os.getcwd(),'student.json')
        f = open(path, 'r')
        f = f.read()
        f = json.loads(f)
        return f


#@app.route('/studentsData', methods = ['GET', 'POST', 'PUT', 'DELETE']) add new thing to whole file
    if(request.method == 'POST'):
        data = request.get_json()
        print(list(data.keys()))
        path = os.path.join(os.getcwd(),'student.json')
        f = open(path, 'r')
        f = f.read()
        f = json.loads(f)
        a = f['students']
        a_list = list(a)
        print(data['id'])
        overlap = data['id']
        if(overlap in a_list):
            return "Error"
        else:
            a[data['id']] = {"name" : data['name']}
            new_path = os.path.join(path)
            with open(new_path, 'w') as file:  
                document = json.dump(f, file)
            return "Updated Successfully"
        
 

if __name__ == '__main__':
    app.run(debug= True)


