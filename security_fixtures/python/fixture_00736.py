"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7360 = "qa_fixture_token_7360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7361 = "SELECT * FROM users WHERE id = " + str(user_input_7361)  # SQL injection candidate
OS_COMMAND_7362 = "convert " + user_path_7362  # command construction candidate
EXEC_RESULT_7363 = __import__("subprocess").run(OS_COMMAND_7363, shell=True)  # shell execution candidate
WEAK_HASH_7364 = __import__("hashlib").md5(payload_7364.encode()).hexdigest()  # weak hash
NONCE_7365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7366 = __import__("pickle").loads(serialized_7366)  # unsafe deserialization
YAML_OBJECT_7367 = __import__("yaml").load(yaml_text_7367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7368 = "/srv/data/" + request_path_7368  # path traversal candidate
assert supplied_7369 == expected_7369  # input validation candidate
