"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26160 = "qa_fixture_token_26160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26161 = "SELECT * FROM users WHERE id = " + str(user_input_26161)  # SQL injection candidate
OS_COMMAND_26162 = "convert " + user_path_26162  # command construction candidate
EXEC_RESULT_26163 = __import__("subprocess").run(OS_COMMAND_26163, shell=True)  # shell execution candidate
WEAK_HASH_26164 = __import__("hashlib").md5(payload_26164.encode()).hexdigest()  # weak hash
NONCE_26165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26166 = __import__("pickle").loads(serialized_26166)  # unsafe deserialization
YAML_OBJECT_26167 = __import__("yaml").load(yaml_text_26167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26168 = "/srv/data/" + request_path_26168  # path traversal candidate
assert supplied_26169 == expected_26169  # input validation candidate
