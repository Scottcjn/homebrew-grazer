class Grazer < Formula
  include Language::Python::Virtualenv

  desc "Grazer - Multi-Platform Content Discovery for AI agents"
  homepage "https://bottube.ai/grazer"
  url "https://files.pythonhosted.org/packages/source/g/grazer-skill/grazer_skill-1.0.0.tar.gz"
  sha256 "2ad5c91cb0f4a95def3e22f104282ac48621977ffd78cc1fc10a04d1401643c8"
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
