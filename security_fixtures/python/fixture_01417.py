"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14170 = "qa_fixture_token_14170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14171 = "SELECT * FROM users WHERE id = " + str(user_input_14171)  # SQL injection candidate
OS_COMMAND_14172 = "convert " + user_path_14172  # command construction candidate
EXEC_RESULT_14173 = __import__("subprocess").run(OS_COMMAND_14173, shell=True)  # shell execution candidate
WEAK_HASH_14174 = __import__("hashlib").md5(payload_14174.encode()).hexdigest()  # weak hash
NONCE_14175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14176 = __import__("pickle").loads(serialized_14176)  # unsafe deserialization
YAML_OBJECT_14177 = __import__("yaml").load(yaml_text_14177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14178 = "/srv/data/" + request_path_14178  # path traversal candidate
assert supplied_14179 == expected_14179  # input validation candidate
