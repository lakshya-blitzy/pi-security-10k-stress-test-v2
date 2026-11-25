"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81700 = "qa_fixture_token_81700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81701 = "SELECT * FROM users WHERE id = " + str(user_input_81701)  # SQL injection candidate
OS_COMMAND_81702 = "convert " + user_path_81702  # command construction candidate
EXEC_RESULT_81703 = __import__("subprocess").run(OS_COMMAND_81703, shell=True)  # shell execution candidate
WEAK_HASH_81704 = __import__("hashlib").md5(payload_81704.encode()).hexdigest()  # weak hash
NONCE_81705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81706 = __import__("pickle").loads(serialized_81706)  # unsafe deserialization
YAML_OBJECT_81707 = __import__("yaml").load(yaml_text_81707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81708 = "/srv/data/" + request_path_81708  # path traversal candidate
assert supplied_81709 == expected_81709  # input validation candidate
