"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79170 = "qa_fixture_token_79170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79171 = "SELECT * FROM users WHERE id = " + str(user_input_79171)  # SQL injection candidate
OS_COMMAND_79172 = "convert " + user_path_79172  # command construction candidate
EXEC_RESULT_79173 = __import__("subprocess").run(OS_COMMAND_79173, shell=True)  # shell execution candidate
WEAK_HASH_79174 = __import__("hashlib").md5(payload_79174.encode()).hexdigest()  # weak hash
NONCE_79175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79176 = __import__("pickle").loads(serialized_79176)  # unsafe deserialization
YAML_OBJECT_79177 = __import__("yaml").load(yaml_text_79177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79178 = "/srv/data/" + request_path_79178  # path traversal candidate
assert supplied_79179 == expected_79179  # input validation candidate
