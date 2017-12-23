# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CriminalCounter
                                 A QGIS plugin
 This plugin helps the policeman in duty to catch criminals
                             -------------------
        begin                : 2017-12-15
        copyright            : (C) 2017 by Group6_Geomatics_TUDelft
        email                : dushenglan940128@163.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CriminalCounter class from file CriminalCounter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CriminalCounter import CriminalCounter
    return CriminalCounter(iface)
