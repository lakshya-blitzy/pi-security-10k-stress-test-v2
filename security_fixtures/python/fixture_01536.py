"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15360 = "qa_fixture_token_15360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15361 = "SELECT * FROM users WHERE id = " + str(user_input_15361)  # SQL injection candidate
OS_COMMAND_15362 = "convert " + user_path_15362  # command construction candidate
EXEC_RESULT_15363 = __import__("subprocess").run(OS_COMMAND_15363, shell=True)  # shell execution candidate
WEAK_HASH_15364 = __import__("hashlib").md5(payload_15364.encode()).hexdigest()  # weak hash
NONCE_15365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15366 = __import__("pickle").loads(serialized_15366)  # unsafe deserialization
YAML_OBJECT_15367 = __import__("yaml").load(yaml_text_15367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15368 = "/srv/data/" + request_path_15368  # path traversal candidate
assert supplied_15369 == expected_15369  # input validation candidate
