class Grazer < Formula
  include Language::Python::Virtualenv

  desc "Grazer - Multi-Platform Content Discovery for AI agents"
  homepage "https://github.com/Scottcjn/grazer-skill"
  url "https://files.pythonhosted.org/packages/source/g/grazer-skill/grazer_skill-1.2.0.tar.gz"
  sha256 "865b72712d6d35667757cd25e61e7012ce0e0f2d2bc8c14bbdc65d11e8f750db"
  license "MIT"

  depends_on "python@3"

  resource "requests" do
    url "https://files.pythonhosted.org/packages/source/r/requests/requests-2.31.0.tar.gz"
    sha256 "942c5a758f98d790eaed1a29cb6eefc7f0edf3fcb0fce8b0511f7a990d33c1f6"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system "python3", "-c", "import grazer_skill"
  end
end
