import os
import sys
from importlib import import_module
from ludic.web.endpoints import Endpoint


def cached_import(module_path, class_name):
    # Check whether module is loaded and fully initialized.
    if not (
        (module := sys.modules.get(module_path))
        and (spec := getattr(module, "__spec__", None))
        and getattr(spec, "_initializing", False) is False
    ):
        module = import_module(module_path)
    return getattr(module, class_name)


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    try:
        return cached_import(module_path, class_name)
    except AttributeError as err:
        raise ImportError(
            'Module "%s" does not define a "%s" attribute/class'
            % (module_path, class_name)
        ) from err


def module_dir(module):
    """
    Find the name of the directory that contains a module, if possible.

    Raise ValueError otherwise, e.g. for namespace packages that are split
    over several directories.
    """
    # Convert to list because __path__ may not support indexing.
    paths = list(getattr(module, "__path__", []))
    if len(paths) == 1:
        return paths[0]
    else:
        filename = getattr(module, "__file__", None)
        if filename is not None:
            return os.path.dirname(filename)
    raise ValueError("Cannot determine directory containing %s" % module)


def autodiscover_modules(app, app_path):
    module_map = {}

    for root, dirs, files in os.walk(app_path):
        for file in files:
            if file in ("page.py", "endpoint.py", "layout.py"):
                module_path = os.path.join(root, file)
                module_type = file.replace(".py", "")                
                module_name = os.path.splitext(os.path.relpath(module_path, app_path).replace(os.sep, '.'))[0]  
                module_name = f"app.{module_name}"              
                
                try:
                    module = import_module(module_name)                   
                    module_url = "/%s" % "/".join(module_name.split(".")[1:-1]) 
                    module_url = module_url.replace("[", "{").replace("]", "}")
                    module_map[module_name] = module

                    if module_name.endswith(".page"):
                        module_index_handler = getattr(module, "index")
                        
                        if module_index_handler:
                            app.add_route(module_url, module_index_handler, methods=["GET"], include_in_schema=True)
                        
                    elif module_name.endswith(".endpoint"):

                        module_index_handler = getattr(module, "index", None)
                        
                        if module_index_handler:
                            app.add_route(module_url, module_index_handler, methods=["GET"], include_in_schema=True)                        

                        for name in module.__dict__.keys():
                            module_endpoint = module.__dict__.get(name)
                            

                            if type(module_endpoint).__name__ == "ABCMeta" and module_endpoint.__name__ != "Endpoint"  and issubclass(module_endpoint, Endpoint):
                                module_endpoint.app = app
                                app.add_route(module_url, module_endpoint, include_in_schema=True)                                

                except Exception as ex:
                    print(f"Error importing module {module_name}: {ex}")

    return module_map



