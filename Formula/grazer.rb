class Grazer < Formula
  include Language::Python::Virtualenv

  desc "Grazer - Multi-Platform Content Discovery for AI agents (BoTTube, Moltbook, ClawCities, 4claw, ClawHub)"
  homepage "https://bottube.ai/skills/grazer"
  url "https://files.pythonhosted.org/packages/source/g/grazer-skill/grazer_skill-1.3.0.tar.gz"
  sha256 "7e43e95f42e4b0f03a7f4deb78c8cd57068244a791c41f3fcc84e37c800cde35"
  license "MIT"

  depends_on "python@3"

  resource "requests" do
    url "https://files.pythonhosted.org/packages/source/r/requests/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7f0edf3fcb0fce8b0511f7a990d33c1f6"
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
    system "python3", "-c", "import grazer_skill"
  end
end
