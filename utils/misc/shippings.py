from aiogram import types
from aiogram.types import LabeledPrice

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo(3 kun)",
    prices=[
        LabeledPrice(
                    'Maxsus quti', 1000000),
        LabeledPrice(
            '3 ish kunida yetkazish', 5000000),   
    ]
)

FAST_SHIPPING =types.ShippingOption(
    id='post_reg',
    title="Express pochta (1 kun)",
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 7000000),
    
    ]

)

PICKUP_SHIPPING = types.ShippingOption(id='pikup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                            LabeledPrice("Yetkazib berishsiz", -5000000)
                                       ])

                                        