# Changelog

## [5.1.0](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v5.0.0...tremendous-python-v5.1.0) (2025-06-24)


### Bug Fixes

* unlock `urllib3` dependency to support recent releases ([#53](https://github.com/tremendous-rewards/tremendous-python/issues/53)) ([35c2826](https://github.com/tremendous-rewards/tremendous-python/commit/35c2826006d948cc8105527002ae945bd2ea054d))


### Miscellaneous Chores

* release 5.1.0 ([65f0167](https://github.com/tremendous-rewards/tremendous-python/commit/65f0167caf14bcb8e1e7b1fd65b0c5b95263b170))

## [5.0.0](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v4.3.0...tremendous-python-v5.0.0) (2025-06-09)


### ⚠ BREAKING CHANGES

* Remove Python 3.7 support ([#50](https://github.com/tremendous-rewards/tremendous-python/issues/50))

### Features

* add more fields to the Funding Source resource ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))
* add support for the Cancel Reward endpoint ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))
* add support for the Connected Organization and Connected ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))
* regen SDK code ([#52](https://github.com/tremendous-rewards/tremendous-python/issues/52)) ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))
* update fields regarding disclosures on the Products resource ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))


### Bug Fixes

* expect `200` instead of `201` when creating a Report or a Campaign ([d6b5213](https://github.com/tremendous-rewards/tremendous-python/commit/d6b5213fe089214deb7d75c570392ae68c34278e))
* Remove Python 3.7 support ([#50](https://github.com/tremendous-rewards/tremendous-python/issues/50)) ([17d8d5c](https://github.com/tremendous-rewards/tremendous-python/commit/17d8d5ca06983edab63c5736814ff1c46dc15be0))

## [4.3.0](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v4.2.0...tremendous-python-v4.3.0) (2024-12-03)


### Features

* add `DeliveryMetadata` to `POST /orders` ([#42](https://github.com/tremendous-rewards/tremendous-python/issues/42)) ([d625a11](https://github.com/tremendous-rewards/tremendous-python/commit/d625a113e08d600e4d1c3d6d1a6af67f68708dbc))


### Bug Fixes

* add missing `FraudReviewReason` value ([d625a11](https://github.com/tremendous-rewards/tremendous-python/commit/d625a113e08d600e4d1c3d6d1a6af67f68708dbc))
* fix typos ([d625a11](https://github.com/tremendous-rewards/tremendous-python/commit/d625a113e08d600e4d1c3d6d1a6af67f68708dbc))

## [4.2.0](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v4.1.0...tremendous-python-v4.2.0) (2024-11-08)


### Features

* add `discount` to `Order` payment details ([4158c9e](https://github.com/tremendous-rewards/tremendous-python/commit/4158c9e5bbf86e0443bd02ca6f3971af76cedde9))
* add `risk` property to fraud reviews ([4158c9e](https://github.com/tremendous-rewards/tremendous-python/commit/4158c9e5bbf86e0443bd02ca6f3971af76cedde9))
* include order property when possible on balance transactions endpoint ([#35](https://github.com/tremendous-rewards/tremendous-python/issues/35)) ([4158c9e](https://github.com/tremendous-rewards/tremendous-python/commit/4158c9e5bbf86e0443bd02ca6f3971af76cedde9))


### Bug Fixes

* fix `POST /orders` "created" response schema ([#38](https://github.com/tremendous-rewards/tremendous-python/issues/38)) ([df2f204](https://github.com/tremendous-rewards/tremendous-python/commit/df2f204330a47d9968cd8a731eadf99e8c263130))

## [4.1.0](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v4.0.1...tremendous-python-v4.1.0) (2024-11-04)


### Features

* add /reports endpoints ([#32](https://github.com/tremendous-rewards/tremendous-python/commit/a8419dddbbaa872fab7a556a47aec0672b4fdb3b))
* add support for updated_phone and updated_email on POST /api/v2/reward/:id/resend ([#32](https://github.com/tremendous-rewards/tremendous-python/commit/a8419dddbbaa872fab7a556a47aec0672b4fdb3b))

## [4.0.1](https://github.com/tremendous-rewards/tremendous-python/compare/tremendous-python-v4.0.0...tremendous-python-v4.0.1) (2024-09-26)


### Bug Fixes

* fix `User-Agent` interpolation ([b8f5637](https://github.com/tremendous-rewards/tremendous-python/commit/b8f56375c51d48ea5636535e585937f244df1bbb))
* regenerate internal classes after spec cleanup ([da9d188](https://github.com/tremendous-rewards/tremendous-python/commit/da9d188f12df022cf245babfd323b00ff4591cbc))
