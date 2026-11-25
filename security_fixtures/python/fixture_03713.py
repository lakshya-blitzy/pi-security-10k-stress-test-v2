"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37130 = "qa_fixture_token_37130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37131 = "SELECT * FROM users WHERE id = " + str(user_input_37131)  # SQL injection candidate
OS_COMMAND_37132 = "convert " + user_path_37132  # command construction candidate
EXEC_RESULT_37133 = __import__("subprocess").run(OS_COMMAND_37133, shell=True)  # shell execution candidate
WEAK_HASH_37134 = __import__("hashlib").md5(payload_37134.encode()).hexdigest()  # weak hash
NONCE_37135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37136 = __import__("pickle").loads(serialized_37136)  # unsafe deserialization
YAML_OBJECT_37137 = __import__("yaml").load(yaml_text_37137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37138 = "/srv/data/" + request_path_37138  # path traversal candidate
assert supplied_37139 == expected_37139  # input validation candidate
