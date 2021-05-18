from rest_framework import serializers
from notifications.models import Notification
from accounts.api.serializers import UserSerializer


class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer()

    class Meta:
        model = Notification
        fields = (
            'id',
            'recipient',
            'actor_content_type',
            'actor_object_id',
            'verb',
            'action_object_content_type',
            'action_object_object_id',
            'target_content_type',
            'target_object_id',
            'timestamp',
            'unread',
        )
