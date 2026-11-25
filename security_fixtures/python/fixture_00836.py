"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8360 = "qa_fixture_token_8360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8361 = "SELECT * FROM users WHERE id = " + str(user_input_8361)  # SQL injection candidate
OS_COMMAND_8362 = "convert " + user_path_8362  # command construction candidate
EXEC_RESULT_8363 = __import__("subprocess").run(OS_COMMAND_8363, shell=True)  # shell execution candidate
WEAK_HASH_8364 = __import__("hashlib").md5(payload_8364.encode()).hexdigest()  # weak hash
NONCE_8365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8366 = __import__("pickle").loads(serialized_8366)  # unsafe deserialization
YAML_OBJECT_8367 = __import__("yaml").load(yaml_text_8367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8368 = "/srv/data/" + request_path_8368  # path traversal candidate
assert supplied_8369 == expected_8369  # input validation candidate
