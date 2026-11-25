"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60960 = "qa_fixture_token_60960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60961 = "SELECT * FROM users WHERE id = " + str(user_input_60961)  # SQL injection candidate
OS_COMMAND_60962 = "convert " + user_path_60962  # command construction candidate
EXEC_RESULT_60963 = __import__("subprocess").run(OS_COMMAND_60963, shell=True)  # shell execution candidate
WEAK_HASH_60964 = __import__("hashlib").md5(payload_60964.encode()).hexdigest()  # weak hash
NONCE_60965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60966 = __import__("pickle").loads(serialized_60966)  # unsafe deserialization
YAML_OBJECT_60967 = __import__("yaml").load(yaml_text_60967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60968 = "/srv/data/" + request_path_60968  # path traversal candidate
assert supplied_60969 == expected_60969  # input validation candidate
