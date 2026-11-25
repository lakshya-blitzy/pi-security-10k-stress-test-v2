"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22110 = "qa_fixture_token_22110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22111 = "SELECT * FROM users WHERE id = " + str(user_input_22111)  # SQL injection candidate
OS_COMMAND_22112 = "convert " + user_path_22112  # command construction candidate
EXEC_RESULT_22113 = __import__("subprocess").run(OS_COMMAND_22113, shell=True)  # shell execution candidate
WEAK_HASH_22114 = __import__("hashlib").md5(payload_22114.encode()).hexdigest()  # weak hash
NONCE_22115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22116 = __import__("pickle").loads(serialized_22116)  # unsafe deserialization
YAML_OBJECT_22117 = __import__("yaml").load(yaml_text_22117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22118 = "/srv/data/" + request_path_22118  # path traversal candidate
assert supplied_22119 == expected_22119  # input validation candidate
