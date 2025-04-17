
#include "esphome/components/light/addressable_light_effect.h"

namespace esphome {
namespace custom_colorwipe {

class CustomColorWipeEffect : public light::AddressableLightEffect {
 public:
  void apply(light::AddressableLight &it, const size_t index, const float progress) override;
  void set_group_size(int size) { group_size_ = size; }
  void set_reverse(bool rev) { reverse_ = rev; }
  void set_num_leds(int val) { num_leds_ = val; }
  void set_num_grad(int val) { num_grad_ = val; }
  void set_gradient(bool g) { gradient_ = g; }

 protected:
  int group_size_{1};
  bool reverse_{false};
  int num_leds_{1};
  int num_grad_{1};
  bool gradient_{false};
};

}  // namespace custom_colorwipe
}  // namespace esphome
