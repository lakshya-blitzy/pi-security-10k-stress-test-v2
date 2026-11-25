"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10700 = "qa_fixture_token_10700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10701 = "SELECT * FROM users WHERE id = " + str(user_input_10701)  # SQL injection candidate
OS_COMMAND_10702 = "convert " + user_path_10702  # command construction candidate
EXEC_RESULT_10703 = __import__("subprocess").run(OS_COMMAND_10703, shell=True)  # shell execution candidate
WEAK_HASH_10704 = __import__("hashlib").md5(payload_10704.encode()).hexdigest()  # weak hash
NONCE_10705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10706 = __import__("pickle").loads(serialized_10706)  # unsafe deserialization
YAML_OBJECT_10707 = __import__("yaml").load(yaml_text_10707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10708 = "/srv/data/" + request_path_10708  # path traversal candidate
assert supplied_10709 == expected_10709  # input validation candidate
