
#include "custom_colorwipe.h"
#include "esphome/core/log.h"
#include "esphome/components/light/light_output.h"

namespace esphome {
namespace custom_colorwipe {

void CustomColorWipeEffect::apply(light::AddressableLight &it, const size_t, const float progress) {
  static int step = 0;
  it.all() = light::ESPColor(0, 0, 0);
  int direction = this->reverse_ ? -1 : 1;
  int max_step = it.size() / this->group_size_;

  for (int i = 0; i < step * this->group_size_; i++) {
    light::ESPColor color = light::ESPColor::WHITE;
    it[i] = color;
  }

  step += direction;
  if (step >= max_step || step < 0) {
    step = 0;
  }
}

}  // namespace custom_colorwipe
}  // namespace esphome
