## Step 1 - Re-generate the SDK source code

The source code from this repo is generated using [OpenAPI generator][1] and the Open API specification for the Tremendous API. The `.py` files can be re-generated and compiled with the following commands:

```console
bin/generate
```

After that, please review the changes to double check that the changes to the API spec were
generated correctly. Please open a Pull Request with the file changes and wait for the test pipeline
before merging it to main.

## Step 2 - Update the version

The Pull Request with the changes to the generated files should update the version on `tremendous/version.py` and `pyproject.toml`
following [Semantic Versioning][2] practices - most changes here should be backwards compatible and
deserve a MINOR version update

## Step 3 - Publish a new release on GitHub

The [publish.yml](.github/workflows/publish.yml) workflow is responsible for publishing the package to
Pip when a new release is published on GitHub.

[1]: https://openapi-generator.tech
[2]: https://semver.org
