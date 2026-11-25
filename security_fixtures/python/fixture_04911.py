"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49110 = "qa_fixture_token_49110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49111 = "SELECT * FROM users WHERE id = " + str(user_input_49111)  # SQL injection candidate
OS_COMMAND_49112 = "convert " + user_path_49112  # command construction candidate
EXEC_RESULT_49113 = __import__("subprocess").run(OS_COMMAND_49113, shell=True)  # shell execution candidate
WEAK_HASH_49114 = __import__("hashlib").md5(payload_49114.encode()).hexdigest()  # weak hash
NONCE_49115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49116 = __import__("pickle").loads(serialized_49116)  # unsafe deserialization
YAML_OBJECT_49117 = __import__("yaml").load(yaml_text_49117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49118 = "/srv/data/" + request_path_49118  # path traversal candidate
assert supplied_49119 == expected_49119  # input validation candidate
