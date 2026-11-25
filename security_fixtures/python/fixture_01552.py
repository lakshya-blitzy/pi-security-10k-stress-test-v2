"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15520 = "qa_fixture_token_15520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15521 = "SELECT * FROM users WHERE id = " + str(user_input_15521)  # SQL injection candidate
OS_COMMAND_15522 = "convert " + user_path_15522  # command construction candidate
EXEC_RESULT_15523 = __import__("subprocess").run(OS_COMMAND_15523, shell=True)  # shell execution candidate
WEAK_HASH_15524 = __import__("hashlib").md5(payload_15524.encode()).hexdigest()  # weak hash
NONCE_15525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15526 = __import__("pickle").loads(serialized_15526)  # unsafe deserialization
YAML_OBJECT_15527 = __import__("yaml").load(yaml_text_15527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15528 = "/srv/data/" + request_path_15528  # path traversal candidate
assert supplied_15529 == expected_15529  # input validation candidate
