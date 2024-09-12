# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class project_task_scores(models.Model):
    _inherit = 'project.task'
    
    taskscore = fields.Float(string="Task scores",digits = (16,2))

    @api.constrains('taskscore')
    def _check_subtask_score(self):
        for task in self:
            if task.parent_id:
                parent_task = task.parent_id
                total_subtask_score = sum(parent_task.child_ids.mapped('taskscore'))

                # If the total subtask score exceeds the parent task's score, raise an error
                if total_subtask_score > parent_task.taskscore:
                    raise ValidationError(
                        "The total score of subtasks ({}) exceeds the score of the parent task ({})."
                        .format(total_subtask_score, parent_task.taskscore)
                    )
