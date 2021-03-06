# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Tests the following set of sequences:
a-b-c:      (7X)
a-d-e:      (2X)
a-f-g-a-h:  (1X)

We want to insure that when we see 'a', that we predict 'b' with highest
confidence, then 'd', then 'f' and 'h' with equally low confidence. 

We expect the following input prediction scores:
inputPredScore_at1        :  0.7
inputPredScore_at2        :  1.0
inputPredScore_at3        :  1.0
inputPredScore_at4        :  1.0

"""


from nupic.frameworks.prediction.helpers import importBaseDescription

config = dict(
              sensorVerbosity=0,
              spVerbosity=0,
              tpVerbosity=0,
              ppVerbosity=3,
              
              filenameTrain = 'confidence/confidence1.csv',
              filenameTest = 'confidence/confidence1.csv',

              iterationCountTrain=None,
              iterationCountTest=None,
              trainTPRepeats = 3,
              
              trainTP=True,
              )
              
mod = importBaseDescription('../base/description.py', config)
locals().update(mod.__dict__)


