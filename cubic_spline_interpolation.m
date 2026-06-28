% =========================================================
% NUMERICAL ANALYSIS: CUBIC SPLINE INTERPOLATION
% Natural vs. Clamped Boundary Conditions
% =========================================================

clear; clc; close all;

% 1. Generate 20 arbitrary data points
n_points = 20;
x = linspace(0, 2*pi, n_points);
y = sin(x) + 0.5*cos(2*x);

% High-resolution query points for smooth plotting
xq = linspace(min(x), max(x), 200);
n = length(x) - 1;
h = diff(x);

%% --- NATURAL CUBIC SPLINE ---
% Boundary conditions: S''(x_0) = 0, S''(x_n) = 0
A_nat = zeros(n+1, n+1);
b_nat = zeros(n+1, 1);
A_nat(1,1) = 1;
A_nat(n+1, n+1) = 1;

for i = 2:n
    A_nat(i, i-1) = h(i-1);
    A_nat(i, i)   = 2*(h(i-1) + h(i));
    A_nat(i, i+1) = h(i);
    b_nat(i)      = 3/h(i)*(y(i+1) - y(i)) - 3/h(i-1)*(y(i) - y(i-1));
end

c_nat = A_nat \ b_nat; % Solve linear system

% Calculate coefficients
b_coeff_nat = zeros(n, 1); d_coeff_nat = zeros(n, 1);
for i = 1:n
    b_coeff_nat(i) = (y(i+1) - y(i))/h(i) - h(i)*(c_nat(i+1) + 2*c_nat(i))/3;
    d_coeff_nat(i) = (c_nat(i+1) - c_nat(i))/(3*h(i));
end

% Evaluate Natural Spline
yq_nat = zeros(size(xq));
for k = 1:length(xq)
    idx = find(x <= xq(k), 1, 'last');
    if isempty(idx) || idx == n+1, idx = n; end
    dx = xq(k) - x(idx);
    yq_nat(k) = y(idx) + b_coeff_nat(idx)*dx + c_nat(idx)*dx^2 + d_coeff_nat(idx)*dx^3;
end

%% --- CLAMPED CUBIC SPLINE ---
% Boundary conditions: S'(x_0) = f'(x_0), S'(x_n) = f'(x_n)
fp_start = 1; fp_end = -1;

A_clamp = zeros(n+1, n+1);
b_clamp = zeros(n+1, 1);
A_clamp(1,1) = 2*h(1); A_clamp(1,2) = h(1);
b_clamp(1)   = 3/h(1)*(y(2) - y(1)) - 3*fp_start;
A_clamp(n+1, n)   = h(n); A_clamp(n+1, n+1) = 2*h(n);
b_clamp(n+1)      = 3*fp_end - 3/h(n)*(y(n+1) - y(n));

for i = 2:n
    A_clamp(i, i-1) = h(i-1);
    A_clamp(i, i)   = 2*(h(i-1) + h(i));
    A_clamp(i, i+1) = h(i);
    b_clamp(i)      = 3/h(i)*(y(i+1) - y(i)) - 3/h(i-1)*(y(i) - y(i-1));
end

c_clamp = A_clamp \ b_clamp;

% Calculate coefficients
b_coeff_clamp = zeros(n, 1); d_coeff_clamp = zeros(n, 1);
for i = 1:n
    b_coeff_clamp(i) = (y(i+1) - y(i))/h(i) - h(i)*(c_clamp(i+1) + 2*c_clamp(i))/3;
    d_coeff_clamp(i) = (c_clamp(i+1) - c_clamp(i))/(3*h(i));
end

% Evaluate Clamped Spline
yq_clamp = zeros(size(xq));
for k = 1:length(xq)
    idx = find(x <= xq(k), 1, 'last');
    if isempty(idx) || idx == n+1, idx = n; end
    dx = xq(k) - x(idx);
    yq_clamp(k) = y(idx) + b_coeff_clamp(idx)*dx + c_clamp(idx)*dx^2 + d_coeff_clamp(idx)*dx^3;
end

%% --- PLOTTING ---
figure;
subplot(2,1,1);
plot(x, y, 'ko', 'MarkerFaceColor', 'k'); hold on; plot(xq, yq_nat, 'b-', 'LineWidth', 1.5);
title('Natural Cubic Spline Interpolation'); grid on; legend('Data Points', 'Natural Spline');

subplot(2,1,2);
plot(x, y, 'ko', 'MarkerFaceColor', 'k'); hold on; plot(xq, yq_clamp, 'r-', 'LineWidth', 1.5);
title('Clamped Cubic Spline Interpolation'); grid on; legend('Data Points', 'Clamped Spline');
