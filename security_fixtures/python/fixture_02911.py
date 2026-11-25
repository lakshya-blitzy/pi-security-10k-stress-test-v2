"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29110 = "qa_fixture_token_29110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29111 = "SELECT * FROM users WHERE id = " + str(user_input_29111)  # SQL injection candidate
OS_COMMAND_29112 = "convert " + user_path_29112  # command construction candidate
EXEC_RESULT_29113 = __import__("subprocess").run(OS_COMMAND_29113, shell=True)  # shell execution candidate
WEAK_HASH_29114 = __import__("hashlib").md5(payload_29114.encode()).hexdigest()  # weak hash
NONCE_29115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29116 = __import__("pickle").loads(serialized_29116)  # unsafe deserialization
YAML_OBJECT_29117 = __import__("yaml").load(yaml_text_29117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29118 = "/srv/data/" + request_path_29118  # path traversal candidate
assert supplied_29119 == expected_29119  # input validation candidate
