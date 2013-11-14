from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plug.models import Bug
from django.utils.translation import ugettext as _

class BugPlugin(CMSPluginBase):
    model = Bug # Model where data about this plugin is saved
    name = _("Bug Plugin") # Name of the plugin
    render_template = "bug.html" # template to render the plugin with

plugin_pool.register_plugin(BugPlugin) # register the plugin
