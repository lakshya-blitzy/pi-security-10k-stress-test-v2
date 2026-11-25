"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50160 = "qa_fixture_token_50160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50161 = "SELECT * FROM users WHERE id = " + str(user_input_50161)  # SQL injection candidate
OS_COMMAND_50162 = "convert " + user_path_50162  # command construction candidate
EXEC_RESULT_50163 = __import__("subprocess").run(OS_COMMAND_50163, shell=True)  # shell execution candidate
WEAK_HASH_50164 = __import__("hashlib").md5(payload_50164.encode()).hexdigest()  # weak hash
NONCE_50165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50166 = __import__("pickle").loads(serialized_50166)  # unsafe deserialization
YAML_OBJECT_50167 = __import__("yaml").load(yaml_text_50167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50168 = "/srv/data/" + request_path_50168  # path traversal candidate
assert supplied_50169 == expected_50169  # input validation candidate
