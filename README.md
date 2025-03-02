# refraction_photon_mass
Simple but accurate visible frequency refraction program


The material has a scaling factor, permittivity, and permeability.
This gives a simple refraction index.
All of that is multiplied by a factor adjusted by the frequency of the photon.
 
This gives the refraction that can then be converted to an angle.

It is just that simple.


||
|Wavelength:  nm|
|  Empirical Refractive Index (n2): |
|  Predicted Refractive Index (n_pre): |
|  Refractive Index % Difference: %|
|  Snell's Law Angle (empirical): degrees|
|  Snell's Law Angle (predicted): degrees|
|  Angle % Difference: %|
|--------------------------------------------------|
|                                                  |
||
|Material: water|
|380  nm 1.3330 1.3356 0.1930% 2.2508 2.2464 0.1931%|
|460  nm 1.3300 1.3301 0.0044% 2.2559 2.2558 0.0044%|
|540  nm 1.3260 1.3258 0.0117% 2.2627 2.2629 0.0117%|
|620  nm 1.3230 1.3229 0.0047% 2.2678 2.2679 0.0047%|
|700  nm 1.3200 1.3200 0.0023% 2.2730 2.2730 0.0023%|
||
|Material: crown glass|
|380  nm 1.5230 1.5231 0.0080% 1.9699 1.9697 0.0080%|
|460  nm 1.5180 1.5168 0.0772% 1.9764 1.9779 0.0773%|
|540  nm 1.5120 1.5120 0.0015% 1.9842 1.9842 0.0015%|
|620  nm 1.5070 1.5087 0.1132% 1.9908 1.9885 0.1132%|
|700  nm 1.5020 1.5016 0.0262% 1.9974 1.9980 0.0262%|
||
|Material: flint glass|
|380  nm 1.6200 1.6147 0.3261% 1.8519 1.8579 0.3263%|
|460  nm 1.6120 1.6080 0.2455% 1.8611 1.8657 0.2456%|
|540  nm 1.6030 1.6029 0.0032% 1.8715 1.8716 0.0032%|
|620  nm 1.5960 1.5994 0.2147% 1.8797 1.8757 0.2148%|
|700  nm 1.5880 1.5921 0.2550% 1.8892 1.8844 0.2551%|
||
|Material: diamond|
|380  nm 2.4190 2.4015 0.7232% 1.2401 1.2491 0.7234%|
|460  nm 2.4020 2.3916 0.4338% 1.2489 1.2543 0.4339%|
|540  nm 2.3840 2.3840 0.0002% 1.2583 1.2583 0.0002%|
|620  nm 2.3690 2.3788 0.4110% 1.2663 1.2611 0.4111%|
|700  nm 2.3540 2.3667 0.5358% 1.2743 1.2675 0.5359%|
||
|Material: silicon|
|380  nm 3.9760 3.9882 0.3061% 0.7544 0.7521 0.3062%|
|460  nm 3.9690 3.9717 0.0687% 0.7558 0.7552 0.0687%|
|540  nm 3.9590 3.9591 0.0037% 0.7577 0.7576 0.0037%|
|620  nm 3.9520 3.9505 0.0388% 0.7590 0.7593 0.0388%|
|700  nm 3.9440 3.9351 0.2259% 0.7606 0.7623 0.2259%|
||
|Material: germanium|
|380  nm 4.0520 4.0494 0.0637% 0.7403 0.7408 0.0637%|
|460  nm 4.0370 4.0327 0.1070% 0.7430 0.7438 0.1070%|
|540  nm 4.0200 4.0199 0.0023% 0.7462 0.7462 0.0023%|
|620  nm 4.0070 4.0111 0.1021% 0.7486 0.7478 0.1021%|
|700  nm 3.9940 3.9970 0.0741% 0.7510 0.7505 0.0742%|
||
|Material: gallium arsenide|
|380  nm 3.8850 3.8895 0.1163% 0.7721 0.7712 0.1163%|
|460  nm 3.8740 3.8734 0.0142% 0.7743 0.7744 0.0142%|
|540  nm 3.8610 3.8612 0.0046% 0.7769 0.7769 0.0046%|
|620  nm 3.8500 3.8527 0.0704% 0.7791 0.7786 0.0704%|
|700  nm 3.8390 3.8382 0.0207% 0.7814 0.7815 0.0207%|
||
|Material: fused silica|
|380  nm 1.4580 1.4656 0.5215% 2.0577 2.0470 0.5217%|
|460  nm 1.4570 1.4596 0.1772% 2.0591 2.0555 0.1772%|
|540  nm 1.4550 1.4550 0.0026% 2.0620 2.0620 0.0026%|
|620  nm 1.4540 1.4518 0.1532% 2.0634 2.0666 0.1533%|
|700  nm 1.4530 1.4431 0.6783% 2.0648 2.0789 0.6786%|
||
|Material: barium titanate|
|380  nm 2.4130 2.4147 0.0700% 1.2432 1.2423 0.0700%|
|460  nm 2.4060 2.4047 0.0536% 1.2468 1.2475 0.0536%|
|540  nm 2.3970 2.3971 0.0039% 1.2515 1.2514 0.0039%|
|620  nm 2.3910 2.3918 0.0351% 1.2546 1.2542 0.0351%|
|700  nm 2.3840 2.3885 0.1877% 1.2583 1.2559 0.1877%|
||
|Material: lithium niobate|
|380  nm 2.2360 2.2352 0.0359% 1.3416 1.3421 0.0359%|
|460  nm 2.2290 2.2260 0.1364% 1.3458 1.3476 0.1365%|
|540  nm 2.2190 2.2189 0.0042% 1.3519 1.3519 0.0042%|
|620  nm 2.2130 2.2140 0.0471% 1.3555 1.3549 0.0471%|
|700  nm 2.2060 2.2075 0.0677% 1.3598 1.3589 0.0677%|



