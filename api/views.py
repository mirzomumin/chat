from rest_framework import generics, permissions
from django.db.models import Count, Q, F, Case, When, OuterRef, Value, BooleanField

from .serializers import MessageSerializer, ChatSerializer
from chat.models import Chat, Message
from account.models import Account
# Create your views here.


class ChatListView(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = ChatSerializer
	queryset = Chat.objects.annotate(
		last_message = (Message.objects
			.filter(chat__id=OuterRef('id'))
			.order_by('-created_at')
			.values('text')[:1]),
		last_message_date = (Message.objects
			.filter(chat__id=OuterRef('id'))
			.order_by('created_at')
			.values('created_at')[:1])
	)

	def get_queryset(self):
		return self.queryset.filter(members=self.request.user).annotate(
			#profile title
			profile_title = Case(
				When(is_group=True, then=F('title')),
				When(is_group=False,
					then=Account.objects
					.exclude(id=self.request.user.id)
					.filter(chat__id=OuterRef('id'))
					.values('username')[:1]),
				default=Value('None Title')),

			#profile title
			profile_image = Case(
				When(is_group=True, then=F('avatar')),
				When(is_group=False, then=Account.objects
					.exclude(id=self.request.user.id)
					.filter(chat__id=OuterRef('id'))
					.values('avatar')[:1]),
				# default=Value('None Image')
			),

			#is_muted
			is_muted = Case(
				When(muted=self.request.user, then=True),
				default=False,
				output_field=BooleanField()
			),

			# is_pinned
			is_pinned = Case(
				When(pinned=self.request.user, then=True),
				default=False,
				output_field=BooleanField()
			),

			# is_read
			is_read = Case(
				When(~Q(messages__from_user=self.request.user) & Q(messages__read=self.request.user),
					then=True),
				default=False,
				output_field=BooleanField()
			),

			# unread messages count
			# unread_messages_count = Count('messages', distinct=True),
			# distinct=True
		).order_by('-is_pinned', 'last_message_date').distinct('is_pinned', 'last_message_date')