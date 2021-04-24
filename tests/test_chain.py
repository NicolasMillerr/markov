from markov.chain import MarkovChain


def test_chain():
    chain = MarkovChain([1, 2, 3, 1, 2])
    assert len(chain.states) == 3

    assert isinstance(chain.transition, dict)
    assert isinstance(chain.transition[1], list)

    assert chain.sample_next(1) == 2

    assert len(chain.build_sequence(10, 1)) == 10
