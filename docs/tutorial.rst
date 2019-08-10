.. -*- mode: rst; encoding: utf-8 -*-

Tutorial
========

This tutorial will give you a basic understanding of how to use PyZenHub

First create a ZenHub instance
------------------------------

.. code-block:: python

    from zenhub import ZenHub

    # using an access token with Public ZenHub
    zen = ZenHub("access_token")

    # using an access token with Enterprise ZenHub
    zen = ZenHub("access_token", api_endpoint="https://{hostname}")


Getting pipelines from your board
---------------------------------

.. code-block:: python

    repo = zen.repository(1234567)
    board = repo.board()

    for pipeline in board.pipelines():
        print(f'\nPipeline: {pipeline.name}')
        for issue in pipeline.issues:
            print(issue)
