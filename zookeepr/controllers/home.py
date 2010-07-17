import logging
import zookeepr.lib.helpers as h
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from zookeepr.model import meta
from zookeepr.model.db_content import DbContent, DbContentType

from zookeepr.lib.base import BaseController, render
from zookeepr.lib.ssl_requirement import ssl_check


log = logging.getLogger(__name__)


class HomeController(BaseController):
    def __before__(self, **kwargs):
        ssl_check(ssl_required=['signin', 'new'])

    def index(self):
        """The home page of the website.

        If the user has not signed in, then they are presented with the
        default page.

        Otherwise, they're shown the customised page.

        We rely on `c.signed_in_person` containing the Person object for
        the currently signed in user, but we don't want to redirect to
        the signin action if we're not signed in so we duplicate the
        __before__ code from SecureController here.
        """

        if 'signed_in_person_id' in session:
            c.signed_in_person = self.dbsession.query(Person).filter_by(id=session['signed_in_person_id']).one()

        return render('/home.mako')
