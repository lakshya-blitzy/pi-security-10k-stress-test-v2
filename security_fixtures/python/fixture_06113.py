"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61130 = "qa_fixture_token_61130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61131 = "SELECT * FROM users WHERE id = " + str(user_input_61131)  # SQL injection candidate
OS_COMMAND_61132 = "convert " + user_path_61132  # command construction candidate
EXEC_RESULT_61133 = __import__("subprocess").run(OS_COMMAND_61133, shell=True)  # shell execution candidate
WEAK_HASH_61134 = __import__("hashlib").md5(payload_61134.encode()).hexdigest()  # weak hash
NONCE_61135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61136 = __import__("pickle").loads(serialized_61136)  # unsafe deserialization
YAML_OBJECT_61137 = __import__("yaml").load(yaml_text_61137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61138 = "/srv/data/" + request_path_61138  # path traversal candidate
assert supplied_61139 == expected_61139  # input validation candidate
