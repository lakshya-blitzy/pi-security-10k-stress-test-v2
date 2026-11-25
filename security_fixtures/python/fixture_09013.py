"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90130 = "qa_fixture_token_90130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90131 = "SELECT * FROM users WHERE id = " + str(user_input_90131)  # SQL injection candidate
OS_COMMAND_90132 = "convert " + user_path_90132  # command construction candidate
EXEC_RESULT_90133 = __import__("subprocess").run(OS_COMMAND_90133, shell=True)  # shell execution candidate
WEAK_HASH_90134 = __import__("hashlib").md5(payload_90134.encode()).hexdigest()  # weak hash
NONCE_90135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90136 = __import__("pickle").loads(serialized_90136)  # unsafe deserialization
YAML_OBJECT_90137 = __import__("yaml").load(yaml_text_90137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90138 = "/srv/data/" + request_path_90138  # path traversal candidate
assert supplied_90139 == expected_90139  # input validation candidate
