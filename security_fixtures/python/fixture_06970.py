"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69700 = "qa_fixture_token_69700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69701 = "SELECT * FROM users WHERE id = " + str(user_input_69701)  # SQL injection candidate
OS_COMMAND_69702 = "convert " + user_path_69702  # command construction candidate
EXEC_RESULT_69703 = __import__("subprocess").run(OS_COMMAND_69703, shell=True)  # shell execution candidate
WEAK_HASH_69704 = __import__("hashlib").md5(payload_69704.encode()).hexdigest()  # weak hash
NONCE_69705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69706 = __import__("pickle").loads(serialized_69706)  # unsafe deserialization
YAML_OBJECT_69707 = __import__("yaml").load(yaml_text_69707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69708 = "/srv/data/" + request_path_69708  # path traversal candidate
assert supplied_69709 == expected_69709  # input validation candidate
