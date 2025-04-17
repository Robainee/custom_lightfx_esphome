
#include "custom_rainbow.h"
#include "esphome/core/log.h"
#include "esphome/components/light/light_output.h"

namespace esphome {
namespace custom_rainbow {

void CustomRainbowEffect::apply(light::AddressableLight &it, const size_t, const float progress) {
  const float speed = 8.0;
  const float phase = this->reverse_ ? -360.0 : 360.0;
  for (int i = 0; i < it.size(); i++) {
    int led_group = i / this->group_size_;
    float hue = fmod((progress * phase) + (led_group * 10.0), 360.0f);
    it[i] = light::ESPHSVColor(hue, 1.0f, 1.0f);
  }
}

}  // namespace custom_rainbow
}  // namespace esphome
