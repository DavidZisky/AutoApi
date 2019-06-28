import os

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://mongo:27017/evedemo')

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

user = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'age': {
            'type': 'integer'
        },
        'experience': {
            'nullable': True
        },
        'alive': {
            'type': 'boolean'
        },
        'title': {
            'type': 'string'
        },
        'inventory': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'primary_artifact': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'artifact',
                'field': '_id',
                'embeddable': True
            }
        },
        'secondary_artifacts': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'artifact',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'address': {
            'type': 'dict',
            'schema': {
                'address': {
                    'type': 'string'
                },
                'city': {
                    'type': 'string'
                },
                'state': {
                    'type': 'string'
                }
            }
        },
        'attack_bonus': {
            'type': 'integer',
            'min': 1,
            'max': 10
        },
        'difficulty': {
            'type': 'float',
            'min': 0.0,
            'max': 1.0
        }
    }
}

artifact = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'cost': {
            'type': 'float'
        },
        'color': {
            'type': 'string'
        },
        'stats': {
            'type': 'dict',
            'schema': {
                'weight': {
                    'type': 'float'
                },
                'length': {
                    'type': 'float'
                },
                'powers': {
                    'type': 'dict',
                    'schema': {
                        'strike': {
                            'type': 'integer'
                        },
                        'deflect': {
                            'type': 'integer'
                        },
                        'speed': {
                            'type': 'integer'
                        }
                    }
                }
            }
        }
    }
}

DOMAIN = {
    'user': user,
    'artifact': artifact,
}
