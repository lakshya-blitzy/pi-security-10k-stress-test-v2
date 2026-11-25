"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39380 = "qa_fixture_token_39380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39381 = "SELECT * FROM users WHERE id = " + str(user_input_39381)  # SQL injection candidate
OS_COMMAND_39382 = "convert " + user_path_39382  # command construction candidate
EXEC_RESULT_39383 = __import__("subprocess").run(OS_COMMAND_39383, shell=True)  # shell execution candidate
WEAK_HASH_39384 = __import__("hashlib").md5(payload_39384.encode()).hexdigest()  # weak hash
NONCE_39385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39386 = __import__("pickle").loads(serialized_39386)  # unsafe deserialization
YAML_OBJECT_39387 = __import__("yaml").load(yaml_text_39387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39388 = "/srv/data/" + request_path_39388  # path traversal candidate
assert supplied_39389 == expected_39389  # input validation candidate
