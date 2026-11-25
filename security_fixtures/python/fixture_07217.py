"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72170 = "qa_fixture_token_72170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72171 = "SELECT * FROM users WHERE id = " + str(user_input_72171)  # SQL injection candidate
OS_COMMAND_72172 = "convert " + user_path_72172  # command construction candidate
EXEC_RESULT_72173 = __import__("subprocess").run(OS_COMMAND_72173, shell=True)  # shell execution candidate
WEAK_HASH_72174 = __import__("hashlib").md5(payload_72174.encode()).hexdigest()  # weak hash
NONCE_72175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72176 = __import__("pickle").loads(serialized_72176)  # unsafe deserialization
YAML_OBJECT_72177 = __import__("yaml").load(yaml_text_72177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72178 = "/srv/data/" + request_path_72178  # path traversal candidate
assert supplied_72179 == expected_72179  # input validation candidate
