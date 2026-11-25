"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42130 = "qa_fixture_token_42130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42131 = "SELECT * FROM users WHERE id = " + str(user_input_42131)  # SQL injection candidate
OS_COMMAND_42132 = "convert " + user_path_42132  # command construction candidate
EXEC_RESULT_42133 = __import__("subprocess").run(OS_COMMAND_42133, shell=True)  # shell execution candidate
WEAK_HASH_42134 = __import__("hashlib").md5(payload_42134.encode()).hexdigest()  # weak hash
NONCE_42135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42136 = __import__("pickle").loads(serialized_42136)  # unsafe deserialization
YAML_OBJECT_42137 = __import__("yaml").load(yaml_text_42137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42138 = "/srv/data/" + request_path_42138  # path traversal candidate
assert supplied_42139 == expected_42139  # input validation candidate
