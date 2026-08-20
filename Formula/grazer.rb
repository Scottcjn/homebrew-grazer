class Grazer < Formula
  include Language::Python::Virtualenv

  desc "Grazer - Multi-Platform Content Discovery for AI agents (BoTTube, Moltbook, ClawCities, 4claw, ClawHub)"
  homepage "https://bottube.ai/skills/grazer"
  url "https://files.pythonhosted.org/packages/source/g/grazer-skill/grazer_skill-1.3.0.tar.gz"
  sha256 "7e43e95f42e4b0f03a7f4deb78c8cd57068244a791c41f3fcc84e37c800cde35"
  license "MIT"

  depends_on "python@3"

  # Homebrew installs every resource with pip --no-deps, so the transitive
  # closure of requests has to be declared here or `import requests` fails at
  # runtime inside the virtualenv.
  resource "certifi" do
    url "https://files.pythonhosted.org/packages/source/c/certifi/certifi-2026.7.22.tar.gz"
    sha256 "741e2c3b351ddf169a738da9f2c048608ff7f2c5cc02f1ebc6b118bb090d5d55"
  end

  resource "charset-normalizer" do
    url "https://files.pythonhosted.org/packages/source/c/charset-normalizer/charset_normalizer-3.4.9.tar.gz"
    sha256 "673611bbd43f0810bec0b0f028ddeaaa501190339cac411f347ac76917c3ae7b"
  end

  resource "idna" do
    url "https://files.pythonhosted.org/packages/source/i/idna/idna-3.18.tar.gz"
    sha256 "ffb385a7e039654cef1ab9ef32c6fafe283c0c0467bba1d9029738ce4a14a848"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/source/r/requests/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
  end

  resource "urllib3" do
    url "https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-2.7.0.tar.gz"
    sha256 "231e0ec3b63ceb14667c67be60f2f2c40a518cb38b03af60abc813da26505f4c"
  end

  def install
    virtualenv_install_with_resources
  end

  def caveats
    <<~EOS
      Grazer installed! Discover content across 6 AI agent platforms:

        grazer discover -p bottube --category music
        grazer discover -p moltbook --topic "vintage computing"
        grazer discover -p fourclaw -b tech
        grazer discover -p clawhub --query "web scraping"

      Platforms: BoTTube, Moltbook, ClawCities, Clawsta, 4claw, ClawHub
      Docs: https://bottube.ai/skills/grazer
      Dev.to: https://dev.to/scottcjn
    EOS
  end

  test do
    # The distribution is named grazer-skill, but the importable top-level
    # package is "grazer", and it lives in the formula's virtualenv, not on the
    # system python's path.
    system libexec/"bin/python", "-c", "import grazer"
    assert_match "discover", shell_output("#{bin}/grazer --help")
  end
end
