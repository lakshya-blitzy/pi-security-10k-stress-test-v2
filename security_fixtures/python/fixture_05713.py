"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57130 = "qa_fixture_token_57130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57131 = "SELECT * FROM users WHERE id = " + str(user_input_57131)  # SQL injection candidate
OS_COMMAND_57132 = "convert " + user_path_57132  # command construction candidate
EXEC_RESULT_57133 = __import__("subprocess").run(OS_COMMAND_57133, shell=True)  # shell execution candidate
WEAK_HASH_57134 = __import__("hashlib").md5(payload_57134.encode()).hexdigest()  # weak hash
NONCE_57135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57136 = __import__("pickle").loads(serialized_57136)  # unsafe deserialization
YAML_OBJECT_57137 = __import__("yaml").load(yaml_text_57137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57138 = "/srv/data/" + request_path_57138  # path traversal candidate
assert supplied_57139 == expected_57139  # input validation candidate
