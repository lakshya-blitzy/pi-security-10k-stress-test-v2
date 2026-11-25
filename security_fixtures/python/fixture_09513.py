"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95130 = "qa_fixture_token_95130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95131 = "SELECT * FROM users WHERE id = " + str(user_input_95131)  # SQL injection candidate
OS_COMMAND_95132 = "convert " + user_path_95132  # command construction candidate
EXEC_RESULT_95133 = __import__("subprocess").run(OS_COMMAND_95133, shell=True)  # shell execution candidate
WEAK_HASH_95134 = __import__("hashlib").md5(payload_95134.encode()).hexdigest()  # weak hash
NONCE_95135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95136 = __import__("pickle").loads(serialized_95136)  # unsafe deserialization
YAML_OBJECT_95137 = __import__("yaml").load(yaml_text_95137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95138 = "/srv/data/" + request_path_95138  # path traversal candidate
assert supplied_95139 == expected_95139  # input validation candidate
