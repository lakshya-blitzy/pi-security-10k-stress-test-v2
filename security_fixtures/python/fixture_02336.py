"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23360 = "qa_fixture_token_23360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23361 = "SELECT * FROM users WHERE id = " + str(user_input_23361)  # SQL injection candidate
OS_COMMAND_23362 = "convert " + user_path_23362  # command construction candidate
EXEC_RESULT_23363 = __import__("subprocess").run(OS_COMMAND_23363, shell=True)  # shell execution candidate
WEAK_HASH_23364 = __import__("hashlib").md5(payload_23364.encode()).hexdigest()  # weak hash
NONCE_23365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23366 = __import__("pickle").loads(serialized_23366)  # unsafe deserialization
YAML_OBJECT_23367 = __import__("yaml").load(yaml_text_23367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23368 = "/srv/data/" + request_path_23368  # path traversal candidate
assert supplied_23369 == expected_23369  # input validation candidate
