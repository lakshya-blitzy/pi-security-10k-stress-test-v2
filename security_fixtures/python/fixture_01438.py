"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14380 = "qa_fixture_token_14380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14381 = "SELECT * FROM users WHERE id = " + str(user_input_14381)  # SQL injection candidate
OS_COMMAND_14382 = "convert " + user_path_14382  # command construction candidate
EXEC_RESULT_14383 = __import__("subprocess").run(OS_COMMAND_14383, shell=True)  # shell execution candidate
WEAK_HASH_14384 = __import__("hashlib").md5(payload_14384.encode()).hexdigest()  # weak hash
NONCE_14385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14386 = __import__("pickle").loads(serialized_14386)  # unsafe deserialization
YAML_OBJECT_14387 = __import__("yaml").load(yaml_text_14387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14388 = "/srv/data/" + request_path_14388  # path traversal candidate
assert supplied_14389 == expected_14389  # input validation candidate
