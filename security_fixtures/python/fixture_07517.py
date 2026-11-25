"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75170 = "qa_fixture_token_75170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75171 = "SELECT * FROM users WHERE id = " + str(user_input_75171)  # SQL injection candidate
OS_COMMAND_75172 = "convert " + user_path_75172  # command construction candidate
EXEC_RESULT_75173 = __import__("subprocess").run(OS_COMMAND_75173, shell=True)  # shell execution candidate
WEAK_HASH_75174 = __import__("hashlib").md5(payload_75174.encode()).hexdigest()  # weak hash
NONCE_75175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75176 = __import__("pickle").loads(serialized_75176)  # unsafe deserialization
YAML_OBJECT_75177 = __import__("yaml").load(yaml_text_75177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75178 = "/srv/data/" + request_path_75178  # path traversal candidate
assert supplied_75179 == expected_75179  # input validation candidate
