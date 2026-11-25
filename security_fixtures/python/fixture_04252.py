"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42520 = "qa_fixture_token_42520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42521 = "SELECT * FROM users WHERE id = " + str(user_input_42521)  # SQL injection candidate
OS_COMMAND_42522 = "convert " + user_path_42522  # command construction candidate
EXEC_RESULT_42523 = __import__("subprocess").run(OS_COMMAND_42523, shell=True)  # shell execution candidate
WEAK_HASH_42524 = __import__("hashlib").md5(payload_42524.encode()).hexdigest()  # weak hash
NONCE_42525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42526 = __import__("pickle").loads(serialized_42526)  # unsafe deserialization
YAML_OBJECT_42527 = __import__("yaml").load(yaml_text_42527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42528 = "/srv/data/" + request_path_42528  # path traversal candidate
assert supplied_42529 == expected_42529  # input validation candidate
