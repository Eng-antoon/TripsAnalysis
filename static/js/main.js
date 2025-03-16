function updateRouteQuality(tripId) {
    const routeQualitySelect = document.getElementById("routeQualitySelect");
    const selectedQuality = routeQualitySelect.value;
  
    if (!selectedQuality) {
      alert("Please select a route quality value.");
      return;
    }
  
    fetch("/update_route_quality", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        trip_id: tripId,
        route_quality: selectedQuality
      })
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          alert("Route quality updated successfully!");
        } else {
          alert("Error: " + data.message);
        }
      })
      .catch((err) => {
        console.error(err);
        alert("An error occurred while updating route quality.");
      });
  }
  
  document.querySelectorAll('.update-route-quality-btn').forEach(function(button) {
    button.addEventListener('click', function() {
      const tripId = this.getAttribute('data-trip-id');
      updateRouteQuality(tripId);
    });
  });
      