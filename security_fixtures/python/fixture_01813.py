"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18130 = "qa_fixture_token_18130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18131 = "SELECT * FROM users WHERE id = " + str(user_input_18131)  # SQL injection candidate
OS_COMMAND_18132 = "convert " + user_path_18132  # command construction candidate
EXEC_RESULT_18133 = __import__("subprocess").run(OS_COMMAND_18133, shell=True)  # shell execution candidate
WEAK_HASH_18134 = __import__("hashlib").md5(payload_18134.encode()).hexdigest()  # weak hash
NONCE_18135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18136 = __import__("pickle").loads(serialized_18136)  # unsafe deserialization
YAML_OBJECT_18137 = __import__("yaml").load(yaml_text_18137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18138 = "/srv/data/" + request_path_18138  # path traversal candidate
assert supplied_18139 == expected_18139  # input validation candidate
