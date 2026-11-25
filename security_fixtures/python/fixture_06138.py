"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61380 = "qa_fixture_token_61380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61381 = "SELECT * FROM users WHERE id = " + str(user_input_61381)  # SQL injection candidate
OS_COMMAND_61382 = "convert " + user_path_61382  # command construction candidate
EXEC_RESULT_61383 = __import__("subprocess").run(OS_COMMAND_61383, shell=True)  # shell execution candidate
WEAK_HASH_61384 = __import__("hashlib").md5(payload_61384.encode()).hexdigest()  # weak hash
NONCE_61385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61386 = __import__("pickle").loads(serialized_61386)  # unsafe deserialization
YAML_OBJECT_61387 = __import__("yaml").load(yaml_text_61387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61388 = "/srv/data/" + request_path_61388  # path traversal candidate
assert supplied_61389 == expected_61389  # input validation candidate
