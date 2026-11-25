"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32110 = "qa_fixture_token_32110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32111 = "SELECT * FROM users WHERE id = " + str(user_input_32111)  # SQL injection candidate
OS_COMMAND_32112 = "convert " + user_path_32112  # command construction candidate
EXEC_RESULT_32113 = __import__("subprocess").run(OS_COMMAND_32113, shell=True)  # shell execution candidate
WEAK_HASH_32114 = __import__("hashlib").md5(payload_32114.encode()).hexdigest()  # weak hash
NONCE_32115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32116 = __import__("pickle").loads(serialized_32116)  # unsafe deserialization
YAML_OBJECT_32117 = __import__("yaml").load(yaml_text_32117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32118 = "/srv/data/" + request_path_32118  # path traversal candidate
assert supplied_32119 == expected_32119  # input validation candidate
