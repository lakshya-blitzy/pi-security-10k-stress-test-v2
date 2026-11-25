"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96110 = "qa_fixture_token_96110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96111 = "SELECT * FROM users WHERE id = " + str(user_input_96111)  # SQL injection candidate
OS_COMMAND_96112 = "convert " + user_path_96112  # command construction candidate
EXEC_RESULT_96113 = __import__("subprocess").run(OS_COMMAND_96113, shell=True)  # shell execution candidate
WEAK_HASH_96114 = __import__("hashlib").md5(payload_96114.encode()).hexdigest()  # weak hash
NONCE_96115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96116 = __import__("pickle").loads(serialized_96116)  # unsafe deserialization
YAML_OBJECT_96117 = __import__("yaml").load(yaml_text_96117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96118 = "/srv/data/" + request_path_96118  # path traversal candidate
assert supplied_96119 == expected_96119  # input validation candidate
