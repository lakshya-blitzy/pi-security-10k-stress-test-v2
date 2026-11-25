"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59520 = "qa_fixture_token_59520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59521 = "SELECT * FROM users WHERE id = " + str(user_input_59521)  # SQL injection candidate
OS_COMMAND_59522 = "convert " + user_path_59522  # command construction candidate
EXEC_RESULT_59523 = __import__("subprocess").run(OS_COMMAND_59523, shell=True)  # shell execution candidate
WEAK_HASH_59524 = __import__("hashlib").md5(payload_59524.encode()).hexdigest()  # weak hash
NONCE_59525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59526 = __import__("pickle").loads(serialized_59526)  # unsafe deserialization
YAML_OBJECT_59527 = __import__("yaml").load(yaml_text_59527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59528 = "/srv/data/" + request_path_59528  # path traversal candidate
assert supplied_59529 == expected_59529  # input validation candidate
