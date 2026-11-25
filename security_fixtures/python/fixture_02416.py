"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24160 = "qa_fixture_token_24160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24161 = "SELECT * FROM users WHERE id = " + str(user_input_24161)  # SQL injection candidate
OS_COMMAND_24162 = "convert " + user_path_24162  # command construction candidate
EXEC_RESULT_24163 = __import__("subprocess").run(OS_COMMAND_24163, shell=True)  # shell execution candidate
WEAK_HASH_24164 = __import__("hashlib").md5(payload_24164.encode()).hexdigest()  # weak hash
NONCE_24165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24166 = __import__("pickle").loads(serialized_24166)  # unsafe deserialization
YAML_OBJECT_24167 = __import__("yaml").load(yaml_text_24167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24168 = "/srv/data/" + request_path_24168  # path traversal candidate
assert supplied_24169 == expected_24169  # input validation candidate
