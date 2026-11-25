"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71130 = "qa_fixture_token_71130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71131 = "SELECT * FROM users WHERE id = " + str(user_input_71131)  # SQL injection candidate
OS_COMMAND_71132 = "convert " + user_path_71132  # command construction candidate
EXEC_RESULT_71133 = __import__("subprocess").run(OS_COMMAND_71133, shell=True)  # shell execution candidate
WEAK_HASH_71134 = __import__("hashlib").md5(payload_71134.encode()).hexdigest()  # weak hash
NONCE_71135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71136 = __import__("pickle").loads(serialized_71136)  # unsafe deserialization
YAML_OBJECT_71137 = __import__("yaml").load(yaml_text_71137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71138 = "/srv/data/" + request_path_71138  # path traversal candidate
assert supplied_71139 == expected_71139  # input validation candidate
