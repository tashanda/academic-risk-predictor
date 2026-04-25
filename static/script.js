let difficulty = 1;

function updateSlider() {
  const value = document.getElementById("study_hours").value;
  document.getElementById("hours-out").textContent = value + " hrs";
}

function setDifficulty(value, button) {
  difficulty = value;

  document.querySelectorAll(".diff-btn").forEach(btn => {
    btn.classList.remove("active");
  });

  button.classList.add("active");
}

function getPrediction() {
  const grade = Number(document.getElementById("current_grade").value);
  const missing = Number(document.getElementById("missing_assignments").value);
  const attendance = Number(document.getElementById("attendance").value);
  const sleep = Number(document.getElementById("sleep_hours").value);
  const study = Number(document.getElementById("study_hours").value);

  const predicted = Math.max(0, Math.min(100,
    grade + study * 0.5 + (attendance - 80) * 0.2 + (sleep - 7) * 1.5 - difficulty * 4 - missing * 3
  ));

  const riskScore = Math.round(100 - predicted);

  let risk = "Low Risk";
  let color = "#22c55e";

  if (riskScore >= 75) {
    risk = "Critical Risk";
    color = "#ef4444";
  } else if (riskScore >= 50) {
    risk = "High Risk";
    color = "#f97316";
  } else if (riskScore >= 25) {
    risk = "Moderate Risk";
    color = "#facc15";
  }

  document.getElementById("placeholder").style.display = "none";
  document.getElementById("results-content").style.display = "flex";

  document.getElementById("risk-badge").textContent = risk;
  document.getElementById("risk-badge").style.color = color;
  document.getElementById("risk-badge").style.borderColor = color;
  document.getElementById("risk-badge").style.background = color + "22";

  document.getElementById("pred-grade").textContent = Math.round(predicted) + "%";
  document.getElementById("pred-grade").style.color = color;

  document.getElementById("gauge-pct").textContent = riskScore + "%";
  document.getElementById("gauge-pct").style.color = color;

  document.getElementById("gauge-fill").style.width = riskScore + "%";
  document.getElementById("gauge-fill").style.background = color;

  document.getElementById("bd-grade").textContent = grade >= 75 ? "Good" : "Needs work";
  document.getElementById("bd-attend").textContent = attendance >= 80 ? "Good" : "Low";
  document.getElementById("bd-study").textContent = study >= 10 ? "Good" : "Low";
  document.getElementById("bd-diff").textContent = ["Easy", "Medium", "Hard", "Extreme"][difficulty - 1];

  document.getElementById("result-rec").textContent =
    "Consider increasing study hours, reducing missing work, and attending office hours to improve your grade.";
}