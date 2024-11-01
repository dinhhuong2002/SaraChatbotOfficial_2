# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa.core.agent import Agent
from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType, SessionStarted, ActionExecuted, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# Chatbot gửi lời chào và đưa ra các lựa chọn, băt đàu phiên nói chuyện.
class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:
        # Gửi sự kiện bắt đầu phiên
        events = [SessionStarted()]

        # Gửi lời chào
        dispatcher.utter_message(text="Xin chào, mình là iTalk - trợ lý của bạn.")

        # Gửi các buttons lựa chọn
        buttons = [
            {"title": "Đăng ký tài khoản", "payload": "/sign_up"},
            {"title": "Đăng nhập", "payload": "/sign_in", "url": "https://bit.ly/4cwD0kX"},
            {"title": "Nạp GO", "payload": "/add_GO"}
        ]
        dispatcher.utter_message(text="Mình có thể giúp gì cho bạn?", buttons=buttons)

        # Gửi sự kiện kết thúc hành động
        events.append(ActionExecuted("action_listen"))

        return events


class ActionDefaultFallback(Action):
    def name(self) -> str:
        return "action_fallback"

    # def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
    #     dispatcher.utter_message(text="Xin lỗi, tôi chưa hiểu rõ  của bạn. Vui lòng đợi, chúng tôi sẽ chuyển bạn đến bộ phận CSKH.")
    #     dispatcher.utter_message(text="Để giải đáp vấn đề của bạn, bạn hãy liên hệ: 0984.650.154 hoặc fanpage [https://www.facebook.com/ioe.vn].")
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Custom behavior for fallback
        # dispatcher.utter_message(text="I'm sorry, I didn't quite understand that. Could you rephrase?")
        dispatcher.utter_message(text="Xin lỗi, mình chưa hiểu ý của bạn. Bạn có muốn liên hệ với CSKH không?")
        # dispatcher.utter_message(text="Để giải đáp vấn đề của bạn, bạn hãy liên hệ: 0984.650.154 hoặc fanpage [ioe.vn](https://www.facebook.com/ioe.vn).")
        buttons = [
            {"title": "Có", "payload": "/help_ioe"},
            {"title": "Không", "payload": "/deny"},
        ]
        # Optionally, you can revert the last user utterance
        return [UserUtteranceReverted()]
        # return []
