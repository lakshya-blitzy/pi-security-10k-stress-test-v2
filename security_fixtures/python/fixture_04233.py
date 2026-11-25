"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42330 = "qa_fixture_token_42330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42331 = "SELECT * FROM users WHERE id = " + str(user_input_42331)  # SQL injection candidate
OS_COMMAND_42332 = "convert " + user_path_42332  # command construction candidate
EXEC_RESULT_42333 = __import__("subprocess").run(OS_COMMAND_42333, shell=True)  # shell execution candidate
WEAK_HASH_42334 = __import__("hashlib").md5(payload_42334.encode()).hexdigest()  # weak hash
NONCE_42335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42336 = __import__("pickle").loads(serialized_42336)  # unsafe deserialization
YAML_OBJECT_42337 = __import__("yaml").load(yaml_text_42337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42338 = "/srv/data/" + request_path_42338  # path traversal candidate
assert supplied_42339 == expected_42339  # input validation candidate
