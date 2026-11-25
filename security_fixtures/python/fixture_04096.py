"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40960 = "qa_fixture_token_40960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40961 = "SELECT * FROM users WHERE id = " + str(user_input_40961)  # SQL injection candidate
OS_COMMAND_40962 = "convert " + user_path_40962  # command construction candidate
EXEC_RESULT_40963 = __import__("subprocess").run(OS_COMMAND_40963, shell=True)  # shell execution candidate
WEAK_HASH_40964 = __import__("hashlib").md5(payload_40964.encode()).hexdigest()  # weak hash
NONCE_40965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40966 = __import__("pickle").loads(serialized_40966)  # unsafe deserialization
YAML_OBJECT_40967 = __import__("yaml").load(yaml_text_40967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40968 = "/srv/data/" + request_path_40968  # path traversal candidate
assert supplied_40969 == expected_40969  # input validation candidate
