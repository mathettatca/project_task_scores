# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectTaskScores(http.Controller):
#     @http.route('/project_task_scores/project_task_scores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_task_scores/project_task_scores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_task_scores.listing', {
#             'root': '/project_task_scores/project_task_scores',
#             'objects': http.request.env['project_task_scores.project_task_scores'].search([]),
#         })

#     @http.route('/project_task_scores/project_task_scores/objects/<model("project_task_scores.project_task_scores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_task_scores.object', {
#             'object': obj
#         })

