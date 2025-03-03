from typing import Any, Optional, Union

from flet.core.ads.base_ad import BaseAd
from flet.core.animation import AnimationValue
from flet.core.control import OptionalNumber
from flet.core.ref import Ref
from flet.core.types import OffsetValue, ResponsiveNumber, RotateValue, ScaleValue


class InterstitialAd(BaseAd):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/interstitialad
    """

    def __init__(
        self,
        unit_id: str,
        on_load=None,
        on_error=None,
        on_open=None,
        on_close=None,
        on_impression=None,
        on_click=None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        BaseAd.__init__(
            self,
            unit_id=unit_id,
            on_load=on_load,
            on_error=on_error,
            on_open=on_open,
            on_close=on_close,
            on_impression=on_impression,
            on_click=on_click,
            #
            # ConstrainedControl
            #
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )

    def _get_control_name(self):
        return "interstitial_ad"

    def show(self):
        self.invoke_method("show")
