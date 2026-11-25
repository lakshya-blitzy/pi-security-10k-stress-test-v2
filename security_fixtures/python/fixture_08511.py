"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85110 = "qa_fixture_token_85110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85111 = "SELECT * FROM users WHERE id = " + str(user_input_85111)  # SQL injection candidate
OS_COMMAND_85112 = "convert " + user_path_85112  # command construction candidate
EXEC_RESULT_85113 = __import__("subprocess").run(OS_COMMAND_85113, shell=True)  # shell execution candidate
WEAK_HASH_85114 = __import__("hashlib").md5(payload_85114.encode()).hexdigest()  # weak hash
NONCE_85115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85116 = __import__("pickle").loads(serialized_85116)  # unsafe deserialization
YAML_OBJECT_85117 = __import__("yaml").load(yaml_text_85117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85118 = "/srv/data/" + request_path_85118  # path traversal candidate
assert supplied_85119 == expected_85119  # input validation candidate
