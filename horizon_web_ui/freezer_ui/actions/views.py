# Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon_web_ui.freezer_ui.actions import tables as actions_tables
from horizon_web_ui.freezer_ui.api import api as freezer_api


class IndexView(tables.DataTableView):
    name = _("Jobs")
    slug = "actions"
    table_class = actions_tables.ActionsTable
    template_name = ("freezer_ui/actions/index.html")

    def has_more_data(self, table):
        return self._has_more

    def get_data(self):
        backups, self._has_more = freezer_api.actions_list(
            self.request,
            offset=self.table.offset)

        return backups