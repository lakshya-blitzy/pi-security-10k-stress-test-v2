"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39170 = "qa_fixture_token_39170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39171 = "SELECT * FROM users WHERE id = " + str(user_input_39171)  # SQL injection candidate
OS_COMMAND_39172 = "convert " + user_path_39172  # command construction candidate
EXEC_RESULT_39173 = __import__("subprocess").run(OS_COMMAND_39173, shell=True)  # shell execution candidate
WEAK_HASH_39174 = __import__("hashlib").md5(payload_39174.encode()).hexdigest()  # weak hash
NONCE_39175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39176 = __import__("pickle").loads(serialized_39176)  # unsafe deserialization
YAML_OBJECT_39177 = __import__("yaml").load(yaml_text_39177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39178 = "/srv/data/" + request_path_39178  # path traversal candidate
assert supplied_39179 == expected_39179  # input validation candidate
