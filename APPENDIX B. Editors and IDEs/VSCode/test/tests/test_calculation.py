import pytest
from src.calculations import calculate_mw

def test_calculate_mw_water():
    """Tests the molecular weight calculation for water."""
    # The expected value for water (H2O) is approx. 18.015
    assert calculate_mw("O") == pytest.approx(18.015, abs=1e-3)

def test_calculate_mw_invalid_smiles():
    """Tests that invalid SMILES returns 0.0."""
    assert calculate_mw("invalid_smiles_string") == 0.0