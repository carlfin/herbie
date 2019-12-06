class StatusConstants:
    STATUS = 'status'
    STATUS_OK = 'ok'
    STATUS_ERROR = 'error'


class ValidatorResponseConstants:
    RESPONSE_KEY = 'response'
    ERROR_MESSAGE = 'error_message'
    VALIDATE_KEY = 'validation_error'
    REQUIRED_KEY = 'required'


class ControllerConstants:
    DELETE_ALL_VERSIONS_MESSAGE = 'entity with key {} deleted from all versions'
    DELETE_FROM_VERSION_MESSAGE = 'entity with key {} deleted from version {}'
    SAVE_MESSAGE = 'entity with key {} created in version {}'
    UPDATE_MESSAGE = 'entity with key {} updated in version {}'
    BUSINESS_ENTITY_NOT_EXIST = 'business entity {} does not exist'
    VERSION_NOT_EXIST = 'version {} does not exist'
    VERSION_MISSING = 'Version is missing'
    KEY = 'key'
    PAYLOAD = 'payload'
    VERSION = 'version'

