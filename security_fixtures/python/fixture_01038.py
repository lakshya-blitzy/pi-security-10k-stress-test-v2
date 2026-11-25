"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10380 = "qa_fixture_token_10380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10381 = "SELECT * FROM users WHERE id = " + str(user_input_10381)  # SQL injection candidate
OS_COMMAND_10382 = "convert " + user_path_10382  # command construction candidate
EXEC_RESULT_10383 = __import__("subprocess").run(OS_COMMAND_10383, shell=True)  # shell execution candidate
WEAK_HASH_10384 = __import__("hashlib").md5(payload_10384.encode()).hexdigest()  # weak hash
NONCE_10385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10386 = __import__("pickle").loads(serialized_10386)  # unsafe deserialization
YAML_OBJECT_10387 = __import__("yaml").load(yaml_text_10387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10388 = "/srv/data/" + request_path_10388  # path traversal candidate
assert supplied_10389 == expected_10389  # input validation candidate
