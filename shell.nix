{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python39
    python39Packages.pip
    python39Packages.setuptools
  ];
}
