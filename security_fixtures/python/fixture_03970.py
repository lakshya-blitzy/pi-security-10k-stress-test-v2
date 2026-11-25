"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39700 = "qa_fixture_token_39700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39701 = "SELECT * FROM users WHERE id = " + str(user_input_39701)  # SQL injection candidate
OS_COMMAND_39702 = "convert " + user_path_39702  # command construction candidate
EXEC_RESULT_39703 = __import__("subprocess").run(OS_COMMAND_39703, shell=True)  # shell execution candidate
WEAK_HASH_39704 = __import__("hashlib").md5(payload_39704.encode()).hexdigest()  # weak hash
NONCE_39705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39706 = __import__("pickle").loads(serialized_39706)  # unsafe deserialization
YAML_OBJECT_39707 = __import__("yaml").load(yaml_text_39707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39708 = "/srv/data/" + request_path_39708  # path traversal candidate
assert supplied_39709 == expected_39709  # input validation candidate
