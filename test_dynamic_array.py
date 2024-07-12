import copy
import ctypes

from .dynamic_array import DynArray



class TestDynArray:

    @staticmethod
    def test_insert():
        # TEST: if buffer size not exceeded
        da = DynArray()
        da.insert(0, 100)
        assert da[0] == 100
        assert len(da) == 1
        assert da.capacity == 16
        da.insert(1, 50)
        assert da[0] == 100
        assert da[1] == 50
        assert len(da) == 2
        assert da.capacity == 16
        da.insert(1, 30)
        assert da[0] == 100
        assert da[1] == 30
        assert da[2] == 50
        assert len(da) == 3
        assert da.capacity == 16
        # TEST: if buffer size exceeded
        da = DynArray()
        for i in range(16):
            da.append(i)
        assert da.capacity == 16
        assert len(da) == 16
        da.insert(1, 100)
        assert da[1] == 100
        assert da[2] == 1
        assert len(da) == 17
        assert da.capacity == 16*2
        # TEST: insert out of bound element
        da = DynArray()
        for i in range(30):
            da.append(i)
        try:
            da.insert(31, 100)
        except IndexError:
            pass
        finally:
            assert len(da) == 30
    
    @staticmethod
    def test_delete():
        # TEST: delete with reducing buffer size
        da = DynArray()
        assert da.capacity == 16
        for i in range(16):
            da.append(i)
        da.resize(32)
        assert da.capacity == 32
        da.delete(1)
        assert len(da) == 15
        assert da.capacity == 21
        # TEST: delete with reducing buffer size till min
        da = DynArray()
        da.resize(20)
        assert da.capacity == 20
        for i in range(11):
            da.append(i)
        da.delete(0)
        assert len(da) == 10
        assert da.capacity == 20
        da.delete(1)
        assert len(da) == 9
        assert da.capacity == 16
        # TEST: delete without changing the buffer
        da = DynArray()
        da.resize(32)
        assert da.capacity == 32
        for i in range(30):
            da.append(i)
        da.delete(5)
        assert len(da) == 29
        assert da.capacity == 32
        da.delete(7)
        assert len(da) == 28
        assert da.capacity == 32
        # TEST: delete out of bound element
        da = DynArray()
        for i in range(30):
            da.append(i)
        try:
            da.delete(31)
        except IndexError:
            pass
        finally:
            assert len(da) == 30
        

def run_TestDynArray():
    TestDynArray.test_insert()
    TestDynArray.test_delete()
    return True



