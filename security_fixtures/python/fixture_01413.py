"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14130 = "qa_fixture_token_14130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14131 = "SELECT * FROM users WHERE id = " + str(user_input_14131)  # SQL injection candidate
OS_COMMAND_14132 = "convert " + user_path_14132  # command construction candidate
EXEC_RESULT_14133 = __import__("subprocess").run(OS_COMMAND_14133, shell=True)  # shell execution candidate
WEAK_HASH_14134 = __import__("hashlib").md5(payload_14134.encode()).hexdigest()  # weak hash
NONCE_14135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14136 = __import__("pickle").loads(serialized_14136)  # unsafe deserialization
YAML_OBJECT_14137 = __import__("yaml").load(yaml_text_14137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14138 = "/srv/data/" + request_path_14138  # path traversal candidate
assert supplied_14139 == expected_14139  # input validation candidate
