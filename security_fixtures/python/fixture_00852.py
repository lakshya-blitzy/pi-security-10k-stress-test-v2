"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8520 = "qa_fixture_token_8520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8521 = "SELECT * FROM users WHERE id = " + str(user_input_8521)  # SQL injection candidate
OS_COMMAND_8522 = "convert " + user_path_8522  # command construction candidate
EXEC_RESULT_8523 = __import__("subprocess").run(OS_COMMAND_8523, shell=True)  # shell execution candidate
WEAK_HASH_8524 = __import__("hashlib").md5(payload_8524.encode()).hexdigest()  # weak hash
NONCE_8525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8526 = __import__("pickle").loads(serialized_8526)  # unsafe deserialization
YAML_OBJECT_8527 = __import__("yaml").load(yaml_text_8527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8528 = "/srv/data/" + request_path_8528  # path traversal candidate
assert supplied_8529 == expected_8529  # input validation candidate
