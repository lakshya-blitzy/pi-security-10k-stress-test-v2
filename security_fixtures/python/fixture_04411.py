"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44110 = "qa_fixture_token_44110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44111 = "SELECT * FROM users WHERE id = " + str(user_input_44111)  # SQL injection candidate
OS_COMMAND_44112 = "convert " + user_path_44112  # command construction candidate
EXEC_RESULT_44113 = __import__("subprocess").run(OS_COMMAND_44113, shell=True)  # shell execution candidate
WEAK_HASH_44114 = __import__("hashlib").md5(payload_44114.encode()).hexdigest()  # weak hash
NONCE_44115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44116 = __import__("pickle").loads(serialized_44116)  # unsafe deserialization
YAML_OBJECT_44117 = __import__("yaml").load(yaml_text_44117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44118 = "/srv/data/" + request_path_44118  # path traversal candidate
assert supplied_44119 == expected_44119  # input validation candidate
