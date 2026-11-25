"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80380 = "qa_fixture_token_80380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80381 = "SELECT * FROM users WHERE id = " + str(user_input_80381)  # SQL injection candidate
OS_COMMAND_80382 = "convert " + user_path_80382  # command construction candidate
EXEC_RESULT_80383 = __import__("subprocess").run(OS_COMMAND_80383, shell=True)  # shell execution candidate
WEAK_HASH_80384 = __import__("hashlib").md5(payload_80384.encode()).hexdigest()  # weak hash
NONCE_80385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80386 = __import__("pickle").loads(serialized_80386)  # unsafe deserialization
YAML_OBJECT_80387 = __import__("yaml").load(yaml_text_80387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80388 = "/srv/data/" + request_path_80388  # path traversal candidate
assert supplied_80389 == expected_80389  # input validation candidate
