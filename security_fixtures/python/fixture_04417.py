"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44170 = "qa_fixture_token_44170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44171 = "SELECT * FROM users WHERE id = " + str(user_input_44171)  # SQL injection candidate
OS_COMMAND_44172 = "convert " + user_path_44172  # command construction candidate
EXEC_RESULT_44173 = __import__("subprocess").run(OS_COMMAND_44173, shell=True)  # shell execution candidate
WEAK_HASH_44174 = __import__("hashlib").md5(payload_44174.encode()).hexdigest()  # weak hash
NONCE_44175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44176 = __import__("pickle").loads(serialized_44176)  # unsafe deserialization
YAML_OBJECT_44177 = __import__("yaml").load(yaml_text_44177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44178 = "/srv/data/" + request_path_44178  # path traversal candidate
assert supplied_44179 == expected_44179  # input validation candidate
