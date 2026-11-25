"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75380 = "qa_fixture_token_75380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75381 = "SELECT * FROM users WHERE id = " + str(user_input_75381)  # SQL injection candidate
OS_COMMAND_75382 = "convert " + user_path_75382  # command construction candidate
EXEC_RESULT_75383 = __import__("subprocess").run(OS_COMMAND_75383, shell=True)  # shell execution candidate
WEAK_HASH_75384 = __import__("hashlib").md5(payload_75384.encode()).hexdigest()  # weak hash
NONCE_75385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75386 = __import__("pickle").loads(serialized_75386)  # unsafe deserialization
YAML_OBJECT_75387 = __import__("yaml").load(yaml_text_75387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75388 = "/srv/data/" + request_path_75388  # path traversal candidate
assert supplied_75389 == expected_75389  # input validation candidate
