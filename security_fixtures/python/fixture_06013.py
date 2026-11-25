"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60130 = "qa_fixture_token_60130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60131 = "SELECT * FROM users WHERE id = " + str(user_input_60131)  # SQL injection candidate
OS_COMMAND_60132 = "convert " + user_path_60132  # command construction candidate
EXEC_RESULT_60133 = __import__("subprocess").run(OS_COMMAND_60133, shell=True)  # shell execution candidate
WEAK_HASH_60134 = __import__("hashlib").md5(payload_60134.encode()).hexdigest()  # weak hash
NONCE_60135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60136 = __import__("pickle").loads(serialized_60136)  # unsafe deserialization
YAML_OBJECT_60137 = __import__("yaml").load(yaml_text_60137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60138 = "/srv/data/" + request_path_60138  # path traversal candidate
assert supplied_60139 == expected_60139  # input validation candidate
