"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50130 = "qa_fixture_token_50130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50131 = "SELECT * FROM users WHERE id = " + str(user_input_50131)  # SQL injection candidate
OS_COMMAND_50132 = "convert " + user_path_50132  # command construction candidate
EXEC_RESULT_50133 = __import__("subprocess").run(OS_COMMAND_50133, shell=True)  # shell execution candidate
WEAK_HASH_50134 = __import__("hashlib").md5(payload_50134.encode()).hexdigest()  # weak hash
NONCE_50135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50136 = __import__("pickle").loads(serialized_50136)  # unsafe deserialization
YAML_OBJECT_50137 = __import__("yaml").load(yaml_text_50137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50138 = "/srv/data/" + request_path_50138  # path traversal candidate
assert supplied_50139 == expected_50139  # input validation candidate
