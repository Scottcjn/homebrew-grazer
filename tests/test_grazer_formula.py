from pathlib import Path


FORMULA = Path(__file__).resolve().parents[1] / "Formula" / "grazer.rb"


def formula_text():
    return FORMULA.read_text(encoding="utf-8")


def test_formula_metadata_points_to_current_grazer_release():
    text = formula_text()

    assert 'desc "Grazer - Multi-Platform Content Discovery for AI agents' in text
    assert 'homepage "https://bottube.ai/skills/grazer"' in text
    assert 'url "https://files.pythonhosted.org/packages/source/g/grazer-skill/grazer_skill-1.3.0.tar.gz"' in text
    assert 'sha256 "7e43e95f42e4b0f03a7f4deb78c8cd57068244a791c41f3fcc84e37c800cde35"' in text
    assert 'license "MIT"' in text


def test_formula_declares_python_runtime_and_requests_resource():
    text = formula_text()

    assert 'depends_on "python@3"' in text
    assert 'resource "requests" do' in text
    assert 'url "https://files.pythonhosted.org/packages/source/r/requests/requests-2.31.0.tar.gz"' in text
    assert 'sha256 "942c5a758f98d790eaed1a29cb6eefc7f0edf3fcb0fce8b0511f7a990d33c1f6"' in text


def test_install_uses_virtualenv_resources():
    text = formula_text()

    assert "include Language::Python::Virtualenv" in text
    assert "def install" in text
    assert "virtualenv_install_with_resources" in text


def test_caveats_document_expected_platform_examples():
    text = formula_text()

    assert "Grazer installed!" in text
    assert "grazer discover -p bottube --category music" in text
    assert 'grazer discover -p moltbook --topic "vintage computing"' in text
    assert 'grazer discover -p clawhub --query "web scraping"' in text
    assert "Platforms: BoTTube, Moltbook, ClawCities, Clawsta, 4claw, ClawHub" in text


def test_homebrew_smoke_test_imports_installed_package():
    text = formula_text()

    assert "test do" in text
    assert 'system "python3", "-c", "import grazer_skill"' in text
