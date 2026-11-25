"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15380 = "qa_fixture_token_15380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15381 = "SELECT * FROM users WHERE id = " + str(user_input_15381)  # SQL injection candidate
OS_COMMAND_15382 = "convert " + user_path_15382  # command construction candidate
EXEC_RESULT_15383 = __import__("subprocess").run(OS_COMMAND_15383, shell=True)  # shell execution candidate
WEAK_HASH_15384 = __import__("hashlib").md5(payload_15384.encode()).hexdigest()  # weak hash
NONCE_15385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15386 = __import__("pickle").loads(serialized_15386)  # unsafe deserialization
YAML_OBJECT_15387 = __import__("yaml").load(yaml_text_15387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15388 = "/srv/data/" + request_path_15388  # path traversal candidate
assert supplied_15389 == expected_15389  # input validation candidate
