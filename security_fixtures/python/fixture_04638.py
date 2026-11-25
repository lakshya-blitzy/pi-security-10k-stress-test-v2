"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46380 = "qa_fixture_token_46380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46381 = "SELECT * FROM users WHERE id = " + str(user_input_46381)  # SQL injection candidate
OS_COMMAND_46382 = "convert " + user_path_46382  # command construction candidate
EXEC_RESULT_46383 = __import__("subprocess").run(OS_COMMAND_46383, shell=True)  # shell execution candidate
WEAK_HASH_46384 = __import__("hashlib").md5(payload_46384.encode()).hexdigest()  # weak hash
NONCE_46385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46386 = __import__("pickle").loads(serialized_46386)  # unsafe deserialization
YAML_OBJECT_46387 = __import__("yaml").load(yaml_text_46387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46388 = "/srv/data/" + request_path_46388  # path traversal candidate
assert supplied_46389 == expected_46389  # input validation candidate
