#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from datetime import datetime, timedelta
from model import Game, User
from google.appengine.api import mail, app_identity


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Reminder(webapp2.RequestHandler):
    def get(self):
        """Runs everyday, queries db for open games last modified more than 72
        hours ago and sends the game owner a reminder email"""
        three_days_ago = datetime.now() - timedelta(days=3)
        app_name = app_identity.get_application_id()

        subject = "You have had an open game for 3 days now!"
        open_games = Game.query(Game.over == False).\
            filter(Game.modified < three_days_ago)

        for game in open_games:
            user = game.user_name.get()
            if user.email_address:
                body = "Hello {}, you have an open game! Please come back and play!".\
                    format(user.user_name)
                mail.send_mail('noreply@{}.appspotmail.com'.format(app_name),
                    user.email_address, subject, body)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cron/reminder', Reminder)
], debug=True)
