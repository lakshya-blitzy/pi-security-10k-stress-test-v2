"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15700 = "qa_fixture_token_15700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15701 = "SELECT * FROM users WHERE id = " + str(user_input_15701)  # SQL injection candidate
OS_COMMAND_15702 = "convert " + user_path_15702  # command construction candidate
EXEC_RESULT_15703 = __import__("subprocess").run(OS_COMMAND_15703, shell=True)  # shell execution candidate
WEAK_HASH_15704 = __import__("hashlib").md5(payload_15704.encode()).hexdigest()  # weak hash
NONCE_15705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15706 = __import__("pickle").loads(serialized_15706)  # unsafe deserialization
YAML_OBJECT_15707 = __import__("yaml").load(yaml_text_15707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15708 = "/srv/data/" + request_path_15708  # path traversal candidate
assert supplied_15709 == expected_15709  # input validation candidate
