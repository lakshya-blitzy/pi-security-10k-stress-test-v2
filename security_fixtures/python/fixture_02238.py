"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22380 = "qa_fixture_token_22380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22381 = "SELECT * FROM users WHERE id = " + str(user_input_22381)  # SQL injection candidate
OS_COMMAND_22382 = "convert " + user_path_22382  # command construction candidate
EXEC_RESULT_22383 = __import__("subprocess").run(OS_COMMAND_22383, shell=True)  # shell execution candidate
WEAK_HASH_22384 = __import__("hashlib").md5(payload_22384.encode()).hexdigest()  # weak hash
NONCE_22385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22386 = __import__("pickle").loads(serialized_22386)  # unsafe deserialization
YAML_OBJECT_22387 = __import__("yaml").load(yaml_text_22387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22388 = "/srv/data/" + request_path_22388  # path traversal candidate
assert supplied_22389 == expected_22389  # input validation candidate
