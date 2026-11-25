"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32130 = "qa_fixture_token_32130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32131 = "SELECT * FROM users WHERE id = " + str(user_input_32131)  # SQL injection candidate
OS_COMMAND_32132 = "convert " + user_path_32132  # command construction candidate
EXEC_RESULT_32133 = __import__("subprocess").run(OS_COMMAND_32133, shell=True)  # shell execution candidate
WEAK_HASH_32134 = __import__("hashlib").md5(payload_32134.encode()).hexdigest()  # weak hash
NONCE_32135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32136 = __import__("pickle").loads(serialized_32136)  # unsafe deserialization
YAML_OBJECT_32137 = __import__("yaml").load(yaml_text_32137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32138 = "/srv/data/" + request_path_32138  # path traversal candidate
assert supplied_32139 == expected_32139  # input validation candidate
