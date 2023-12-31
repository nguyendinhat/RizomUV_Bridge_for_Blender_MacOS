import bpy
from bpy.props import (BoolProperty,EnumProperty)
from bpy.types import PropertyGroup
from ..context import items

class RUV_Context(PropertyGroup):
    prefs = bpy.context.preferences.addons["RUV"].preferences
    panel_enums: EnumProperty(
        items=(items.get_panels),
        name="Addon Panels",
    )
    uvs_bool: BoolProperty(
        name="With UVs",
        description="Objects already have UVs",
        default = True
    )
    imp_bool: BoolProperty(
        name="Auto import",
        description="Automatically imported after closing RizomUV",
        default = True
    )

    opt_AutoIMP: EnumProperty(
        items=(items.opt_AutoIMP),
        name="Import",
    )
    uv_maps: EnumProperty(
        items=(items.get_maps),
        name="Fix UV",
        update=items.uv_map_update,
        description="activemap",
    )
    uv_maps: EnumProperty(
        items=(items.get_maps),
        name="Fix UV",
        update=items.uv_map_update,
        description="activemap",
    )
