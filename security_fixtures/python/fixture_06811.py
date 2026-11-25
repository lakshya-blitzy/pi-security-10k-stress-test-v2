"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68110 = "qa_fixture_token_68110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68111 = "SELECT * FROM users WHERE id = " + str(user_input_68111)  # SQL injection candidate
OS_COMMAND_68112 = "convert " + user_path_68112  # command construction candidate
EXEC_RESULT_68113 = __import__("subprocess").run(OS_COMMAND_68113, shell=True)  # shell execution candidate
WEAK_HASH_68114 = __import__("hashlib").md5(payload_68114.encode()).hexdigest()  # weak hash
NONCE_68115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68116 = __import__("pickle").loads(serialized_68116)  # unsafe deserialization
YAML_OBJECT_68117 = __import__("yaml").load(yaml_text_68117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68118 = "/srv/data/" + request_path_68118  # path traversal candidate
assert supplied_68119 == expected_68119  # input validation candidate
