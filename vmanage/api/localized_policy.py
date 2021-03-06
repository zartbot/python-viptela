"""Cisco vManage Localized Policy API Methods.
"""

from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods


class LocalizedPolicy(object):
    """vManage Localized Policy API

    Responsible for DELETE, GET, POST, PUT methods against vManage
    Localized Policy.

    """
    def __init__(self, session, host, port=443):
        """Initialize Localized Policy object with session parameters.

        Args:
            session (obj): Requests Session object
            host (str): hostname or IP address of vManage
            port (int): default HTTPS 443

        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f'https://{self.host}:{self.port}/dataservice/'

    def delete_localized_definition(self, definition, definitionId):
        """Deletes the specified policy definition which include:
        'qosmap','rewriterule','acl','aclv6','vedgeroute'

        Args:
            definition (str): One of the above policy types
            definitionId (str): ID of the policy definition

        Returns:
            result (dict): All data associated with a response.

        """

        api = f"template/policy/definition/{definition}/{definitionId}"
        url = self.base_url + api
        response = HttpMethods(self.session, url).request('DELETE')
        result = ParseMethods.parse_status(response)
        return result

    def delete_localized_policy(self, policy_id):
        """Deletes the specified localized policy

        Args:
            policyId (str): ID of the active localized policy
        Returns:
            result (dict): All data associated with a response.

        """

        api = f"template/policy/vedge/{policy_id}"
        url = self.base_url + api
        response = HttpMethods(self.session, url).request('DELETE')
        result = ParseMethods.parse_status(response)
        return result

    def get_localized_definition(self, definition):
        """Obtain a list of various policy definitions which include:
        'qosmap','rewriterule','acl','aclv6','vedgeroute'

        Args:
            definition (str): One of the above policy types

        Returns:
            result (dict): All data associated with a response.

        """

        api = f"template/policy/definition/{definition}"
        url = self.base_url + api
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_localized_policy(self):
        """Obtain a list of all configured localized policies

        Returns:
            result (dict): All data associated with a response.

        """

        api = "template/policy/vedge"
        url = self.base_url + api
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result
