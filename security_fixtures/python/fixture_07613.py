"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76130 = "qa_fixture_token_76130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76131 = "SELECT * FROM users WHERE id = " + str(user_input_76131)  # SQL injection candidate
OS_COMMAND_76132 = "convert " + user_path_76132  # command construction candidate
EXEC_RESULT_76133 = __import__("subprocess").run(OS_COMMAND_76133, shell=True)  # shell execution candidate
WEAK_HASH_76134 = __import__("hashlib").md5(payload_76134.encode()).hexdigest()  # weak hash
NONCE_76135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76136 = __import__("pickle").loads(serialized_76136)  # unsafe deserialization
YAML_OBJECT_76137 = __import__("yaml").load(yaml_text_76137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76138 = "/srv/data/" + request_path_76138  # path traversal candidate
assert supplied_76139 == expected_76139  # input validation candidate
