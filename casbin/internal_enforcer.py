# Copyright 2021 The casbin Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from casbin.core_enforcer import CoreEnforcer
from casbin.model.policy_op import PolicyOp


class InternalEnforcer(CoreEnforcer):
    """
    InternalEnforcer = CoreEnforcer + Internal API.
    """

    async def _add_policy(self, sec, ptype, rule):
        """adds a rule to the current policy."""
        rule_added = self.model.add_policy(sec, ptype, rule)
        if not rule_added:
            return rule_added

        if self.adapter and self.auto_save:
            if await self.adapter.add_policy(sec, ptype, rule) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rule_added

    async def _add_policies(self, sec, ptype, rules):
        """adds rules to the current policy."""
        rules_added = self.model.add_policies(sec, ptype, rules)
        if not rules_added:
            return rules_added

        if self.adapter and self.auto_save:
            if hasattr(self.adapter, "add_policies") is False:
                return False

            if await self.adapter.add_policies(sec, ptype, rules) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rules_added

    async def _update_policy(self, sec, ptype, old_rule, new_rule):
        """updates a rule from the current policy."""
        rule_updated = self.model.update_policy(sec, ptype, old_rule, new_rule)

        if not rule_updated:
            return rule_updated

        if self.adapter and self.auto_save:

            if await self.adapter.update_policy(sec, ptype, old_rule, new_rule) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rule_updated

    async def _update_policies(self, sec, ptype, old_rules, new_rules):
        """updates rules from the current policy."""
        rules_updated = self.model.update_policies(sec, ptype, old_rules, new_rules)

        if not rules_updated:
            return rules_updated

        if self.adapter and self.auto_save:

            if await self.adapter.update_policies(sec, ptype, old_rules, new_rules) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rules_updated

    async def _remove_policy(self, sec, ptype, rule):
        """removes a rule from the current policy."""
        rule_removed = self.model.remove_policy(sec, ptype, rule)
        if not rule_removed:
            return rule_removed

        if self.adapter and self.auto_save:
            if await self.adapter.remove_policy(sec, ptype, rule) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rule_removed

    async def _remove_policies(self, sec, ptype, rules):
        """RemovePolicies removes policy rules from the model."""
        rules_removed = self.model.remove_policies(sec, ptype, rules)
        if not rules_removed:
            return rules_removed

        if self.adapter and self.auto_save:
            if hasattr(self.adapter, "remove_policies") is False:
                return False

            if await self.adapter.remove_policies(sec, ptype, rules) is False:
                return False

            if self.watcher:
                self.watcher.update()

        return rules_removed

    async def _remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """removes rules based on field filters from the current policy."""
        rule_removed = self.model.remove_filtered_policy(
            sec, ptype, field_index, *field_values
        )
        if not rule_removed:
            return rule_removed

        if self.adapter and self.auto_save:
            if (
                await self.adapter.remove_filtered_policy(
                    sec, ptype, field_index, *field_values
                )
                is False
            ):
                return False

            if self.watcher:
                self.watcher.update()

        return rule_removed

    async def _remove_filtered_policy_returns_effects(
        self, sec, ptype, field_index, *field_values
    ):
        """removes rules based on field filters from the current policy."""
        rule_removed = self.model.remove_filtered_policy_returns_effects(
            sec, ptype, field_index, *field_values
        )
        if len(rule_removed) == 0:
            return rule_removed

        if self.adapter and self.auto_save:
            if (
                await self.adapter.remove_filtered_policy(
                    sec, ptype, field_index, *field_values
                )
                is False
            ):
                return False

            if self.watcher:
                self.watcher.update()

        return rule_removed
