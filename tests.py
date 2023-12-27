import pytest
import asyncio


async def get_answer():
    return 52


async def raise_error():
    raise ValueError("Some error message")


@pytest.mark.asyncio
async def test_get_answer():
    expected_value = 52
    result = await get_answer()
    assert result == expected_value


@pytest.mark.asyncio
async def test_raise_error():
    expected_exception = ValueError("Some error message")
    
    with pytest.raises(ValueError) as exc_info:
        await raise_error()

    assert str(exc_info.value) == str(expected_exception)
