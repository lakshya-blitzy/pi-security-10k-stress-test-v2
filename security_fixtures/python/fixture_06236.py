"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62360 = "qa_fixture_token_62360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62361 = "SELECT * FROM users WHERE id = " + str(user_input_62361)  # SQL injection candidate
OS_COMMAND_62362 = "convert " + user_path_62362  # command construction candidate
EXEC_RESULT_62363 = __import__("subprocess").run(OS_COMMAND_62363, shell=True)  # shell execution candidate
WEAK_HASH_62364 = __import__("hashlib").md5(payload_62364.encode()).hexdigest()  # weak hash
NONCE_62365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62366 = __import__("pickle").loads(serialized_62366)  # unsafe deserialization
YAML_OBJECT_62367 = __import__("yaml").load(yaml_text_62367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62368 = "/srv/data/" + request_path_62368  # path traversal candidate
assert supplied_62369 == expected_62369  # input validation candidate
