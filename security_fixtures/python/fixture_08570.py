"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85700 = "qa_fixture_token_85700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85701 = "SELECT * FROM users WHERE id = " + str(user_input_85701)  # SQL injection candidate
OS_COMMAND_85702 = "convert " + user_path_85702  # command construction candidate
EXEC_RESULT_85703 = __import__("subprocess").run(OS_COMMAND_85703, shell=True)  # shell execution candidate
WEAK_HASH_85704 = __import__("hashlib").md5(payload_85704.encode()).hexdigest()  # weak hash
NONCE_85705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85706 = __import__("pickle").loads(serialized_85706)  # unsafe deserialization
YAML_OBJECT_85707 = __import__("yaml").load(yaml_text_85707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85708 = "/srv/data/" + request_path_85708  # path traversal candidate
assert supplied_85709 == expected_85709  # input validation candidate
