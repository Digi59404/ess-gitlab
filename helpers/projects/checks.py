from gitlab import exceptions
from helpers.projects.methods import *

def check_project_visbility(gl, project_id):
    try:
        attributes = get_project_attributes(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_visbility': '403 Forbidden'}
    return {'project_visbility': attributes['visibility']}

def check_project_pages_access_level(gl, project_id):
    try:
        attributes = get_project_attributes(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_pages_access_level': '403 Forbidden'}
    return {'project_pages_access_level': attributes['pages_access_level']}

def check_project_security_and_compliance_enabled(gl, project_id):
    try:
        attributes = get_project_attributes(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_security_and_compliance_enabled': '403 Forbidden'}
    return {'project_security_and_compliance_enabled': attributes['security_and_compliance_enabled']}

def check_project_approvals_before_merge(gl, project_id):
    try:
        attributes = get_project_attributes(gl, project_id)
    except exceptions.GitlabGetError:
        return {'roject_approvals_before_merge': '403 Forbidden'}
    return {'roject_approvals_before_merge': attributes['approvals_before_merge']}

def check_project_push_rules_unsigned_commits(gl, project_id):
    try:
        push_rules = get_project_push_rules(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_push_rules_unsigned_commits': '403 Forbidden'}
    return {'project_push_rules_unsigned_commits': push_rules.reject_unsigned_commits}

def check_project_push_rules_comitter_check(gl, project_id):
    #Committer restriction: Users can only push commits to this repository that were committed with one of their own verified emails.
    try:
        push_rules = get_project_push_rules(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_push_rules_comitter_check': '403 Forbidden'}
    return {'project_push_rules_comitter_check': push_rules.commit_committer_check}

def check_project_push_rules_comitter_check(gl, project_id):
    try:
        protected_branches = get_protectedbranches(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_protected_branches': '403 Forbidden'}
    for i in protected_branches:
        protected_branches = i
    return {'project_protected_branches': protected_branches._attrs}

def get_project_info(gl, project_id):
    try:
        attributes = get_project_attributes(gl, project_id)
        project_languages = get_project_languages(gl, project_id)
        project_contributors = get_project_contributors(gl, project_id)
    except exceptions.GitlabGetError:
        return {'project_info': '403 Forbidden'}
    return {'project_info': {'name': attributes['name'], 'name_with_namespace': attributes['name_with_namespace'], 'description': attributes['description'], 'web_url': attributes['web_url'], 'project_languages': project_languages, 'project_contributors': project_contributors}}

def get_project_all_keys(gl, project_id):
    project_all_keys = {}
    try:
        access_tokens = get_project_access_tokens(gl, project_id)
        for i in access_tokens:
            access_tokens = i
        try:
            project_all_keys.update({'project_access_tokens': access_tokens._attrs})
        except:
            project_all_keys.update({'project_access_tokens': access_tokens})
    except exceptions.GitlabGetError:
        project_all_keys.update({'project_access_tokens': '403 Forbidden'})
    except exceptions.GitlabAuthenticationError:
        project_all_keys.update({'project_access_tokens': '401 Unauthorized'})
    try:
        deployment_tokens = get_project_deployment_tokens(gl, project_id)
        for i in deployment_tokens:
            deployment_tokens = i
        try:
            project_all_keys.update({'project_deployment_tokens': deployment_tokens._attrs})
        except:
            project_all_keys.update({'project_deployment_tokens': deployment_tokens})
    except exceptions.GitlabGetError:
        project_all_keys.update({'project_deployment_tokens': '403 Forbidden'})
    except exceptions.GitlabAuthenticationError:
        project_all_keys.update({'project_deployment_tokens': '401 Unauthorized'})
    except exceptions.GitlabListError:
        project_all_keys.update({'project_deployment_tokens': '403 Forbidden'})
    try:
        project_keys = get_project_keys(gl, project_id)
        for i in project_keys:
            project_keys = i
        try:
            project_all_keys.update({'project_keys': project_keys._attrs})
        except:
            project_all_keys.update({'project_keys': project_keys})
    except exceptions.GitlabGetError:
        project_all_keys.update({'project_keys': '403 Forbidden'})
    except exceptions.GitlabAuthenticationError:
        project_all_keys.update({'project_keys': '401 Unauthorized'})
    except exceptions.GitlabListError:
        project_all_keys.update({'project_keys': '403 Forbidden'})
    return {'project_all_keys': project_all_keys}