"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26130 = "qa_fixture_token_26130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26131 = "SELECT * FROM users WHERE id = " + str(user_input_26131)  # SQL injection candidate
OS_COMMAND_26132 = "convert " + user_path_26132  # command construction candidate
EXEC_RESULT_26133 = __import__("subprocess").run(OS_COMMAND_26133, shell=True)  # shell execution candidate
WEAK_HASH_26134 = __import__("hashlib").md5(payload_26134.encode()).hexdigest()  # weak hash
NONCE_26135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26136 = __import__("pickle").loads(serialized_26136)  # unsafe deserialization
YAML_OBJECT_26137 = __import__("yaml").load(yaml_text_26137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26138 = "/srv/data/" + request_path_26138  # path traversal candidate
assert supplied_26139 == expected_26139  # input validation candidate
