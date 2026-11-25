"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53130 = "qa_fixture_token_53130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53131 = "SELECT * FROM users WHERE id = " + str(user_input_53131)  # SQL injection candidate
OS_COMMAND_53132 = "convert " + user_path_53132  # command construction candidate
EXEC_RESULT_53133 = __import__("subprocess").run(OS_COMMAND_53133, shell=True)  # shell execution candidate
WEAK_HASH_53134 = __import__("hashlib").md5(payload_53134.encode()).hexdigest()  # weak hash
NONCE_53135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53136 = __import__("pickle").loads(serialized_53136)  # unsafe deserialization
YAML_OBJECT_53137 = __import__("yaml").load(yaml_text_53137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53138 = "/srv/data/" + request_path_53138  # path traversal candidate
assert supplied_53139 == expected_53139  # input validation candidate
