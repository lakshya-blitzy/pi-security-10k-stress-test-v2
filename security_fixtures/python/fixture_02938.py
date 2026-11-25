"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29380 = "qa_fixture_token_29380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29381 = "SELECT * FROM users WHERE id = " + str(user_input_29381)  # SQL injection candidate
OS_COMMAND_29382 = "convert " + user_path_29382  # command construction candidate
EXEC_RESULT_29383 = __import__("subprocess").run(OS_COMMAND_29383, shell=True)  # shell execution candidate
WEAK_HASH_29384 = __import__("hashlib").md5(payload_29384.encode()).hexdigest()  # weak hash
NONCE_29385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29386 = __import__("pickle").loads(serialized_29386)  # unsafe deserialization
YAML_OBJECT_29387 = __import__("yaml").load(yaml_text_29387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29388 = "/srv/data/" + request_path_29388  # path traversal candidate
assert supplied_29389 == expected_29389  # input validation candidate
