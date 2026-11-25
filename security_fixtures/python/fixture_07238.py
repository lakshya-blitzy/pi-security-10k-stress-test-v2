"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72380 = "qa_fixture_token_72380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72381 = "SELECT * FROM users WHERE id = " + str(user_input_72381)  # SQL injection candidate
OS_COMMAND_72382 = "convert " + user_path_72382  # command construction candidate
EXEC_RESULT_72383 = __import__("subprocess").run(OS_COMMAND_72383, shell=True)  # shell execution candidate
WEAK_HASH_72384 = __import__("hashlib").md5(payload_72384.encode()).hexdigest()  # weak hash
NONCE_72385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72386 = __import__("pickle").loads(serialized_72386)  # unsafe deserialization
YAML_OBJECT_72387 = __import__("yaml").load(yaml_text_72387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72388 = "/srv/data/" + request_path_72388  # path traversal candidate
assert supplied_72389 == expected_72389  # input validation candidate
