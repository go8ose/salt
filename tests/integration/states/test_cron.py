# -*- coding: utf-8 -*-

'''
Tests for the cron state
'''

# Import python libs
from __future__ import absolute_import
import logging
import os

log = logging.getLogger(__name__)

# Import Salt Testing libs
from tests.support.case import ModuleCase
from tests.support.paths import TMP
from tests.support.mixins import SaltReturnAssertsMixin




class CronTest(ModuleCase, SaltReturnAssertsMixin):
    def test_cron(self):
        '''
        cron.present test interface
        '''
        name = os.path.join(TMP, 'cron_defaults')
        ret = self.run_state('cron.present', test=True, name=name)
        self.assertSaltNoneReturn(ret)

    def test_hour_division(self):
        '''
        cron.present test interface
        '''
        name = os.path.join(TMP, 'hour_division')
        ret = self.run_state('cron.present', test=True, name=name, hour='*/2')
        self.assertSaltNoneReturn(ret)

    def test_hour_list(self):
        '''
        cron.present test interface
        '''
        name = os.path.join(TMP, 'hour_list')
        ret = self.run_state('cron.present', test=True, name=name, hour='0,1,2,3,4,5')
        self.assertSaltNoneReturn(ret)
