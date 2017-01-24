.. _canvas-programmer-guide-valuepersistance:

Port value persistence
====================================

Port values can be persisted (saved) under specific circumstances. When an input port is edited in the UI, a `defaultValue` is associated with node's input port and will be saved with the graph. Additionally, top graph ports can be set as persistable, using `Edit Port -> metadata -> persist value` (see :ref:`canvas-user-guide-port-options`).

In order to persist a port's value, a different mechanism is used depending on the value type:

- Persisted KL Object values must implement the `RTValToJSONEncoder` and `RTValFromJSONDecoder` KL interfaces, which define
  the `String convertToString!()` and `Boolean convertFromString!(String data)` methods, respectively. If these are not implemented, a warning will be issued.

  .. note:: Data compatibility between KL changes or extension versions must be handled by the user, in its persisted `String`, as there is no built-in versioning system

- Other KL types (base types, structs, arrays...) will be saved as a deep `json` traversal of their data members. Users must be careful as Objects members will be deeply traversed too.
