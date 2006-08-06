import datetime
import md5

from zookeepr.tests.functional import *

class TestRegisterController(ControllerTest):

    def test_registration_confirmation(self):
        # insert registration model object
        timestamp = datetime.datetime.now()
        email_address = 'testguy@testguy.org'
        password = 'password'
        r = model.Registration(timestamp=timestamp,
                               email_address=email_address,
                               password=password,
                               activated=False)
        url_hash = r.url_hash
        print url_hash
        self.objectstore.save(r)
        self.objectstore.flush()
        rid = r.id
        print r
        # clear so that we reload the object later
        self.objectstore.clear()
        
        # visit the link
        response = self.app.get('/register/confirm/' + url_hash)
        response.mustcontain('Thanks for confirming your registration')
        
        # test that it's activated
        r = self.objectstore.get(model.Registration, rid)
        self.assertEqual(True, r.activated, "registration was not activated")

        # clean up
        r = self.objectstore.get(model.Registration, rid)
        self.objectstore.delete(r)
        self.objectstore.flush()

    def test_registration_confirmation_invalid_url_hash(self):
        """test that an invalid has doesn't activate anything"""
        self.assertEmptyModel(model.Registration)

        response = self.app.get('/register/confirm/nonexistent', status=404)
