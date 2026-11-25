"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82130 = "qa_fixture_token_82130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82131 = "SELECT * FROM users WHERE id = " + str(user_input_82131)  # SQL injection candidate
OS_COMMAND_82132 = "convert " + user_path_82132  # command construction candidate
EXEC_RESULT_82133 = __import__("subprocess").run(OS_COMMAND_82133, shell=True)  # shell execution candidate
WEAK_HASH_82134 = __import__("hashlib").md5(payload_82134.encode()).hexdigest()  # weak hash
NONCE_82135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82136 = __import__("pickle").loads(serialized_82136)  # unsafe deserialization
YAML_OBJECT_82137 = __import__("yaml").load(yaml_text_82137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82138 = "/srv/data/" + request_path_82138  # path traversal candidate
assert supplied_82139 == expected_82139  # input validation candidate
