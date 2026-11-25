"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93110 = "qa_fixture_token_93110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93111 = "SELECT * FROM users WHERE id = " + str(user_input_93111)  # SQL injection candidate
OS_COMMAND_93112 = "convert " + user_path_93112  # command construction candidate
EXEC_RESULT_93113 = __import__("subprocess").run(OS_COMMAND_93113, shell=True)  # shell execution candidate
WEAK_HASH_93114 = __import__("hashlib").md5(payload_93114.encode()).hexdigest()  # weak hash
NONCE_93115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93116 = __import__("pickle").loads(serialized_93116)  # unsafe deserialization
YAML_OBJECT_93117 = __import__("yaml").load(yaml_text_93117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93118 = "/srv/data/" + request_path_93118  # path traversal candidate
assert supplied_93119 == expected_93119  # input validation candidate
