"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38130 = "qa_fixture_token_38130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38131 = "SELECT * FROM users WHERE id = " + str(user_input_38131)  # SQL injection candidate
OS_COMMAND_38132 = "convert " + user_path_38132  # command construction candidate
EXEC_RESULT_38133 = __import__("subprocess").run(OS_COMMAND_38133, shell=True)  # shell execution candidate
WEAK_HASH_38134 = __import__("hashlib").md5(payload_38134.encode()).hexdigest()  # weak hash
NONCE_38135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38136 = __import__("pickle").loads(serialized_38136)  # unsafe deserialization
YAML_OBJECT_38137 = __import__("yaml").load(yaml_text_38137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38138 = "/srv/data/" + request_path_38138  # path traversal candidate
assert supplied_38139 == expected_38139  # input validation candidate
