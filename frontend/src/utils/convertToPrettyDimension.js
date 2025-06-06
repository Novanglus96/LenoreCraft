function convertToFraction(decimalInches) {
  decimalInches = parseFloat(decimalInches);
  if (isNaN(decimalInches) || decimalInches < 0) {
    throw new Error("Input must be a positive number.");
  }

  const feet = Math.floor(decimalInches / 12);
  const inches = Math.floor(decimalInches % 12);
  const fractionalInch = decimalInches % 1;

  // Helper to convert decimal to fractional inch
  function getFractionalInch(value) {
    const fractions = [
      { value: 0.875, fraction: "7/8" },
      { value: 0.75, fraction: "3/4" },
      { value: 0.625, fraction: "5/8" },
      { value: 0.5, fraction: "1/2" },
      { value: 0.375, fraction: "3/8" },
      { value: 0.25, fraction: "1/4" },
      { value: 0.125, fraction: "1/8" },
      { value: 0, fraction: "" },
    ];

    for (const { value: cutoff, fraction } of fractions) {
      if (value >= cutoff) return fraction;
    }
    return "";
  }

  const fractionalPart = getFractionalInch(fractionalInch);
  let prettyDimension = "";

  if (feet && !inches && !fractionalPart) {
    // Whole feet only (e.g., 12, 24)
    prettyDimension += `${feet}'`;
  } else if (!feet && !inches && fractionalPart) {
    // Fractional inch only (e.g., 0.75)
    prettyDimension += `${fractionalPart}"`;
  } else {
    // Combination of feet, inches, and fractional part
    if (feet) prettyDimension += `${feet}' `;
    if (inches) prettyDimension += `${inches}`;
    if (fractionalPart) prettyDimension += ` ${fractionalPart}`;
    if (inches || fractionalPart) prettyDimension += `"`;
  }

  return prettyDimension.trim();
}

export function convertToPrettyDimension(ht, w, ld, lumber = false) {
  // If this is lumber, [Nominal Thickness] x [Nominal Width] x [Length] [Wood Type]
  let dimensions = null;
  let ht_str = null;
  let w_str = null;
  let ld_str = null;
  if (ht) {
    ht_str = convertToFraction(ht);
  }
  if (w) {
    w_str = convertToFraction(w);
  }
  if (ld) {
    ld_str = convertToFraction(ld);
  }
  if (lumber) {
    if (ht_str) {
      dimensions = ht_str + "x";
    }
    if (w_str) {
      dimensions += w_str + "x";
    }
    if (ld_str) {
      dimensions += ld_str;
    }
  } else {
    if (ht_str) {
      dimensions = ht_str + "x";
    }
    if (w_str) {
      dimensions += w_str + "x";
    }
    if (ld_str) {
      dimensions += ld_str;
    }
  }
  if (!dimensions) {
    dimensions = "(none)";
  }
  // If this is a finished product, 	Height x Width x Depth/Length
  return dimensions;
}
