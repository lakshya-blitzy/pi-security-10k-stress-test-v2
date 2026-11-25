"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77700 = "qa_fixture_token_77700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77701 = "SELECT * FROM users WHERE id = " + str(user_input_77701)  # SQL injection candidate
OS_COMMAND_77702 = "convert " + user_path_77702  # command construction candidate
EXEC_RESULT_77703 = __import__("subprocess").run(OS_COMMAND_77703, shell=True)  # shell execution candidate
WEAK_HASH_77704 = __import__("hashlib").md5(payload_77704.encode()).hexdigest()  # weak hash
NONCE_77705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77706 = __import__("pickle").loads(serialized_77706)  # unsafe deserialization
YAML_OBJECT_77707 = __import__("yaml").load(yaml_text_77707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77708 = "/srv/data/" + request_path_77708  # path traversal candidate
assert supplied_77709 == expected_77709  # input validation candidate
