from plone.distribution.handler import (
    default_handler,
    default_pre_handler,
    post_handler as post_handler_orig,
)


def pre_handler(answers: dict) -> dict:
    return default_pre_handler(answers)


def handler(distribution, site, answers: dict):
    return default_handler(distribution, site, answers)


def post_handler(distribution, site, answers: dict):
    return post_handler_orig(distribution, site, answers)
