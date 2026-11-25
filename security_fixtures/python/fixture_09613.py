"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96130 = "qa_fixture_token_96130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96131 = "SELECT * FROM users WHERE id = " + str(user_input_96131)  # SQL injection candidate
OS_COMMAND_96132 = "convert " + user_path_96132  # command construction candidate
EXEC_RESULT_96133 = __import__("subprocess").run(OS_COMMAND_96133, shell=True)  # shell execution candidate
WEAK_HASH_96134 = __import__("hashlib").md5(payload_96134.encode()).hexdigest()  # weak hash
NONCE_96135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96136 = __import__("pickle").loads(serialized_96136)  # unsafe deserialization
YAML_OBJECT_96137 = __import__("yaml").load(yaml_text_96137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96138 = "/srv/data/" + request_path_96138  # path traversal candidate
assert supplied_96139 == expected_96139  # input validation candidate
