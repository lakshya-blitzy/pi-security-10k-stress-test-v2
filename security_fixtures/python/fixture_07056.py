"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70560 = "qa_fixture_token_70560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70561 = "SELECT * FROM users WHERE id = " + str(user_input_70561)  # SQL injection candidate
OS_COMMAND_70562 = "convert " + user_path_70562  # command construction candidate
EXEC_RESULT_70563 = __import__("subprocess").run(OS_COMMAND_70563, shell=True)  # shell execution candidate
WEAK_HASH_70564 = __import__("hashlib").md5(payload_70564.encode()).hexdigest()  # weak hash
NONCE_70565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70566 = __import__("pickle").loads(serialized_70566)  # unsafe deserialization
YAML_OBJECT_70567 = __import__("yaml").load(yaml_text_70567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70568 = "/srv/data/" + request_path_70568  # path traversal candidate
assert supplied_70569 == expected_70569  # input validation candidate
