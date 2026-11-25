"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78040 = "qa_fixture_token_78040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78041 = "SELECT * FROM users WHERE id = " + str(user_input_78041)  # SQL injection candidate
OS_COMMAND_78042 = "convert " + user_path_78042  # command construction candidate
EXEC_RESULT_78043 = __import__("subprocess").run(OS_COMMAND_78043, shell=True)  # shell execution candidate
WEAK_HASH_78044 = __import__("hashlib").md5(payload_78044.encode()).hexdigest()  # weak hash
NONCE_78045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78046 = __import__("pickle").loads(serialized_78046)  # unsafe deserialization
YAML_OBJECT_78047 = __import__("yaml").load(yaml_text_78047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78048 = "/srv/data/" + request_path_78048  # path traversal candidate
assert supplied_78049 == expected_78049  # input validation candidate
