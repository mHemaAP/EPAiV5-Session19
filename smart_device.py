from typing import Any, Callable

class SmartDevice:
    """
    Smart device class which manages all the smart devices connected.
    """
    # Class attribute for device count
    device_count = 0

    def __init__(self, device_name: str, model_number: str, device_online: bool = False):
        """
        Initializes the object with 
        
        Params:
        device_name:      A string representing IOT device Part Name
        model_number:     A string representing IOT device Model Number
        device_online:    Status of the IOT device (default is False)

        Returns:
        None
        """
        if not isinstance(device_name, str):
            raise TypeError("device_name should be of type 'str'")
        if not isinstance(model_number, str):
            raise TypeError("model_number should be of type 'str'")
        if not isinstance(device_online, bool):
            raise TypeError("device_online should be of type 'bool'")

        # Required attributes initialization
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = device_online
        self.status = {}

        # Increment device count
        SmartDevice.device_count += 1

    def update_status(self, attribute: str, value: Any) -> None:
        """
        Updates the status of the connected device.
        """
        # Update status dictionary
        self.status[attribute] = value

    def get_status(self, attribute: str) -> Any:
        """
        Gets the status of a particular parameter of a smart device.
        """
        # Get status with default return for missing attributes
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self) -> None:
        """
        Toggles the device's online status between True and False.
        """
        # Toggle online status
        self.is_online = not self.is_online

    def reset(self) -> None:
        """
        Resets all status attributes to their default values (clears the status dictionary).
        """
        # Reset status dictionary
        self.status.clear()        

    def __call__(self) -> str:
        """
        Makes the object callable and returns basic device information.
        """
        # Make the class callable and returns formatted string
        return f"{self.device_name} (Model: {self.model_number})"
    
    @property
    def device_info(self) -> Callable[[], str]:
        """        
        This provides device information as a callable function.
        """
        if hasattr(self, "_custom_device_info"):
            return self._custom_device_info
        else:
            def default_info() -> str:
                return f"Device Name: {self.device_name}, Model: {self.model_number}, Online: {self.is_online}"
            return default_info 
    
    @device_info.setter
    def device_info(self, custom_callable: Callable[[], str]) -> None:
        """  
        Sets a custom callable for the device information.
        """
        if not callable(custom_callable):
            raise TypeError("device_info must be a callable")
        self._custom_device_info = custom_callable  