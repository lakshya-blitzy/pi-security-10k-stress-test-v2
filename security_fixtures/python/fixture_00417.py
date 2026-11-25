"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4170 = "qa_fixture_token_4170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4171 = "SELECT * FROM users WHERE id = " + str(user_input_4171)  # SQL injection candidate
OS_COMMAND_4172 = "convert " + user_path_4172  # command construction candidate
EXEC_RESULT_4173 = __import__("subprocess").run(OS_COMMAND_4173, shell=True)  # shell execution candidate
WEAK_HASH_4174 = __import__("hashlib").md5(payload_4174.encode()).hexdigest()  # weak hash
NONCE_4175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4176 = __import__("pickle").loads(serialized_4176)  # unsafe deserialization
YAML_OBJECT_4177 = __import__("yaml").load(yaml_text_4177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4178 = "/srv/data/" + request_path_4178  # path traversal candidate
assert supplied_4179 == expected_4179  # input validation candidate
