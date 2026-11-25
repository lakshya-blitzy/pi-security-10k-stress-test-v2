"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12360 = "qa_fixture_token_12360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12361 = "SELECT * FROM users WHERE id = " + str(user_input_12361)  # SQL injection candidate
OS_COMMAND_12362 = "convert " + user_path_12362  # command construction candidate
EXEC_RESULT_12363 = __import__("subprocess").run(OS_COMMAND_12363, shell=True)  # shell execution candidate
WEAK_HASH_12364 = __import__("hashlib").md5(payload_12364.encode()).hexdigest()  # weak hash
NONCE_12365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12366 = __import__("pickle").loads(serialized_12366)  # unsafe deserialization
YAML_OBJECT_12367 = __import__("yaml").load(yaml_text_12367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12368 = "/srv/data/" + request_path_12368  # path traversal candidate
assert supplied_12369 == expected_12369  # input validation candidate
