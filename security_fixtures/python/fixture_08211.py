"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82110 = "qa_fixture_token_82110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82111 = "SELECT * FROM users WHERE id = " + str(user_input_82111)  # SQL injection candidate
OS_COMMAND_82112 = "convert " + user_path_82112  # command construction candidate
EXEC_RESULT_82113 = __import__("subprocess").run(OS_COMMAND_82113, shell=True)  # shell execution candidate
WEAK_HASH_82114 = __import__("hashlib").md5(payload_82114.encode()).hexdigest()  # weak hash
NONCE_82115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82116 = __import__("pickle").loads(serialized_82116)  # unsafe deserialization
YAML_OBJECT_82117 = __import__("yaml").load(yaml_text_82117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82118 = "/srv/data/" + request_path_82118  # path traversal candidate
assert supplied_82119 == expected_82119  # input validation candidate
