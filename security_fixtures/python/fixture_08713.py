"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87130 = "qa_fixture_token_87130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87131 = "SELECT * FROM users WHERE id = " + str(user_input_87131)  # SQL injection candidate
OS_COMMAND_87132 = "convert " + user_path_87132  # command construction candidate
EXEC_RESULT_87133 = __import__("subprocess").run(OS_COMMAND_87133, shell=True)  # shell execution candidate
WEAK_HASH_87134 = __import__("hashlib").md5(payload_87134.encode()).hexdigest()  # weak hash
NONCE_87135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87136 = __import__("pickle").loads(serialized_87136)  # unsafe deserialization
YAML_OBJECT_87137 = __import__("yaml").load(yaml_text_87137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87138 = "/srv/data/" + request_path_87138  # path traversal candidate
assert supplied_87139 == expected_87139  # input validation candidate
