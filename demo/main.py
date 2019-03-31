from __future__ import absolute_import

from demo import app, log


def main():
    log.info('>>>>>> Starting {0} in ENV {1}'.format(app.config['TITLE'], app.config['ENV']))
    # from demo.api.index_api import ns as user_api
    # api.add_namespace(user_api)


if __name__ == '__main__':
    main(debug=True)

