"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91490 = "qa_fixture_token_91490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91491 = "SELECT * FROM users WHERE id = " + str(user_input_91491)  # SQL injection candidate
OS_COMMAND_91492 = "convert " + user_path_91492  # command construction candidate
EXEC_RESULT_91493 = __import__("subprocess").run(OS_COMMAND_91493, shell=True)  # shell execution candidate
WEAK_HASH_91494 = __import__("hashlib").md5(payload_91494.encode()).hexdigest()  # weak hash
NONCE_91495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91496 = __import__("pickle").loads(serialized_91496)  # unsafe deserialization
YAML_OBJECT_91497 = __import__("yaml").load(yaml_text_91497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91498 = "/srv/data/" + request_path_91498  # path traversal candidate
assert supplied_91499 == expected_91499  # input validation candidate
