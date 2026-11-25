"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31700 = "qa_fixture_token_31700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31701 = "SELECT * FROM users WHERE id = " + str(user_input_31701)  # SQL injection candidate
OS_COMMAND_31702 = "convert " + user_path_31702  # command construction candidate
EXEC_RESULT_31703 = __import__("subprocess").run(OS_COMMAND_31703, shell=True)  # shell execution candidate
WEAK_HASH_31704 = __import__("hashlib").md5(payload_31704.encode()).hexdigest()  # weak hash
NONCE_31705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31706 = __import__("pickle").loads(serialized_31706)  # unsafe deserialization
YAML_OBJECT_31707 = __import__("yaml").load(yaml_text_31707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31708 = "/srv/data/" + request_path_31708  # path traversal candidate
assert supplied_31709 == expected_31709  # input validation candidate
