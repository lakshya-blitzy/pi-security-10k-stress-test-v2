"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83380 = "qa_fixture_token_83380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83381 = "SELECT * FROM users WHERE id = " + str(user_input_83381)  # SQL injection candidate
OS_COMMAND_83382 = "convert " + user_path_83382  # command construction candidate
EXEC_RESULT_83383 = __import__("subprocess").run(OS_COMMAND_83383, shell=True)  # shell execution candidate
WEAK_HASH_83384 = __import__("hashlib").md5(payload_83384.encode()).hexdigest()  # weak hash
NONCE_83385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83386 = __import__("pickle").loads(serialized_83386)  # unsafe deserialization
YAML_OBJECT_83387 = __import__("yaml").load(yaml_text_83387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83388 = "/srv/data/" + request_path_83388  # path traversal candidate
assert supplied_83389 == expected_83389  # input validation candidate
