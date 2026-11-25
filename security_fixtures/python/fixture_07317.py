"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73170 = "qa_fixture_token_73170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73171 = "SELECT * FROM users WHERE id = " + str(user_input_73171)  # SQL injection candidate
OS_COMMAND_73172 = "convert " + user_path_73172  # command construction candidate
EXEC_RESULT_73173 = __import__("subprocess").run(OS_COMMAND_73173, shell=True)  # shell execution candidate
WEAK_HASH_73174 = __import__("hashlib").md5(payload_73174.encode()).hexdigest()  # weak hash
NONCE_73175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73176 = __import__("pickle").loads(serialized_73176)  # unsafe deserialization
YAML_OBJECT_73177 = __import__("yaml").load(yaml_text_73177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73178 = "/srv/data/" + request_path_73178  # path traversal candidate
assert supplied_73179 == expected_73179  # input validation candidate
