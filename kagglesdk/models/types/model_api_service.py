from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.datasets.types.dataset_api_service import ApiCategory, ApiDatasetNewFile, ApiUploadDirectoryInfo
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ListModelsOrderBy, ModelFramework, ModelInstanceType
from kagglesdk.models.types.model_types import BaseModelInstanceInformation, ModelLink
from typing import Optional, List

class ApiCreateModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    body (ApiCreateModelInstanceRequestBody)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._body = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def body(self) -> Optional['ApiCreateModelInstanceRequestBody']:
    return self._body

  @body.setter
  def body(self, body: Optional['ApiCreateModelInstanceRequestBody']):
    if body is None:
      del self.body
      return
    if not isinstance(body, ApiCreateModelInstanceRequestBody):
      raise TypeError('body must be of type ApiCreateModelInstanceRequestBody')
    self._body = body


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/create/instance'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return 'body'

class ApiCreateModelInstanceRequestBody(KaggleObject):
  r"""
  Attributes:
    instance_slug (str)
    framework (ModelFramework)
    overview (str)
    usage (str)
    fine_tunable (bool)
    training_data (str)
    files (ApiDatasetNewFile)
    directories (ApiUploadDirectoryInfo)
    license_name (str)
    model_instance_type (ModelInstanceType)
    base_model_instance (str)
    external_base_model_url (str)
  """

  def __init__(self):
    self._instance_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._overview = ""
    self._usage = ""
    self._fine_tunable = None
    self._training_data = []
    self._files = []
    self._directories = []
    self._license_name = None
    self._model_instance_type = None
    self._base_model_instance = None
    self._external_base_model_url = None
    self._freeze()

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def overview(self) -> str:
    return self._overview

  @overview.setter
  def overview(self, overview: str):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def usage(self) -> str:
    return self._usage

  @usage.setter
  def usage(self, usage: str):
    if usage is None:
      del self.usage
      return
    if not isinstance(usage, str):
      raise TypeError('usage must be of type str')
    self._usage = usage

  @property
  def fine_tunable(self) -> bool:
    return self._fine_tunable or False

  @fine_tunable.setter
  def fine_tunable(self, fine_tunable: bool):
    if fine_tunable is None:
      del self.fine_tunable
      return
    if not isinstance(fine_tunable, bool):
      raise TypeError('fine_tunable must be of type bool')
    self._fine_tunable = fine_tunable

  @property
  def training_data(self) -> Optional[List[str]]:
    return self._training_data

  @training_data.setter
  def training_data(self, training_data: Optional[List[str]]):
    if training_data is None:
      del self.training_data
      return
    if not isinstance(training_data, list):
      raise TypeError('training_data must be of type list')
    if not all([isinstance(t, str) for t in training_data]):
      raise TypeError('training_data must contain only items of type str')
    self._training_data = training_data

  @property
  def files(self) -> Optional[List[Optional['ApiDatasetNewFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetNewFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetNewFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetNewFile')
    self._files = files

  @property
  def directories(self) -> Optional[List[Optional['ApiUploadDirectoryInfo']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['ApiUploadDirectoryInfo']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, ApiUploadDirectoryInfo) for t in directories]):
      raise TypeError('directories must contain only items of type ApiUploadDirectoryInfo')
    self._directories = directories

  @property
  def license_name(self) -> str:
    return self._license_name or ""

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

  @property
  def model_instance_type(self) -> 'ModelInstanceType':
    return self._model_instance_type or ModelInstanceType.MODEL_INSTANCE_TYPE_UNSPECIFIED

  @model_instance_type.setter
  def model_instance_type(self, model_instance_type: 'ModelInstanceType'):
    if model_instance_type is None:
      del self.model_instance_type
      return
    if not isinstance(model_instance_type, ModelInstanceType):
      raise TypeError('model_instance_type must be of type ModelInstanceType')
    self._model_instance_type = model_instance_type

  @property
  def base_model_instance(self) -> str:
    return self._base_model_instance or ""

  @base_model_instance.setter
  def base_model_instance(self, base_model_instance: str):
    if base_model_instance is None:
      del self.base_model_instance
      return
    if not isinstance(base_model_instance, str):
      raise TypeError('base_model_instance must be of type str')
    self._base_model_instance = base_model_instance

  @property
  def external_base_model_url(self) -> str:
    return self._external_base_model_url or ""

  @external_base_model_url.setter
  def external_base_model_url(self, external_base_model_url: str):
    if external_base_model_url is None:
      del self.external_base_model_url
      return
    if not isinstance(external_base_model_url, str):
      raise TypeError('external_base_model_url must be of type str')
    self._external_base_model_url = external_base_model_url


class ApiCreateModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    body (ApiCreateModelInstanceVersionRequestBody)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._body = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def body(self) -> Optional['ApiCreateModelInstanceVersionRequestBody']:
    return self._body

  @body.setter
  def body(self, body: Optional['ApiCreateModelInstanceVersionRequestBody']):
    if body is None:
      del self.body
      return
    if not isinstance(body, ApiCreateModelInstanceVersionRequestBody):
      raise TypeError('body must be of type ApiCreateModelInstanceVersionRequestBody')
    self._body = body


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/create/version'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return 'body'

class ApiCreateModelInstanceVersionRequestBody(KaggleObject):
  r"""
  Attributes:
    version_notes (str)
    files (ApiDatasetNewFile)
    directories (ApiUploadDirectoryInfo)
  """

  def __init__(self):
    self._version_notes = None
    self._files = []
    self._directories = []
    self._freeze()

  @property
  def version_notes(self) -> str:
    return self._version_notes or ""

  @version_notes.setter
  def version_notes(self, version_notes: str):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def files(self) -> Optional[List[Optional['ApiDatasetNewFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiDatasetNewFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiDatasetNewFile) for t in files]):
      raise TypeError('files must contain only items of type ApiDatasetNewFile')
    self._files = files

  @property
  def directories(self) -> Optional[List[Optional['ApiUploadDirectoryInfo']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['ApiUploadDirectoryInfo']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, ApiUploadDirectoryInfo) for t in directories]):
      raise TypeError('directories must contain only items of type ApiUploadDirectoryInfo')
    self._directories = directories


class ApiCreateModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    slug (str)
    title (str)
    subtitle (str)
    is_private (bool)
    description (str)
    publish_time (datetime)
    provenance_sources (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._slug = ""
    self._title = ""
    self._subtitle = None
    self._is_private = None
    self._description = None
    self._publish_time = None
    self._provenance_sources = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def is_private(self) -> bool:
    return self._is_private or False

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def publish_time(self) -> datetime:
    return self._publish_time

  @publish_time.setter
  def publish_time(self, publish_time: datetime):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def provenance_sources(self) -> str:
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: str):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources


  def endpoint(self):
    path = '/api/v1/models/create/new'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'

class ApiCreateModelResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
    error (str)
    error_code (int)
    url (str)
  """

  def __init__(self):
    self._id = None
    self._ref = None
    self._error = None
    self._error_code = None
    self._url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def ref(self) -> str:
    return self._ref or ""

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def error_code(self) -> int:
    return self._error_code or 0

  @error_code.setter
  def error_code(self, error_code: int):
    if error_code is None:
      del self.error_code
      return
    if not isinstance(error_code, int):
      raise TypeError('error_code must be of type int')
    self._error_code = error_code

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class ApiDeleteModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/delete'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

class ApiDeleteModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._version_number = 0
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/{version_number}/delete'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

class ApiDeleteModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/delete'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

class ApiDeleteModelResponse(KaggleObject):
  r"""
  Attributes:
    error (str)
  """

  def __init__(self):
    self._error = None
    self._freeze()

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error


class ApiDownloadModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    version_number (int)
    path (str)
      Relative path to a specific file inside the databundle.
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._version_number = 0
    self._path = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def path(self) -> str:
    """Relative path to a specific file inside the databundle."""
    return self._path or ""

  @path.setter
  def path(self, path: str):
    if path is None:
      del self.path
      return
    if not isinstance(path, str):
      raise TypeError('path must be of type str')
    self._path = path


  def endpoint(self):
    if self.path:
      path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/{version_number}/download/{path}'
    else:
      path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/{version_number}/download'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/{version_number}/download'

class ApiGetModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/get'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/get'

class ApiGetModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/get'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/models/{owner_slug}/{model_slug}/get'

class ApiListModelInstanceVersionFilesRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    instance_slug (str)
    framework (ModelFramework)
    version_number (int)
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._instance_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._version_number = None
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def page_size(self) -> int:
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


  def endpoint(self):
    if self.version_number:
      path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/{version_number}/files'
    else:
      path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/files'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/files'

class ApiListModelInstanceVersionFilesResponse(KaggleObject):
  r"""
  Attributes:
    files (ApiModelFile)
    next_page_token (str)
  """

  def __init__(self):
    self._files = []
    self._next_page_token = ""
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['ApiModelFile']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ApiModelFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ApiModelFile) for t in files]):
      raise TypeError('files must contain only items of type ApiModelFile')
    self._files = files

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ApiListModelsRequest(KaggleObject):
  r"""
  Attributes:
    search (str)
      Display models matching the specified search terms.
    sort_by (ListModelsOrderBy)
      Sort the results (default is 'hotness'). 'relevance' only works if there is
      a search query.
    owner (str)
      Display models by a particular user or organization.
    page_size (int)
      Page size.
    page_token (str)
      Page token used for pagination.
    only_vertex_models (bool)
      Only list models that have Vertex URLs
  """

  def __init__(self):
    self._search = None
    self._sort_by = None
    self._owner = None
    self._page_size = None
    self._page_token = None
    self._only_vertex_models = None
    self._freeze()

  @property
  def search(self) -> str:
    """Display models matching the specified search terms."""
    return self._search or ""

  @search.setter
  def search(self, search: str):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

  @property
  def sort_by(self) -> 'ListModelsOrderBy':
    r"""
    Sort the results (default is 'hotness'). 'relevance' only works if there is
    a search query.
    """
    return self._sort_by or ListModelsOrderBy.LIST_MODELS_ORDER_BY_UNSPECIFIED

  @sort_by.setter
  def sort_by(self, sort_by: 'ListModelsOrderBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, ListModelsOrderBy):
      raise TypeError('sort_by must be of type ListModelsOrderBy')
    self._sort_by = sort_by

  @property
  def owner(self) -> str:
    """Display models by a particular user or organization."""
    return self._owner or ""

  @owner.setter
  def owner(self, owner: str):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def page_size(self) -> int:
    """Page size."""
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    """Page token used for pagination."""
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def only_vertex_models(self) -> bool:
    """Only list models that have Vertex URLs"""
    return self._only_vertex_models or False

  @only_vertex_models.setter
  def only_vertex_models(self, only_vertex_models: bool):
    if only_vertex_models is None:
      del self.only_vertex_models
      return
    if not isinstance(only_vertex_models, bool):
      raise TypeError('only_vertex_models must be of type bool')
    self._only_vertex_models = only_vertex_models


  def endpoint(self):
    path = '/api/v1/models/list'
    return path.format_map(self.to_field_map(self))

class ApiListModelsResponse(KaggleObject):
  r"""
  Attributes:
    models (ApiModel)
    next_page_token (str)
    total_results (int)
  """

  def __init__(self):
    self._models = []
    self._next_page_token = ""
    self._total_results = 0
    self._freeze()

  @property
  def models(self) -> Optional[List[Optional['ApiModel']]]:
    return self._models

  @models.setter
  def models(self, models: Optional[List[Optional['ApiModel']]]):
    if models is None:
      del self.models
      return
    if not isinstance(models, list):
      raise TypeError('models must be of type list')
    if not all([isinstance(t, ApiModel) for t in models]):
      raise TypeError('models must contain only items of type ApiModel')
    self._models = models

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def total_results(self) -> int:
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results


class ApiModel(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
      ref is `owner_slug/model_slug`
    title (str)
    subtitle (str)
    author (str)
    slug (str)
    is_private (bool)
    description (str)
    instances (ApiModelInstance)
    tags (ApiCategory)
    publish_time (datetime)
    provenance_sources (str)
    url (str)
    model_version_links (ModelLink)
  """

  def __init__(self):
    self._id = 0
    self._ref = ""
    self._title = ""
    self._subtitle = ""
    self._author = ""
    self._slug = ""
    self._is_private = False
    self._description = ""
    self._instances = []
    self._tags = []
    self._publish_time = None
    self._provenance_sources = ""
    self._url = ""
    self._model_version_links = []
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def ref(self) -> str:
    """ref is `owner_slug/model_slug`"""
    return self._ref

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def subtitle(self) -> str:
    return self._subtitle

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def author(self) -> str:
    return self._author

  @author.setter
  def author(self, author: str):
    if author is None:
      del self.author
      return
    if not isinstance(author, str):
      raise TypeError('author must be of type str')
    self._author = author

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def instances(self) -> Optional[List[Optional['ApiModelInstance']]]:
    return self._instances

  @instances.setter
  def instances(self, instances: Optional[List[Optional['ApiModelInstance']]]):
    if instances is None:
      del self.instances
      return
    if not isinstance(instances, list):
      raise TypeError('instances must be of type list')
    if not all([isinstance(t, ApiModelInstance) for t in instances]):
      raise TypeError('instances must contain only items of type ApiModelInstance')
    self._instances = instances

  @property
  def tags(self) -> Optional[List[Optional['ApiCategory']]]:
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['ApiCategory']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, ApiCategory) for t in tags]):
      raise TypeError('tags must contain only items of type ApiCategory')
    self._tags = tags

  @property
  def publish_time(self) -> datetime:
    return self._publish_time

  @publish_time.setter
  def publish_time(self, publish_time: datetime):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def provenance_sources(self) -> str:
    return self._provenance_sources

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: str):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def model_version_links(self) -> Optional[List[Optional['ModelLink']]]:
    return self._model_version_links

  @model_version_links.setter
  def model_version_links(self, model_version_links: Optional[List[Optional['ModelLink']]]):
    if model_version_links is None:
      del self.model_version_links
      return
    if not isinstance(model_version_links, list):
      raise TypeError('model_version_links must be of type list')
    if not all([isinstance(t, ModelLink) for t in model_version_links]):
      raise TypeError('model_version_links must contain only items of type ModelLink')
    self._model_version_links = model_version_links


class ApiModelFile(KaggleObject):
  r"""
  Attributes:
    name (str)
    size (int)
    creation_date (datetime)
  """

  def __init__(self):
    self._name = ""
    self._size = 0
    self._creation_date = None
    self._freeze()

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def size(self) -> int:
    return self._size

  @size.setter
  def size(self, size: int):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size

  @property
  def creation_date(self) -> datetime:
    return self._creation_date or None

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date


class ApiModelInstance(KaggleObject):
  r"""
  Attributes:
    id (int)
    slug (str)
    framework (ModelFramework)
    fine_tunable (bool)
    overview (str)
    usage (str)
    download_url (str)
    version_id (int)
    version_number (int)
    training_data (str)
    url (str)
    license_name (str)
    model_instance_type (ModelInstanceType)
    base_model_instance_information (BaseModelInstanceInformation)
    external_base_model_url (str)
  """

  def __init__(self):
    self._id = 0
    self._slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._fine_tunable = False
    self._overview = ""
    self._usage = ""
    self._download_url = ""
    self._version_id = 0
    self._version_number = 0
    self._training_data = []
    self._url = ""
    self._license_name = ""
    self._model_instance_type = ModelInstanceType.MODEL_INSTANCE_TYPE_UNSPECIFIED
    self._base_model_instance_information = None
    self._external_base_model_url = ""
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def fine_tunable(self) -> bool:
    return self._fine_tunable

  @fine_tunable.setter
  def fine_tunable(self, fine_tunable: bool):
    if fine_tunable is None:
      del self.fine_tunable
      return
    if not isinstance(fine_tunable, bool):
      raise TypeError('fine_tunable must be of type bool')
    self._fine_tunable = fine_tunable

  @property
  def overview(self) -> str:
    return self._overview

  @overview.setter
  def overview(self, overview: str):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def usage(self) -> str:
    return self._usage

  @usage.setter
  def usage(self, usage: str):
    if usage is None:
      del self.usage
      return
    if not isinstance(usage, str):
      raise TypeError('usage must be of type str')
    self._usage = usage

  @property
  def download_url(self) -> str:
    return self._download_url

  @download_url.setter
  def download_url(self, download_url: str):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url

  @property
  def version_id(self) -> int:
    return self._version_id

  @version_id.setter
  def version_id(self, version_id: int):
    if version_id is None:
      del self.version_id
      return
    if not isinstance(version_id, int):
      raise TypeError('version_id must be of type int')
    self._version_id = version_id

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def training_data(self) -> Optional[List[str]]:
    return self._training_data

  @training_data.setter
  def training_data(self, training_data: Optional[List[str]]):
    if training_data is None:
      del self.training_data
      return
    if not isinstance(training_data, list):
      raise TypeError('training_data must be of type list')
    if not all([isinstance(t, str) for t in training_data]):
      raise TypeError('training_data must contain only items of type str')
    self._training_data = training_data

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def license_name(self) -> str:
    return self._license_name

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

  @property
  def model_instance_type(self) -> 'ModelInstanceType':
    return self._model_instance_type

  @model_instance_type.setter
  def model_instance_type(self, model_instance_type: 'ModelInstanceType'):
    if model_instance_type is None:
      del self.model_instance_type
      return
    if not isinstance(model_instance_type, ModelInstanceType):
      raise TypeError('model_instance_type must be of type ModelInstanceType')
    self._model_instance_type = model_instance_type

  @property
  def base_model_instance_information(self) -> Optional['BaseModelInstanceInformation']:
    return self._base_model_instance_information or None

  @base_model_instance_information.setter
  def base_model_instance_information(self, base_model_instance_information: Optional['BaseModelInstanceInformation']):
    if base_model_instance_information is None:
      del self.base_model_instance_information
      return
    if not isinstance(base_model_instance_information, BaseModelInstanceInformation):
      raise TypeError('base_model_instance_information must be of type BaseModelInstanceInformation')
    self._base_model_instance_information = base_model_instance_information

  @property
  def external_base_model_url(self) -> str:
    return self._external_base_model_url

  @external_base_model_url.setter
  def external_base_model_url(self, external_base_model_url: str):
    if external_base_model_url is None:
      del self.external_base_model_url
      return
    if not isinstance(external_base_model_url, str):
      raise TypeError('external_base_model_url must be of type str')
    self._external_base_model_url = external_base_model_url


class ApiUpdateModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    overview (str)
    usage (str)
    fine_tunable (bool)
    training_data (str)
    update_mask (FieldMask)
    license_name (str)
    model_instance_type (ModelInstanceType)
    base_model_instance (str)
    external_base_model_url (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._overview = ""
    self._usage = ""
    self._fine_tunable = None
    self._training_data = []
    self._update_mask = None
    self._license_name = None
    self._model_instance_type = None
    self._base_model_instance = None
    self._external_base_model_url = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def overview(self) -> str:
    return self._overview

  @overview.setter
  def overview(self, overview: str):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def usage(self) -> str:
    return self._usage

  @usage.setter
  def usage(self, usage: str):
    if usage is None:
      del self.usage
      return
    if not isinstance(usage, str):
      raise TypeError('usage must be of type str')
    self._usage = usage

  @property
  def fine_tunable(self) -> bool:
    return self._fine_tunable or False

  @fine_tunable.setter
  def fine_tunable(self, fine_tunable: bool):
    if fine_tunable is None:
      del self.fine_tunable
      return
    if not isinstance(fine_tunable, bool):
      raise TypeError('fine_tunable must be of type bool')
    self._fine_tunable = fine_tunable

  @property
  def training_data(self) -> Optional[List[str]]:
    return self._training_data

  @training_data.setter
  def training_data(self, training_data: Optional[List[str]]):
    if training_data is None:
      del self.training_data
      return
    if not isinstance(training_data, list):
      raise TypeError('training_data must be of type list')
    if not all([isinstance(t, str) for t in training_data]):
      raise TypeError('training_data must contain only items of type str')
    self._training_data = training_data

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask

  @property
  def license_name(self) -> str:
    return self._license_name or ""

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

  @property
  def model_instance_type(self) -> 'ModelInstanceType':
    return self._model_instance_type or ModelInstanceType.MODEL_INSTANCE_TYPE_UNSPECIFIED

  @model_instance_type.setter
  def model_instance_type(self, model_instance_type: 'ModelInstanceType'):
    if model_instance_type is None:
      del self.model_instance_type
      return
    if not isinstance(model_instance_type, ModelInstanceType):
      raise TypeError('model_instance_type must be of type ModelInstanceType')
    self._model_instance_type = model_instance_type

  @property
  def base_model_instance(self) -> str:
    return self._base_model_instance or ""

  @base_model_instance.setter
  def base_model_instance(self, base_model_instance: str):
    if base_model_instance is None:
      del self.base_model_instance
      return
    if not isinstance(base_model_instance, str):
      raise TypeError('base_model_instance must be of type str')
    self._base_model_instance = base_model_instance

  @property
  def external_base_model_url(self) -> str:
    return self._external_base_model_url or ""

  @external_base_model_url.setter
  def external_base_model_url(self, external_base_model_url: str):
    if external_base_model_url is None:
      del self.external_base_model_url
      return
    if not isinstance(external_base_model_url, str):
      raise TypeError('external_base_model_url must be of type str')
    self._external_base_model_url = external_base_model_url


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/{framework}/{instance_slug}/update'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'

class ApiUpdateModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    title (str)
    subtitle (str)
    is_private (bool)
    description (str)
    publish_time (datetime)
    provenance_sources (str)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._title = ""
    self._subtitle = None
    self._is_private = False
    self._description = None
    self._publish_time = None
    self._provenance_sources = None
    self._update_mask = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def publish_time(self) -> datetime:
    return self._publish_time

  @publish_time.setter
  def publish_time(self, publish_time: datetime):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def provenance_sources(self) -> str:
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: str):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


  def endpoint(self):
    path = '/api/v1/models/{owner_slug}/{model_slug}/update'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'

class ApiUpdateModelResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
    ref (str)
    error (str)
    url (str)
  """

  def __init__(self):
    self._id = None
    self._ref = None
    self._error = None
    self._url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def ref(self) -> str:
    return self._ref or ""

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class ApiUploadModelFileRequest(KaggleObject):
  r"""
  Attributes:
    file_name (str)
    content_length (int)
    last_modified_epoch_seconds (int)
  """

  def __init__(self):
    self._file_name = ""
    self._content_length = 0
    self._last_modified_epoch_seconds = 0
    self._freeze()

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def last_modified_epoch_seconds(self) -> int:
    return self._last_modified_epoch_seconds

  @last_modified_epoch_seconds.setter
  def last_modified_epoch_seconds(self, last_modified_epoch_seconds: int):
    if last_modified_epoch_seconds is None:
      del self.last_modified_epoch_seconds
      return
    if not isinstance(last_modified_epoch_seconds, int):
      raise TypeError('last_modified_epoch_seconds must be of type int')
    self._last_modified_epoch_seconds = last_modified_epoch_seconds


  def endpoint(self):
    path = '/api/v1/models/upload/file/{content_length}/{last_modified_epoch_seconds}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

class ApiUploadModelFileResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque string token used to reference the new BlobFile.
    create_url (str)
      URL to use to start the upload
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque string token used to reference the new BlobFile."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def create_url(self) -> str:
    """URL to use to start the upload"""
    return self._create_url

  @create_url.setter
  def create_url(self, create_url: str):
    if create_url is None:
      del self.create_url
      return
    if not isinstance(create_url, str):
      raise TypeError('create_url must be of type str')
    self._create_url = create_url


ApiCreateModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", ApiCreateModelInstanceRequestBody, None, KaggleObjectSerializer()),
]

ApiCreateModelInstanceRequestBody._fields = [
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("usage", "usage", "_usage", str, "", PredefinedSerializer()),
  FieldMetadata("fineTunable", "fine_tunable", "_fine_tunable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("trainingData", "training_data", "_training_data", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("files", "files", "_files", ApiDatasetNewFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("directories", "directories", "_directories", ApiUploadDirectoryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("licenseName", "license_name", "_license_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceType", "model_instance_type", "_model_instance_type", ModelInstanceType, None, EnumSerializer(), optional=True),
  FieldMetadata("baseModelInstance", "base_model_instance", "_base_model_instance", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalBaseModelUrl", "external_base_model_url", "_external_base_model_url", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateModelInstanceVersionRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", ApiCreateModelInstanceVersionRequestBody, None, KaggleObjectSerializer()),
]

ApiCreateModelInstanceVersionRequestBody._fields = [
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("files", "files", "_files", ApiDatasetNewFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("directories", "directories", "_directories", ApiUploadDirectoryInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ApiCreateModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateModelResponse._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ref", "ref", "_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("errorCode", "error_code", "_error_code", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

ApiDeleteModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
]

ApiDeleteModelInstanceVersionRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
]

ApiDeleteModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
]

ApiDeleteModelResponse._fields = [
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

ApiDownloadModelInstanceVersionRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("path", "path", "_path", str, None, PredefinedSerializer(), optional=True),
]

ApiGetModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
]

ApiGetModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
]

ApiListModelInstanceVersionFilesRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListModelInstanceVersionFilesResponse._fields = [
  FieldMetadata("files", "files", "_files", ApiModelFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListModelsRequest._fields = [
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", ListModelsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("owner", "owner", "_owner", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("onlyVertexModels", "only_vertex_models", "_only_vertex_models", bool, None, PredefinedSerializer(), optional=True),
]

ApiListModelsResponse._fields = [
  FieldMetadata("models", "models", "_models", ApiModel, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
]

ApiModel._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("author", "author", "_author", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("instances", "instances", "_instances", ApiModelInstance, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tags", "tags", "_tags", ApiCategory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("modelVersionLinks", "model_version_links", "_model_version_links", ModelLink, [], ListSerializer(KaggleObjectSerializer())),
]

ApiModelFile._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer(), optional=True),
]

ApiModelInstance._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("fineTunable", "fine_tunable", "_fine_tunable", bool, False, PredefinedSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("usage", "usage", "_usage", str, "", PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, "", PredefinedSerializer()),
  FieldMetadata("versionId", "version_id", "_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("trainingData", "training_data", "_training_data", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("licenseName", "license_name", "_license_name", str, "", PredefinedSerializer()),
  FieldMetadata("modelInstanceType", "model_instance_type", "_model_instance_type", ModelInstanceType, ModelInstanceType.MODEL_INSTANCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("baseModelInstanceInformation", "base_model_instance_information", "_base_model_instance_information", BaseModelInstanceInformation, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("externalBaseModelUrl", "external_base_model_url", "_external_base_model_url", str, "", PredefinedSerializer()),
]

ApiUpdateModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("usage", "usage", "_usage", str, "", PredefinedSerializer()),
  FieldMetadata("fineTunable", "fine_tunable", "_fine_tunable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("trainingData", "training_data", "_training_data", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("licenseName", "license_name", "_license_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceType", "model_instance_type", "_model_instance_type", ModelInstanceType, None, EnumSerializer(), optional=True),
  FieldMetadata("baseModelInstance", "base_model_instance", "_base_model_instance", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalBaseModelUrl", "external_base_model_url", "_external_base_model_url", str, None, PredefinedSerializer(), optional=True),
]

ApiUpdateModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

ApiUpdateModelResponse._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ref", "ref", "_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

ApiUploadModelFileRequest._fields = [
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedEpochSeconds", "last_modified_epoch_seconds", "_last_modified_epoch_seconds", int, 0, PredefinedSerializer()),
]

ApiUploadModelFileResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
]

