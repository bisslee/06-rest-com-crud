from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    
    {
        'hotel_id':'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 430.00,
        'cidade': 'Sampa'        
    },
    {
        'hotel_id':'beta',
        'nome': 'BEta Hotel',
        'estrelas': 2.3,
        'diaria': 930.00,
        'cidade': 'Rio Janeiro'        
    },
    {
        'hotel_id':'gama',
        'nome': 'Gama Hotel',
        'estrelas': 4.1,
        'diaria': 230.00,
        'cidade': 'Florianópolis'        
    },
    {
        'hotel_id':'omicron',
        'nome': 'Omicron Hotel',
        'estrelas': 3.1,
        'diaria': 170.00,
        'cidade': 'Samap'        
    },
    
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    arqumentos = reqparse.RequestParser()
    arqumentos.add_argument('nome')
    arqumentos.add_argument('estrelas')
    arqumentos.add_argument('diaria')
    arqumentos.add_argument('cidade')
        
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id']==hotel_id:
                return hotel
        return None
    
    def load_novo(hotel_id):
        dados = Hotel.arqumentos.parse_args()
        novo_hotel = HotelModel(hotel_id, **dados)
        
        return novo_hotel; 
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel, 200
        return {'message': 'Hotel not found'}, 404
    
    def post(self, hotel_id):       
        hotel_objeto = Hotel.load_novo(hotel_id)   
        novo_hotel = hotel_objeto.json()     
        hoteis.append(novo_hotel)        
        return novo_hotel, 201
    
    def put(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        hotel_objeto = Hotel.load_novo(hotel_id)   
        novo_hotel = hotel_objeto.json()     
        if hotel:           
            hotel.update(novo_hotel)
            return hotel, 200
        
        hoteis.append(novo_hotel)
        return novo_hotel, 201
        
    def delete(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)    
        if hotel:           
            hoteis.remove(hotel)
            return  {'message': 'hotel apagado'}, 200
        return {'message': 'hotel não encontrado'}, 204