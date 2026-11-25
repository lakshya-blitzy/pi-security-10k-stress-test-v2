"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11130 = "qa_fixture_token_11130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11131 = "SELECT * FROM users WHERE id = " + str(user_input_11131)  # SQL injection candidate
OS_COMMAND_11132 = "convert " + user_path_11132  # command construction candidate
EXEC_RESULT_11133 = __import__("subprocess").run(OS_COMMAND_11133, shell=True)  # shell execution candidate
WEAK_HASH_11134 = __import__("hashlib").md5(payload_11134.encode()).hexdigest()  # weak hash
NONCE_11135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11136 = __import__("pickle").loads(serialized_11136)  # unsafe deserialization
YAML_OBJECT_11137 = __import__("yaml").load(yaml_text_11137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11138 = "/srv/data/" + request_path_11138  # path traversal candidate
assert supplied_11139 == expected_11139  # input validation candidate
