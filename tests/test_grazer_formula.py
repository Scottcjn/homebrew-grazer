import re
from pathlib import Path


FORMULA = Path(__file__).resolve().parents[1] / "Formula" / "grazer.rb"

# grazer-skill's own runtime requirement is requests>=2.31.0, and requests
# declares certifi / charset-normalizer / idna / urllib3 as install_requires.
# Homebrew's Language::Python::Virtualenv installs resources with
# `pip install --no-deps`, so anything not listed as a resource is simply never
# installed. A missing entry here does not fail the build, it fails at import
# time inside the shipped binary.
REQUESTS_RUNTIME_CLOSURE = {
    "certifi",
    "charset-normalizer",
    "idna",
    "requests",
    "urllib3",
}

RESOURCE_BLOCK = re.compile(
    r'resource\s+"(?P<name>[^"]+)"\s+do\s+'
    r'url\s+"(?P<url>[^"]+)"\s+'
    r'sha256\s+"(?P<sha256>[^"]+)"\s+end',
    re.MULTILINE,
)
SHA256_LITERAL = re.compile(r'sha256\s+"([^"]*)"')


def formula_text():
    return FORMULA.read_text(encoding="utf-8")


def resources():
    return {m.group("name"): m.groupdict() for m in RESOURCE_BLOCK.finditer(formula_text())}


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
    assert 'sha256 "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"' in text


def test_requests_runtime_closure_is_declared_as_resources():
    """--no-deps means every transitive runtime dep needs its own resource."""
    missing = REQUESTS_RUNTIME_CLOSURE - set(resources())

    assert not missing, f"missing resources, the install will import-fail: {sorted(missing)}"


def test_every_sha256_is_a_wellformed_digest():
    """A truncated or hand-written digest either blocks install or verifies nothing."""
    bad = [s for s in SHA256_LITERAL.findall(formula_text()) if not re.fullmatch(r"[0-9a-f]{64}", s)]

    assert not bad, f"not 64 lowercase hex chars: {bad}"


def test_every_resource_url_is_an_sdist_named_after_its_resource():
    for name, res in resources().items():
        filename = res["url"].rsplit("/", 1)[-1]

        assert filename.endswith(".tar.gz"), f"{name}: resource url is not an sdist: {filename}"
        assert filename.split("-")[0] == name.replace("-", "_"), f"{name}: url ships {filename}"


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


def test_homebrew_smoke_test_imports_the_real_top_level_module():
    """The importable package is `grazer`; `grazer_skill` is only the dist name."""
    text = formula_text()

    assert "test do" in text
    assert "import grazer_skill" not in text, "grazer_skill is not an importable module"
    assert 'system libexec/"bin/python", "-c", "import grazer"' in text


def test_homebrew_smoke_test_runs_the_installed_binary_not_system_python():
    """A virtualenv formula installs into libexec, where system python3 cannot see it."""
    text = formula_text()

    assert 'system "python3"' not in text, "system python3 cannot import a libexec virtualenv"
    assert 'shell_output("#{bin}/grazer --help")' in text
