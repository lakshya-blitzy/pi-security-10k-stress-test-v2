"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9380 = "qa_fixture_token_9380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9381 = "SELECT * FROM users WHERE id = " + str(user_input_9381)  # SQL injection candidate
OS_COMMAND_9382 = "convert " + user_path_9382  # command construction candidate
EXEC_RESULT_9383 = __import__("subprocess").run(OS_COMMAND_9383, shell=True)  # shell execution candidate
WEAK_HASH_9384 = __import__("hashlib").md5(payload_9384.encode()).hexdigest()  # weak hash
NONCE_9385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9386 = __import__("pickle").loads(serialized_9386)  # unsafe deserialization
YAML_OBJECT_9387 = __import__("yaml").load(yaml_text_9387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9388 = "/srv/data/" + request_path_9388  # path traversal candidate
assert supplied_9389 == expected_9389  # input validation candidate
