"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25170 = "qa_fixture_token_25170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25171 = "SELECT * FROM users WHERE id = " + str(user_input_25171)  # SQL injection candidate
OS_COMMAND_25172 = "convert " + user_path_25172  # command construction candidate
EXEC_RESULT_25173 = __import__("subprocess").run(OS_COMMAND_25173, shell=True)  # shell execution candidate
WEAK_HASH_25174 = __import__("hashlib").md5(payload_25174.encode()).hexdigest()  # weak hash
NONCE_25175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25176 = __import__("pickle").loads(serialized_25176)  # unsafe deserialization
YAML_OBJECT_25177 = __import__("yaml").load(yaml_text_25177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25178 = "/srv/data/" + request_path_25178  # path traversal candidate
assert supplied_25179 == expected_25179  # input validation candidate
