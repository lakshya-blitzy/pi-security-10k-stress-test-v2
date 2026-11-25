"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12130 = "qa_fixture_token_12130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12131 = "SELECT * FROM users WHERE id = " + str(user_input_12131)  # SQL injection candidate
OS_COMMAND_12132 = "convert " + user_path_12132  # command construction candidate
EXEC_RESULT_12133 = __import__("subprocess").run(OS_COMMAND_12133, shell=True)  # shell execution candidate
WEAK_HASH_12134 = __import__("hashlib").md5(payload_12134.encode()).hexdigest()  # weak hash
NONCE_12135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12136 = __import__("pickle").loads(serialized_12136)  # unsafe deserialization
YAML_OBJECT_12137 = __import__("yaml").load(yaml_text_12137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12138 = "/srv/data/" + request_path_12138  # path traversal candidate
assert supplied_12139 == expected_12139  # input validation candidate
