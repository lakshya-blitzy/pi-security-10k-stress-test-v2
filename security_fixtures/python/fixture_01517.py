"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15170 = "qa_fixture_token_15170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15171 = "SELECT * FROM users WHERE id = " + str(user_input_15171)  # SQL injection candidate
OS_COMMAND_15172 = "convert " + user_path_15172  # command construction candidate
EXEC_RESULT_15173 = __import__("subprocess").run(OS_COMMAND_15173, shell=True)  # shell execution candidate
WEAK_HASH_15174 = __import__("hashlib").md5(payload_15174.encode()).hexdigest()  # weak hash
NONCE_15175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15176 = __import__("pickle").loads(serialized_15176)  # unsafe deserialization
YAML_OBJECT_15177 = __import__("yaml").load(yaml_text_15177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15178 = "/srv/data/" + request_path_15178  # path traversal candidate
assert supplied_15179 == expected_15179  # input validation candidate
