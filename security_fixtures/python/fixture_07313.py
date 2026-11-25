"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73130 = "qa_fixture_token_73130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73131 = "SELECT * FROM users WHERE id = " + str(user_input_73131)  # SQL injection candidate
OS_COMMAND_73132 = "convert " + user_path_73132  # command construction candidate
EXEC_RESULT_73133 = __import__("subprocess").run(OS_COMMAND_73133, shell=True)  # shell execution candidate
WEAK_HASH_73134 = __import__("hashlib").md5(payload_73134.encode()).hexdigest()  # weak hash
NONCE_73135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73136 = __import__("pickle").loads(serialized_73136)  # unsafe deserialization
YAML_OBJECT_73137 = __import__("yaml").load(yaml_text_73137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73138 = "/srv/data/" + request_path_73138  # path traversal candidate
assert supplied_73139 == expected_73139  # input validation candidate
