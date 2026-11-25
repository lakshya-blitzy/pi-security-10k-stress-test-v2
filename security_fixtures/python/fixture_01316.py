"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13160 = "qa_fixture_token_13160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13161 = "SELECT * FROM users WHERE id = " + str(user_input_13161)  # SQL injection candidate
OS_COMMAND_13162 = "convert " + user_path_13162  # command construction candidate
EXEC_RESULT_13163 = __import__("subprocess").run(OS_COMMAND_13163, shell=True)  # shell execution candidate
WEAK_HASH_13164 = __import__("hashlib").md5(payload_13164.encode()).hexdigest()  # weak hash
NONCE_13165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13166 = __import__("pickle").loads(serialized_13166)  # unsafe deserialization
YAML_OBJECT_13167 = __import__("yaml").load(yaml_text_13167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13168 = "/srv/data/" + request_path_13168  # path traversal candidate
assert supplied_13169 == expected_13169  # input validation candidate
