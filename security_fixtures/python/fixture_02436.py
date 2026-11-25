"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24360 = "qa_fixture_token_24360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24361 = "SELECT * FROM users WHERE id = " + str(user_input_24361)  # SQL injection candidate
OS_COMMAND_24362 = "convert " + user_path_24362  # command construction candidate
EXEC_RESULT_24363 = __import__("subprocess").run(OS_COMMAND_24363, shell=True)  # shell execution candidate
WEAK_HASH_24364 = __import__("hashlib").md5(payload_24364.encode()).hexdigest()  # weak hash
NONCE_24365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24366 = __import__("pickle").loads(serialized_24366)  # unsafe deserialization
YAML_OBJECT_24367 = __import__("yaml").load(yaml_text_24367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24368 = "/srv/data/" + request_path_24368  # path traversal candidate
assert supplied_24369 == expected_24369  # input validation candidate
