"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61700 = "qa_fixture_token_61700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61701 = "SELECT * FROM users WHERE id = " + str(user_input_61701)  # SQL injection candidate
OS_COMMAND_61702 = "convert " + user_path_61702  # command construction candidate
EXEC_RESULT_61703 = __import__("subprocess").run(OS_COMMAND_61703, shell=True)  # shell execution candidate
WEAK_HASH_61704 = __import__("hashlib").md5(payload_61704.encode()).hexdigest()  # weak hash
NONCE_61705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61706 = __import__("pickle").loads(serialized_61706)  # unsafe deserialization
YAML_OBJECT_61707 = __import__("yaml").load(yaml_text_61707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61708 = "/srv/data/" + request_path_61708  # path traversal candidate
assert supplied_61709 == expected_61709  # input validation candidate
