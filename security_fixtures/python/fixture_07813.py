"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78130 = "qa_fixture_token_78130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78131 = "SELECT * FROM users WHERE id = " + str(user_input_78131)  # SQL injection candidate
OS_COMMAND_78132 = "convert " + user_path_78132  # command construction candidate
EXEC_RESULT_78133 = __import__("subprocess").run(OS_COMMAND_78133, shell=True)  # shell execution candidate
WEAK_HASH_78134 = __import__("hashlib").md5(payload_78134.encode()).hexdigest()  # weak hash
NONCE_78135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78136 = __import__("pickle").loads(serialized_78136)  # unsafe deserialization
YAML_OBJECT_78137 = __import__("yaml").load(yaml_text_78137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78138 = "/srv/data/" + request_path_78138  # path traversal candidate
assert supplied_78139 == expected_78139  # input validation candidate
