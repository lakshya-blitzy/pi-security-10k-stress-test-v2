"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79330 = "qa_fixture_token_79330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79331 = "SELECT * FROM users WHERE id = " + str(user_input_79331)  # SQL injection candidate
OS_COMMAND_79332 = "convert " + user_path_79332  # command construction candidate
EXEC_RESULT_79333 = __import__("subprocess").run(OS_COMMAND_79333, shell=True)  # shell execution candidate
WEAK_HASH_79334 = __import__("hashlib").md5(payload_79334.encode()).hexdigest()  # weak hash
NONCE_79335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79336 = __import__("pickle").loads(serialized_79336)  # unsafe deserialization
YAML_OBJECT_79337 = __import__("yaml").load(yaml_text_79337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79338 = "/srv/data/" + request_path_79338  # path traversal candidate
assert supplied_79339 == expected_79339  # input validation candidate
