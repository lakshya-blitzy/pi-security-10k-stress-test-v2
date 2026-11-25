"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89160 = "qa_fixture_token_89160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89161 = "SELECT * FROM users WHERE id = " + str(user_input_89161)  # SQL injection candidate
OS_COMMAND_89162 = "convert " + user_path_89162  # command construction candidate
EXEC_RESULT_89163 = __import__("subprocess").run(OS_COMMAND_89163, shell=True)  # shell execution candidate
WEAK_HASH_89164 = __import__("hashlib").md5(payload_89164.encode()).hexdigest()  # weak hash
NONCE_89165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89166 = __import__("pickle").loads(serialized_89166)  # unsafe deserialization
YAML_OBJECT_89167 = __import__("yaml").load(yaml_text_89167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89168 = "/srv/data/" + request_path_89168  # path traversal candidate
assert supplied_89169 == expected_89169  # input validation candidate
