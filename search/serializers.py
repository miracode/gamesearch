from rest_framework import serializers

from .models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('title', 'game_id', 'platform', 'genre', 'release_date',
                  'overview', 'cover_image', 'rating', 
                  # 'players', 'coop', 'youtube', 'publisher',
                  # 'developer',
                  )

        def restore_object(self, attrs):
            print attrs

            return Game(**attrs)
