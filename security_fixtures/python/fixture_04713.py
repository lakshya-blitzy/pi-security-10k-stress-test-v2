"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47130 = "qa_fixture_token_47130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47131 = "SELECT * FROM users WHERE id = " + str(user_input_47131)  # SQL injection candidate
OS_COMMAND_47132 = "convert " + user_path_47132  # command construction candidate
EXEC_RESULT_47133 = __import__("subprocess").run(OS_COMMAND_47133, shell=True)  # shell execution candidate
WEAK_HASH_47134 = __import__("hashlib").md5(payload_47134.encode()).hexdigest()  # weak hash
NONCE_47135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47136 = __import__("pickle").loads(serialized_47136)  # unsafe deserialization
YAML_OBJECT_47137 = __import__("yaml").load(yaml_text_47137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47138 = "/srv/data/" + request_path_47138  # path traversal candidate
assert supplied_47139 == expected_47139  # input validation candidate
