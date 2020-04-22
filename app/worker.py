"""Modulo para enfileirar e execução de workers
"""
from rq import Queue
from redis import Redis

redis_conn = Redis('10.31.120.87', '30379', db=2)

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
    return job2

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
