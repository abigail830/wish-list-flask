from __future__ import absolute_import

from demo import app, log


def main():
    log.info('>>>>>> Starting {0} in ENV {1}'.format(app.config['TITLE'], app.config['ENV']))


if __name__ == '__main__':
    main()

