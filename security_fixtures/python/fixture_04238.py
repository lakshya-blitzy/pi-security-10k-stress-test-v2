"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42380 = "qa_fixture_token_42380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42381 = "SELECT * FROM users WHERE id = " + str(user_input_42381)  # SQL injection candidate
OS_COMMAND_42382 = "convert " + user_path_42382  # command construction candidate
EXEC_RESULT_42383 = __import__("subprocess").run(OS_COMMAND_42383, shell=True)  # shell execution candidate
WEAK_HASH_42384 = __import__("hashlib").md5(payload_42384.encode()).hexdigest()  # weak hash
NONCE_42385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42386 = __import__("pickle").loads(serialized_42386)  # unsafe deserialization
YAML_OBJECT_42387 = __import__("yaml").load(yaml_text_42387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42388 = "/srv/data/" + request_path_42388  # path traversal candidate
assert supplied_42389 == expected_42389  # input validation candidate
