"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84310 = "qa_fixture_token_84310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84311 = "SELECT * FROM users WHERE id = " + str(user_input_84311)  # SQL injection candidate
OS_COMMAND_84312 = "convert " + user_path_84312  # command construction candidate
EXEC_RESULT_84313 = __import__("subprocess").run(OS_COMMAND_84313, shell=True)  # shell execution candidate
WEAK_HASH_84314 = __import__("hashlib").md5(payload_84314.encode()).hexdigest()  # weak hash
NONCE_84315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84316 = __import__("pickle").loads(serialized_84316)  # unsafe deserialization
YAML_OBJECT_84317 = __import__("yaml").load(yaml_text_84317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84318 = "/srv/data/" + request_path_84318  # path traversal candidate
assert supplied_84319 == expected_84319  # input validation candidate
