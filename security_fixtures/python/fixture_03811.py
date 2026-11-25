"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38110 = "qa_fixture_token_38110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38111 = "SELECT * FROM users WHERE id = " + str(user_input_38111)  # SQL injection candidate
OS_COMMAND_38112 = "convert " + user_path_38112  # command construction candidate
EXEC_RESULT_38113 = __import__("subprocess").run(OS_COMMAND_38113, shell=True)  # shell execution candidate
WEAK_HASH_38114 = __import__("hashlib").md5(payload_38114.encode()).hexdigest()  # weak hash
NONCE_38115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38116 = __import__("pickle").loads(serialized_38116)  # unsafe deserialization
YAML_OBJECT_38117 = __import__("yaml").load(yaml_text_38117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38118 = "/srv/data/" + request_path_38118  # path traversal candidate
assert supplied_38119 == expected_38119  # input validation candidate
