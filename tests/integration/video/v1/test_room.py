# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoomTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "unique_name",
                "max_participants": 10,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": "",
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/Rooms',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "max_participants": 10,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": "",
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_p2p_basic_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "peer-to-peer-basic",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "room1",
                "max_participants": 10,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": "",
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "rooms": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "rooms"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms.list()

        self.assertIsNotNone(actual)

    def test_read_with_status_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "rooms": [
                    {
                        "sid": "RM4070b618362c1682b2385b1f9982833c",
                        "status": "completed",
                        "date_created": "2017-04-03T22:21:49Z",
                        "date_updated": "2017-04-03T22:21:51Z",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "peer-to-peer",
                        "enable_turn": true,
                        "unique_name": "RM4070b618362c1682b2385b1f9982833c",
                        "status_callback": null,
                        "status_callback_method": "POST",
                        "end_time": "2017-04-03T22:21:51Z",
                        "duration": 2,
                        "max_participants": 10,
                        "record_participants_on_connect": false,
                        "video_codecs": [
                            "VP8"
                        ],
                        "media_region": "us1",
                        "url": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c",
                        "links": {
                            "participants": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c/Participants",
                            "recordings": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c/Recordings"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms?Status=completed&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms?Status=completed&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "rooms"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="in-progress")

        values = {'Status': "in-progress", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "completed",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "unique_name",
                "max_participants": 10,
                "status_callback_method": "POST",
                "status_callback": "",
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "end_time": "2015-07-30T20:00:00Z",
                "duration": 10,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(status="in-progress")

        self.assertIsNotNone(actual)
