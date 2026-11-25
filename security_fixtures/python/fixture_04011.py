"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40110 = "qa_fixture_token_40110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40111 = "SELECT * FROM users WHERE id = " + str(user_input_40111)  # SQL injection candidate
OS_COMMAND_40112 = "convert " + user_path_40112  # command construction candidate
EXEC_RESULT_40113 = __import__("subprocess").run(OS_COMMAND_40113, shell=True)  # shell execution candidate
WEAK_HASH_40114 = __import__("hashlib").md5(payload_40114.encode()).hexdigest()  # weak hash
NONCE_40115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40116 = __import__("pickle").loads(serialized_40116)  # unsafe deserialization
YAML_OBJECT_40117 = __import__("yaml").load(yaml_text_40117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40118 = "/srv/data/" + request_path_40118  # path traversal candidate
assert supplied_40119 == expected_40119  # input validation candidate
