{% extends "modules/modulefile.tcl" %}
{% block footer %}

lappend auto_path /apps/modulelibs/UsefulModuleFunctions
package require modulefunctions 1.0

modulefunctions::mustBeMemberToLoad ag-archpc-castep

{% endblock %}

