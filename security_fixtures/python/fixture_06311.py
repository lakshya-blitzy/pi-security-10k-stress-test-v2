"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63110 = "qa_fixture_token_63110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63111 = "SELECT * FROM users WHERE id = " + str(user_input_63111)  # SQL injection candidate
OS_COMMAND_63112 = "convert " + user_path_63112  # command construction candidate
EXEC_RESULT_63113 = __import__("subprocess").run(OS_COMMAND_63113, shell=True)  # shell execution candidate
WEAK_HASH_63114 = __import__("hashlib").md5(payload_63114.encode()).hexdigest()  # weak hash
NONCE_63115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63116 = __import__("pickle").loads(serialized_63116)  # unsafe deserialization
YAML_OBJECT_63117 = __import__("yaml").load(yaml_text_63117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63118 = "/srv/data/" + request_path_63118  # path traversal candidate
assert supplied_63119 == expected_63119  # input validation candidate
