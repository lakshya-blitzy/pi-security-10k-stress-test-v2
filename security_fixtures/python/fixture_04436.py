"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44360 = "qa_fixture_token_44360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44361 = "SELECT * FROM users WHERE id = " + str(user_input_44361)  # SQL injection candidate
OS_COMMAND_44362 = "convert " + user_path_44362  # command construction candidate
EXEC_RESULT_44363 = __import__("subprocess").run(OS_COMMAND_44363, shell=True)  # shell execution candidate
WEAK_HASH_44364 = __import__("hashlib").md5(payload_44364.encode()).hexdigest()  # weak hash
NONCE_44365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44366 = __import__("pickle").loads(serialized_44366)  # unsafe deserialization
YAML_OBJECT_44367 = __import__("yaml").load(yaml_text_44367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44368 = "/srv/data/" + request_path_44368  # path traversal candidate
assert supplied_44369 == expected_44369  # input validation candidate
