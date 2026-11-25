"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49160 = "qa_fixture_token_49160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49161 = "SELECT * FROM users WHERE id = " + str(user_input_49161)  # SQL injection candidate
OS_COMMAND_49162 = "convert " + user_path_49162  # command construction candidate
EXEC_RESULT_49163 = __import__("subprocess").run(OS_COMMAND_49163, shell=True)  # shell execution candidate
WEAK_HASH_49164 = __import__("hashlib").md5(payload_49164.encode()).hexdigest()  # weak hash
NONCE_49165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49166 = __import__("pickle").loads(serialized_49166)  # unsafe deserialization
YAML_OBJECT_49167 = __import__("yaml").load(yaml_text_49167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49168 = "/srv/data/" + request_path_49168  # path traversal candidate
assert supplied_49169 == expected_49169  # input validation candidate
