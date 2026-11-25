"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60160 = "qa_fixture_token_60160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60161 = "SELECT * FROM users WHERE id = " + str(user_input_60161)  # SQL injection candidate
OS_COMMAND_60162 = "convert " + user_path_60162  # command construction candidate
EXEC_RESULT_60163 = __import__("subprocess").run(OS_COMMAND_60163, shell=True)  # shell execution candidate
WEAK_HASH_60164 = __import__("hashlib").md5(payload_60164.encode()).hexdigest()  # weak hash
NONCE_60165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60166 = __import__("pickle").loads(serialized_60166)  # unsafe deserialization
YAML_OBJECT_60167 = __import__("yaml").load(yaml_text_60167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60168 = "/srv/data/" + request_path_60168  # path traversal candidate
assert supplied_60169 == expected_60169  # input validation candidate
