from flask import Flask, jsonify, request, abort, render_template, url_for, redirect
from carDAO import carDAO

#app = Flask(__name__, static_url_path='', static_folder='.')


app = Flask(__name__)

@app.route('/')
def car():
   return render_template('car.html')

#curl "http://127.0.0.1:5000/cars"
@app.route('/cars')
def getAll():
    #print("in getall")
    results = carDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/cars/2"
@app.route('/cars/<int:id>')
def findById(id):
    foundCar = carDAO.findByID(id)

    return jsonify(foundCar)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    car = {
        "name": request.json['name'],
        "model": request.json['model'],
        "price": request.json['price'],
    }
    values =(car['name'],car['model'],car['price'])
    newId = carDAO.create(values)
    car['id'] = newId
    return jsonify(car)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
    foundCar = carDAO.findByID(id)
    if not foundCar:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundCar['name'] = reqJson['name']
    if 'model' in reqJson:
        foundCar['model'] = reqJson['model']
    if 'price' in reqJson:
        foundCar['price'] = reqJson['price']
    values = (foundCar['name'],foundCar['model'],foundCar['price'],foundCar['id'])
    carDAO.update(values)
    return jsonify(foundCar)
        

    

@app.route('/cars/<int:id>' , methods=['DELETE'])
def delete(id):
    carDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)