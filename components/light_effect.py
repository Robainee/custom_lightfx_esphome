
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light
from esphome.const import CONF_NAME

CONF_GROUP_SIZE = "group_size"
CONF_REVERSE = "reverse"
CONF_NUM_LEDS = "num_leds"
CONF_NUM_GRAD = "num_grad"
CONF_GRADIENT = "gradient"

rainbow_ns = cg.esphome_ns.namespace('custom_rainbow')
colorwipe_ns = cg.esphome_ns.namespace('custom_colorwipe')

RainbowEffect = rainbow_ns.class_('CustomRainbowEffect', light.AddressableLightEffect)
ColorWipeEffect = colorwipe_ns.class_('CustomColorWipeEffect', light.AddressableLightEffect)

SHARED_SCHEMA = {
    cv.Required(CONF_NAME): cv.string,
    cv.Optional(CONF_GROUP_SIZE, default=1): cv.int_,
    cv.Optional(CONF_REVERSE, default=False): cv.boolean,
    cv.Optional(CONF_NUM_LEDS, default=1): cv.int_,
    cv.Optional(CONF_NUM_GRAD, default=1): cv.int_,
    cv.Optional(CONF_GRADIENT, default=False): cv.boolean,
}

CONFIG_SCHEMA = cv.Schema({
    cv.Optional("addressable_custom_rainbow"): light.ADDRESSABLE_LIGHT_EFFECT_SCHEMA.extend(SHARED_SCHEMA),
    cv.Optional("addressable_custom_colorwipe"): light.ADDRESSABLE_LIGHT_EFFECT_SCHEMA.extend(SHARED_SCHEMA),
})

async def to_code(config):
    if "addressable_custom_rainbow" in config:
        conf = config["addressable_custom_rainbow"]
        var = cg.new_Pvariable(conf[CONF_ID])
        await light.register_effect(var, conf[CONF_NAME])
        cg.add(var.set_group_size(conf[CONF_GROUP_SIZE]))
        cg.add(var.set_reverse(conf[CONF_REVERSE]))
        cg.add(var.set_num_leds(conf[CONF_NUM_LEDS]))
        cg.add(var.set_num_grad(conf[CONF_NUM_GRAD]))
        cg.add(var.set_gradient(conf[CONF_GRADIENT]))

    if "addressable_custom_colorwipe" in config:
        conf = config["addressable_custom_colorwipe"]
        var = cg.new_Pvariable(conf[CONF_ID])
        await light.register_effect(var, conf[CONF_NAME])
        cg.add(var.set_group_size(conf[CONF_GROUP_SIZE]))
        cg.add(var.set_reverse(conf[CONF_REVERSE]))
        cg.add(var.set_num_leds(conf[CONF_NUM_LEDS]))
        cg.add(var.set_num_grad(conf[CONF_NUM_GRAD]))
        cg.add(var.set_gradient(conf[CONF_GRADIENT]))
