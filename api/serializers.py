from rest_framework import serializers

from chat.models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
	messages = MessageSerializer(many=True)
	last_message = serializers.StringRelatedField()
	last_message_date = serializers.DateTimeField()
	profile_title = serializers.StringRelatedField()
	profile_image = serializers.ImageField()
	is_muted = serializers.BooleanField()
	is_pinned = serializers.BooleanField()
	is_read = serializers.BooleanField()
	# unread_messages_count = serializers.IntegerField()
	class Meta:
		model = Chat
		fields = '__all__'