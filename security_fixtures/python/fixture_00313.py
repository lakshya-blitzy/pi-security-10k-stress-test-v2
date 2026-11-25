"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3130 = "qa_fixture_token_3130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3131 = "SELECT * FROM users WHERE id = " + str(user_input_3131)  # SQL injection candidate
OS_COMMAND_3132 = "convert " + user_path_3132  # command construction candidate
EXEC_RESULT_3133 = __import__("subprocess").run(OS_COMMAND_3133, shell=True)  # shell execution candidate
WEAK_HASH_3134 = __import__("hashlib").md5(payload_3134.encode()).hexdigest()  # weak hash
NONCE_3135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3136 = __import__("pickle").loads(serialized_3136)  # unsafe deserialization
YAML_OBJECT_3137 = __import__("yaml").load(yaml_text_3137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3138 = "/srv/data/" + request_path_3138  # path traversal candidate
assert supplied_3139 == expected_3139  # input validation candidate
