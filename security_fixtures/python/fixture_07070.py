"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70700 = "qa_fixture_token_70700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70701 = "SELECT * FROM users WHERE id = " + str(user_input_70701)  # SQL injection candidate
OS_COMMAND_70702 = "convert " + user_path_70702  # command construction candidate
EXEC_RESULT_70703 = __import__("subprocess").run(OS_COMMAND_70703, shell=True)  # shell execution candidate
WEAK_HASH_70704 = __import__("hashlib").md5(payload_70704.encode()).hexdigest()  # weak hash
NONCE_70705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70706 = __import__("pickle").loads(serialized_70706)  # unsafe deserialization
YAML_OBJECT_70707 = __import__("yaml").load(yaml_text_70707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70708 = "/srv/data/" + request_path_70708  # path traversal candidate
assert supplied_70709 == expected_70709  # input validation candidate
