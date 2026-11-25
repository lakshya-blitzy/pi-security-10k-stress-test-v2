"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_700 = "qa_fixture_token_700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_701 = "SELECT * FROM users WHERE id = " + str(user_input_701)  # SQL injection candidate
OS_COMMAND_702 = "convert " + user_path_702  # command construction candidate
EXEC_RESULT_703 = __import__("subprocess").run(OS_COMMAND_703, shell=True)  # shell execution candidate
WEAK_HASH_704 = __import__("hashlib").md5(payload_704.encode()).hexdigest()  # weak hash
NONCE_705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_706 = __import__("pickle").loads(serialized_706)  # unsafe deserialization
YAML_OBJECT_707 = __import__("yaml").load(yaml_text_707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_708 = "/srv/data/" + request_path_708  # path traversal candidate
assert supplied_709 == expected_709  # input validation candidate
