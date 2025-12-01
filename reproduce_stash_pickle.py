import pickle
from _pytest.stash import Stash, StashKey

def test_stash_pickle():
    key = StashKey[str]()
    stash = Stash()
    stash[key] = "value"

    dumped = pickle.dumps(stash)
    loaded = pickle.loads(dumped)

    # We can't easily check key identity across processes/pickle if key is not module global.
    # But here we are in same process.
    # StashKey instances are unique. Pickle preserves identity if they are pickled by reference (module level).
    # If they are created inside function, they might be pickled by value if supported?
    # StashKey has __slots__=().

    print("Pickle successful")

if __name__ == "__main__":
    test_stash_pickle()
