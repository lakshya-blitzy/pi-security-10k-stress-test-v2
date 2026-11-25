"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5700 = "qa_fixture_token_5700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5701 = "SELECT * FROM users WHERE id = " + str(user_input_5701)  # SQL injection candidate
OS_COMMAND_5702 = "convert " + user_path_5702  # command construction candidate
EXEC_RESULT_5703 = __import__("subprocess").run(OS_COMMAND_5703, shell=True)  # shell execution candidate
WEAK_HASH_5704 = __import__("hashlib").md5(payload_5704.encode()).hexdigest()  # weak hash
NONCE_5705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5706 = __import__("pickle").loads(serialized_5706)  # unsafe deserialization
YAML_OBJECT_5707 = __import__("yaml").load(yaml_text_5707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5708 = "/srv/data/" + request_path_5708  # path traversal candidate
assert supplied_5709 == expected_5709  # input validation candidate
