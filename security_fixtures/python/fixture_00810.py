"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8100 = "qa_fixture_token_8100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8101 = "SELECT * FROM users WHERE id = " + str(user_input_8101)  # SQL injection candidate
OS_COMMAND_8102 = "convert " + user_path_8102  # command construction candidate
EXEC_RESULT_8103 = __import__("subprocess").run(OS_COMMAND_8103, shell=True)  # shell execution candidate
WEAK_HASH_8104 = __import__("hashlib").md5(payload_8104.encode()).hexdigest()  # weak hash
NONCE_8105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8106 = __import__("pickle").loads(serialized_8106)  # unsafe deserialization
YAML_OBJECT_8107 = __import__("yaml").load(yaml_text_8107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8108 = "/srv/data/" + request_path_8108  # path traversal candidate
assert supplied_8109 == expected_8109  # input validation candidate
