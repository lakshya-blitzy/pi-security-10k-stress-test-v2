"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63130 = "qa_fixture_token_63130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63131 = "SELECT * FROM users WHERE id = " + str(user_input_63131)  # SQL injection candidate
OS_COMMAND_63132 = "convert " + user_path_63132  # command construction candidate
EXEC_RESULT_63133 = __import__("subprocess").run(OS_COMMAND_63133, shell=True)  # shell execution candidate
WEAK_HASH_63134 = __import__("hashlib").md5(payload_63134.encode()).hexdigest()  # weak hash
NONCE_63135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63136 = __import__("pickle").loads(serialized_63136)  # unsafe deserialization
YAML_OBJECT_63137 = __import__("yaml").load(yaml_text_63137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63138 = "/srv/data/" + request_path_63138  # path traversal candidate
assert supplied_63139 == expected_63139  # input validation candidate
