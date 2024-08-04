from flask import Response, jsonify, request
from flask_restx import Api, Namespace, Resource

from src.music.youtubeAPIService import YoutubeAPIService
from src.rcmd.rcmdService import RcmdService
from src.rcmd.rcmdDto import CreateRcmdDto

namespace = Namespace('rcmd', description='API operations')

@namespace.route('/openai')
class RcmdController(Resource):
    def __init__(self, *args, **kwargs):
        self.service = RcmdService()
        self.music_service = YoutubeAPIService()
        super().__init__(*args, **kwargs)
    
    def post(self): # Recommend  
        user_id = request.json['user_id']
        diary = request.json['diary']
        emotions = request.json['emotions'] if 'emotions' in request.json else []
        filters = request.json['filters'] if 'filters' in request.json else {}
        
        dto = CreateRcmdDto(user_id, diary, emotions, filters)
        result = self.service.recommend(dto)        
        
        ### TEST MUSIC API ###
        # musics = [
        #     {
        #         "artist": "The Beatles",
        #         "correctness": 8,
        #         "genre": "Rock",
        #         "title": "Here Comes the Sun"
        #     },
        #     {
        #         "artist": "Pharrell Williams",
        #         "correctness": 9,
        #         "genre": "Pop",
        #         "title": "Happy"
        #     },
        #     {
        #         "artist": "The Beatles",
        #         "correctness": 7,
        #         "genre": "Rock",
        #         "title": "Good Day Sunshine"
        #     }
        # ]
        
        for music in result.musics:
            music['url'] = self.music_service.search(music['title'], music['artist'])
        
        return result.musics
    
    def put(self): # Train
        return {'message': 'Hello, world!'}