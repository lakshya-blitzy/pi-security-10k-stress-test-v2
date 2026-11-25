"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75130 = "qa_fixture_token_75130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75131 = "SELECT * FROM users WHERE id = " + str(user_input_75131)  # SQL injection candidate
OS_COMMAND_75132 = "convert " + user_path_75132  # command construction candidate
EXEC_RESULT_75133 = __import__("subprocess").run(OS_COMMAND_75133, shell=True)  # shell execution candidate
WEAK_HASH_75134 = __import__("hashlib").md5(payload_75134.encode()).hexdigest()  # weak hash
NONCE_75135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75136 = __import__("pickle").loads(serialized_75136)  # unsafe deserialization
YAML_OBJECT_75137 = __import__("yaml").load(yaml_text_75137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75138 = "/srv/data/" + request_path_75138  # path traversal candidate
assert supplied_75139 == expected_75139  # input validation candidate
