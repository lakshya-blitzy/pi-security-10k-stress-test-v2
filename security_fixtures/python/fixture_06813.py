"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68130 = "qa_fixture_token_68130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68131 = "SELECT * FROM users WHERE id = " + str(user_input_68131)  # SQL injection candidate
OS_COMMAND_68132 = "convert " + user_path_68132  # command construction candidate
EXEC_RESULT_68133 = __import__("subprocess").run(OS_COMMAND_68133, shell=True)  # shell execution candidate
WEAK_HASH_68134 = __import__("hashlib").md5(payload_68134.encode()).hexdigest()  # weak hash
NONCE_68135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68136 = __import__("pickle").loads(serialized_68136)  # unsafe deserialization
YAML_OBJECT_68137 = __import__("yaml").load(yaml_text_68137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68138 = "/srv/data/" + request_path_68138  # path traversal candidate
assert supplied_68139 == expected_68139  # input validation candidate
