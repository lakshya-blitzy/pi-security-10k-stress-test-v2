"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15330 = "qa_fixture_token_15330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15331 = "SELECT * FROM users WHERE id = " + str(user_input_15331)  # SQL injection candidate
OS_COMMAND_15332 = "convert " + user_path_15332  # command construction candidate
EXEC_RESULT_15333 = __import__("subprocess").run(OS_COMMAND_15333, shell=True)  # shell execution candidate
WEAK_HASH_15334 = __import__("hashlib").md5(payload_15334.encode()).hexdigest()  # weak hash
NONCE_15335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15336 = __import__("pickle").loads(serialized_15336)  # unsafe deserialization
YAML_OBJECT_15337 = __import__("yaml").load(yaml_text_15337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15338 = "/srv/data/" + request_path_15338  # path traversal candidate
assert supplied_15339 == expected_15339  # input validation candidate
