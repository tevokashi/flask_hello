"""Modulo para enfileirar e execução de workers
teste
"""
from os import environ
from rq import Queue
import redis

redis_url = environ.get('REDISTOGO_URL')
redis_conn = redis.from_url(redis_url)

queues = {}


def enfileira(param, tipo=0):
    """[summary]

    Arguments:
        param {[string]} -- dois numeros separados por virgula

    Keyword Arguments:
        tipo {int} -- [valor do job] (default: {0})

    Returns:
        [objeto] -- objeto job do rq
    """
    if tipo == 1:
        job = "worker.subtracao"
    else:
        job = "worker.soma"
    if tipo not in queues:
        queues[tipo] = Queue(tipo, connection=redis_conn, default_timeout=3600)
    job2 = queues[tipo].enqueue(job, param, result_ttl=2592000)
    return job2.key


def soma(param):
    """soma dois numeros

    Arguments:
        param {[string]} -- dois numeros separados por virgula

    Returns:
        [int] -- soma de dois numeros
    """
    num1, num2 = param.split(',')
    return num1 + num2


def subtracao(param):
    """subtrai dois numeros

    Arguments:
        param {[string]} -- dois numeros separados por virgula

    Returns:
        [int] -- diferença entra dois numeros
    """
    num1, num2 = param.split(',')
    return num1 - num2
