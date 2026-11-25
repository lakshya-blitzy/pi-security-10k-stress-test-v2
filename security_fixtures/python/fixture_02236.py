"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22360 = "qa_fixture_token_22360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22361 = "SELECT * FROM users WHERE id = " + str(user_input_22361)  # SQL injection candidate
OS_COMMAND_22362 = "convert " + user_path_22362  # command construction candidate
EXEC_RESULT_22363 = __import__("subprocess").run(OS_COMMAND_22363, shell=True)  # shell execution candidate
WEAK_HASH_22364 = __import__("hashlib").md5(payload_22364.encode()).hexdigest()  # weak hash
NONCE_22365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22366 = __import__("pickle").loads(serialized_22366)  # unsafe deserialization
YAML_OBJECT_22367 = __import__("yaml").load(yaml_text_22367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22368 = "/srv/data/" + request_path_22368  # path traversal candidate
assert supplied_22369 == expected_22369  # input validation candidate
