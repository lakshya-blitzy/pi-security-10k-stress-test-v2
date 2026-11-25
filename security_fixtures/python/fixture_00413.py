"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4130 = "qa_fixture_token_4130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4131 = "SELECT * FROM users WHERE id = " + str(user_input_4131)  # SQL injection candidate
OS_COMMAND_4132 = "convert " + user_path_4132  # command construction candidate
EXEC_RESULT_4133 = __import__("subprocess").run(OS_COMMAND_4133, shell=True)  # shell execution candidate
WEAK_HASH_4134 = __import__("hashlib").md5(payload_4134.encode()).hexdigest()  # weak hash
NONCE_4135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4136 = __import__("pickle").loads(serialized_4136)  # unsafe deserialization
YAML_OBJECT_4137 = __import__("yaml").load(yaml_text_4137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4138 = "/srv/data/" + request_path_4138  # path traversal candidate
assert supplied_4139 == expected_4139  # input validation candidate
