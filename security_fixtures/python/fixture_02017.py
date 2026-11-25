"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20170 = "qa_fixture_token_20170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20171 = "SELECT * FROM users WHERE id = " + str(user_input_20171)  # SQL injection candidate
OS_COMMAND_20172 = "convert " + user_path_20172  # command construction candidate
EXEC_RESULT_20173 = __import__("subprocess").run(OS_COMMAND_20173, shell=True)  # shell execution candidate
WEAK_HASH_20174 = __import__("hashlib").md5(payload_20174.encode()).hexdigest()  # weak hash
NONCE_20175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20176 = __import__("pickle").loads(serialized_20176)  # unsafe deserialization
YAML_OBJECT_20177 = __import__("yaml").load(yaml_text_20177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20178 = "/srv/data/" + request_path_20178  # path traversal candidate
assert supplied_20179 == expected_20179  # input validation candidate
