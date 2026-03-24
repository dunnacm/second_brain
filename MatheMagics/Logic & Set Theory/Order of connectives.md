---
down:
tags:
  - mathemagics/mathematicalLogic_and_setTheory
---
## Order
1. Propositional forms in [[Grouping symbols]] (parenthesis or brackets)
2. [[Negation]]
3. [[Conjunction]]
4. [[(Logical) Disjunction ⇔ Inclusive or]]
5. [[Conditionals]]
6. [[Biconditionals]]

## Examples
### Example 1
Unparenthesized form:
$$\neg \mathtt{P}\lor \mathtt{Q}\land \mathtt{R}\to \mathtt{S}$$

Parsed as:
$$\bigl(\neg \mathtt{P}\lor (\mathtt{Q}\land \mathtt{R})\bigr)\to \mathtt{S}$$


### Example 2
Unparenthesized form:
$$\mathtt{P}\leftrightarrow \mathtt{Q}\to \neg \mathtt{R}\lor \mathtt{S}\land \mathtt{T}$$

Parsed as:
$$\mathtt{P}\leftrightarrow \bigl(\mathtt{Q}\to (\neg \mathtt{R}\lor (\mathtt{S}\land \mathtt{T}))\bigr)$$


### Example 3
Unparenthesized form:
$$\neg \mathtt{P}\land \mathtt{Q}\lor \mathtt{R}\leftrightarrow \mathtt{S}\to \mathtt{T}$$

Parsed as:
$$\bigl((\neg \mathtt{P}\land \mathtt{Q})\lor \mathtt{R}\bigr)\leftrightarrow (\mathtt{S}\to \mathtt{T})$$



### Example 4
Unparenthesized form:
$$\mathtt{P}\to \mathtt{Q}\land \mathtt{R}\lor \neg \mathtt{S}\leftrightarrow \mathtt{T}$$

Parsed as:
$$\bigl(\mathtt{P}\to ((\mathtt{Q}\land \mathtt{R})\lor \neg \mathtt{S})\bigr)\leftrightarrow \mathtt{T}$$



### Example 5
Unparenthesized form:
$$\neg \mathtt{P}\leftrightarrow \mathtt{Q}\lor \mathtt{R}\to \mathtt{S}\land \neg \mathtt{T}$$

Parsed as:
$$\neg \mathtt{P}\leftrightarrow \bigl((\mathtt{Q}\lor \mathtt{R})\to (\mathtt{S}\land \neg \mathtt{T})\bigr)$$



### Example 6
Unparenthesized form:
$$\mathtt{P}\to \mathtt{Q}\to \mathtt{R}\lor \mathtt{S}\land \neg \mathtt{T}$$

Parsed as:
$$\mathtt{P}\to \bigl(\mathtt{Q}\to (\mathtt{R}\lor (\mathtt{S}\land \neg \mathtt{T}))\bigr)$$



### Example 7
Unparenthesized form:
$$\mathtt{P}\leftrightarrow \mathtt{Q}\leftrightarrow \mathtt{R}\to \mathtt{S}\lor \neg \mathtt{T}$$

Parsed as:
$$\mathtt{P}\leftrightarrow \bigl(\mathtt{Q}\leftrightarrow (\mathtt{R}\to (\mathtt{S}\lor \neg \mathtt{T}))\bigr)$$



### Example 8
Unparenthesized form:
$$\neg \mathtt{P}\land \neg \mathtt{Q}\lor \mathtt{R}\to \mathtt{S}\leftrightarrow \mathtt{T}$$

Parsed as:
$$\bigl((\neg \mathtt{P}\land \neg \mathtt{Q})\lor \mathtt{R}\to \mathtt{S}\bigr)\leftrightarrow \mathtt{T}$$

Since $\to$ binds more strongly than $\leftrightarrow$ but less strongly than $\lor$, this is:
$$\bigl(((\neg \mathtt{P}\land \neg \mathtt{Q})\lor \mathtt{R})\to \mathtt{S}\bigr)\leftrightarrow \mathtt{T}$$



### Example 9
Unparenthesized form:
$$\mathtt{P}\land \mathtt{Q}\to \mathtt{R}\leftrightarrow \neg \mathtt{S}\lor \mathtt{T}\land \mathtt{U}$$

Parsed as:
$$\bigl((\mathtt{P}\land \mathtt{Q})\to \mathtt{R}\bigr)\leftrightarrow \bigl(\neg \mathtt{S}\lor (\mathtt{T}\land \mathtt{U})\bigr)$$


### Example 10
Unparenthesized form:
$$\neg \mathtt{P}\to \mathtt{Q}\leftrightarrow \mathtt{R}\to \mathtt{S}\leftrightarrow \mathtt{T}$$

Parsed as:
$$\bigl(\neg \mathtt{P}\to \mathtt{Q}\bigr)\leftrightarrow \bigl((\mathtt{R}\to \mathtt{S})\leftrightarrow \mathtt{T}\bigr)$$



## Good self-test prompts
For each of the following, try to parenthesize before checking:
$$\mathtt{P}\lor \mathtt{Q}\to \mathtt{R}\leftrightarrow \mathtt{S}\land \neg \mathtt{T}$$

$$\neg \mathtt{P}\lor \mathtt{Q}\leftrightarrow \mathtt{R}\to \mathtt{S}\land \mathtt{T}$$
