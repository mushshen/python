#!/usr/bin/env python
#learn url:https://www.joinquant.com/post/3616?f=home&m=banner

import jqdata
jqdata.get_money_flow('000001.XSHE', '2015-12-25', '2015-12-30', fields="change_pct")
