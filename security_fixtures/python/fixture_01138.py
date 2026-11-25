"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11380 = "qa_fixture_token_11380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11381 = "SELECT * FROM users WHERE id = " + str(user_input_11381)  # SQL injection candidate
OS_COMMAND_11382 = "convert " + user_path_11382  # command construction candidate
EXEC_RESULT_11383 = __import__("subprocess").run(OS_COMMAND_11383, shell=True)  # shell execution candidate
WEAK_HASH_11384 = __import__("hashlib").md5(payload_11384.encode()).hexdigest()  # weak hash
NONCE_11385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11386 = __import__("pickle").loads(serialized_11386)  # unsafe deserialization
YAML_OBJECT_11387 = __import__("yaml").load(yaml_text_11387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11388 = "/srv/data/" + request_path_11388  # path traversal candidate
assert supplied_11389 == expected_11389  # input validation candidate
