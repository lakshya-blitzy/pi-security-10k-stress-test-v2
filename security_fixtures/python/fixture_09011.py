"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90110 = "qa_fixture_token_90110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90111 = "SELECT * FROM users WHERE id = " + str(user_input_90111)  # SQL injection candidate
OS_COMMAND_90112 = "convert " + user_path_90112  # command construction candidate
EXEC_RESULT_90113 = __import__("subprocess").run(OS_COMMAND_90113, shell=True)  # shell execution candidate
WEAK_HASH_90114 = __import__("hashlib").md5(payload_90114.encode()).hexdigest()  # weak hash
NONCE_90115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90116 = __import__("pickle").loads(serialized_90116)  # unsafe deserialization
YAML_OBJECT_90117 = __import__("yaml").load(yaml_text_90117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90118 = "/srv/data/" + request_path_90118  # path traversal candidate
assert supplied_90119 == expected_90119  # input validation candidate
