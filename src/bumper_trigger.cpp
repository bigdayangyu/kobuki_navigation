#include <iostream>
#include <memory>
#include <mutex>
#include <string>

#include "kobuki_msgs/msg/bumper_event.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/bool.hpp"
#include "std_msgs/msg/string.hpp"

void toggleCallback(
	const kobuki_msgs::msg::BumperEvent::SharedPtr data,
	std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String>> pub)
{
	static std_msgs::msg::String dock_msg;
	static int counter = 0;
	
	if(data->bumper >= 2){
  	  counter++;
  	} else {
  	  counter = 0;
  	}
  	if (counter >= 100) {
  		std::cout << "FIREEEEEEEEEE!!!!" << std::endl;
  		dock_msg.data = "robot_docked";
  		pub->publish(dock_msg);
  	}
	std::cout << "I heard: [" << (size_t)data->bumper << "]" << std::endl;
}

//create a publisher
int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  // create a node
  auto node = rclcpp::Node::make_shared("kobuki_bumper_detector");
  // create publishers 
  auto toggle_pub = node->create_publisher<std_msgs::msg::String>("command", 10);

  std::function<void(const kobuki_msgs::msg::BumperEvent::SharedPtr)> fcn =
    std::bind(&toggleCallback, std::placeholders::_1, toggle_pub);
  auto bumper_sub = node->create_subscription<kobuki_msgs::msg::BumperEvent>(
  	"bumper_event", rclcpp::SystemDefaultsQoS(), fcn);
  
  rclcpp::spin(node);

  return 0;
}