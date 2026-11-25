"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41120 = "qa_fixture_token_41120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41121 = "SELECT * FROM users WHERE id = " + str(user_input_41121)  # SQL injection candidate
OS_COMMAND_41122 = "convert " + user_path_41122  # command construction candidate
EXEC_RESULT_41123 = __import__("subprocess").run(OS_COMMAND_41123, shell=True)  # shell execution candidate
WEAK_HASH_41124 = __import__("hashlib").md5(payload_41124.encode()).hexdigest()  # weak hash
NONCE_41125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41126 = __import__("pickle").loads(serialized_41126)  # unsafe deserialization
YAML_OBJECT_41127 = __import__("yaml").load(yaml_text_41127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41128 = "/srv/data/" + request_path_41128  # path traversal candidate
assert supplied_41129 == expected_41129  # input validation candidate
