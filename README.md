
# Project fork moved to [CFEIntact](https://github.com/cfe-lab/CFEIntact)

[![codecov](https://codecov.io/gh/cfe-lab/HIVIntact/branch/master/graph/badge.svg?token=OCYKUD7QET)](https://codecov.io/gh/cfe-lab/HIVIntact)

# HIVIntact
An automated Python proviral intactness checker for HIV-1 consensus sequences.

# Installation instructions

The pipeline is written in Python 3. The below installation instructions assume that Python 3 is already present on the system. If not, it can be installed via a package manager, e.g. for Debian-based systems:

```
sudo apt install python3
```

or for RedHat-based systems:

```
sudo yum install python3
```

or for Macintosh-based systems:

```
sudo port install python3
```

Installation on Windows systems is not recommended.

In addition, for local installations, `pip` and `virtualenv` are also required, and can be installed using the commands listed above.

The pipeline also requires that the MAFFT multiple sequence aligner be installed. Again, one of:

```
sudo apt install mafft
sudo yum install mafft
sudo port install mafft
```

depending on your operating system, should get you there.

Finally, when `--check-nonhiv`, `--check-scramble` and `--check-internal-inversion` options are enabled, the BLAST+ software is expected to be installed.
See [installation instructions](https://blast.ncbi.nlm.nih.gov/doc/blast-help/downloadblastdata.html).

### Local install (recommended)

Install with:

```
git clone --recurse-submodules git@github.com:ramics/intactness-pipeline
cd intactness-pipeline
virtualenv -p python3 env
env/bin/pip install .
```

### Global install

Install with:

```
git clone --recurse-submodules git@github.com/ramics/intactness-pipeline
cd intactness-pipeline
python3 setup.py build
sudo python3 setup.py install
```

Whichever way you choose to install, you'll get a number of warnings if tools needed by the pipeline or one of its dependencies aren't in your path, along with links to download and install those dependencies. 

# Running the pipeline

If you've installed locally, you need to activate the Python environment by running `source env/bin/activate`.

Then run on a set of FASTA sequences with:

```
proviral intact --subtype B sequences.fasta
```

See help (including how to switch various intactness tests on and off) at:

```
proviral intact --help
```

Currently available subtypes can be seen by listing the `util/subtype_alignments` folder.

This will return four files:

* `intact.fasta`: all consensus sequences considered to be intact.
* `nonintact.fasta`: all consensus sequences not considered to be intact.
* `orfs.json`: locations of ORFs in all sequences.
* `errors.json`: a JSON dump of the reasons why some sequences were considered not intact.

# Development instructions

## git flow

We're using `git flow` for this project. The package `git-flow` can be installed on most OSes. To get started, go to the `provirus-pipeline` repo on your machine and type:

```
git flow init
```

Press enter until you hit the command line again. Then, to develop a feature, say the ability to detect long deletions, type:

```
git flow feature start long-deletions
```

You'll now be on a feature branch. If you'd like other people to collborate on your feature branch, you'll need to publish it.  Type:

```
git flow feature publish long-deletions
```

Hack away until you're satisfied, then type:

```
git flow feature finish long-deletions
```

Follow the instructions, and this will merge your feature into develop.  You can then `git push` to develop, and your feature will be included in the next release.

## Releases

A release is a merge to master.  The `master` branch of this github repo is blocked with a review guard, meaning before you merge `develop` into `master`, you need to open a **pull request** on github from `develop` into `master` and get it reviewed by another contributor.  This is to keep code quality high.

Please bump at least the minor version in `setup.py` with every release.

## Other tips

To reinstall locally without reinstalling dependencies or bumping the version, run:

```
env/bin/pip install --force-reinstall --no-deps --upgrade .
```


