console.log("Seat.js loaded");

function selectSeat(seatId, seatNumber) {
  // Tandai seat yang dipilih
  const selectedSeat = document.querySelector(`[data-seat-id="${seatId}"]`);
  selectedSeat.classList.add("selected");

  console.log("Seat clicked:", seatId, seatNumber);

  // Update hidden input dengan nilai seat yang dipilih
  document.getElementById("selected-seat-id").value = seatId;
  document.getElementById("selected-seat-number").value = seatNumber;

  // condition if selected
  if (seatId) {
    const seat = (document.getElementById("selected-seat-number").value = seatNumber);

    seat.removeAttribute("onclick");
  }
}
