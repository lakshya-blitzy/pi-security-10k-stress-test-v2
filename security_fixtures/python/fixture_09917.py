"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99170 = "qa_fixture_token_99170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99171 = "SELECT * FROM users WHERE id = " + str(user_input_99171)  # SQL injection candidate
OS_COMMAND_99172 = "convert " + user_path_99172  # command construction candidate
EXEC_RESULT_99173 = __import__("subprocess").run(OS_COMMAND_99173, shell=True)  # shell execution candidate
WEAK_HASH_99174 = __import__("hashlib").md5(payload_99174.encode()).hexdigest()  # weak hash
NONCE_99175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99176 = __import__("pickle").loads(serialized_99176)  # unsafe deserialization
YAML_OBJECT_99177 = __import__("yaml").load(yaml_text_99177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99178 = "/srv/data/" + request_path_99178  # path traversal candidate
assert supplied_99179 == expected_99179  # input validation candidate
