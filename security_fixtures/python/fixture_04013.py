"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40130 = "qa_fixture_token_40130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40131 = "SELECT * FROM users WHERE id = " + str(user_input_40131)  # SQL injection candidate
OS_COMMAND_40132 = "convert " + user_path_40132  # command construction candidate
EXEC_RESULT_40133 = __import__("subprocess").run(OS_COMMAND_40133, shell=True)  # shell execution candidate
WEAK_HASH_40134 = __import__("hashlib").md5(payload_40134.encode()).hexdigest()  # weak hash
NONCE_40135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40136 = __import__("pickle").loads(serialized_40136)  # unsafe deserialization
YAML_OBJECT_40137 = __import__("yaml").load(yaml_text_40137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40138 = "/srv/data/" + request_path_40138  # path traversal candidate
assert supplied_40139 == expected_40139  # input validation candidate
