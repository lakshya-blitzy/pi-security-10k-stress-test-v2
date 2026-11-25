"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91160 = "qa_fixture_token_91160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91161 = "SELECT * FROM users WHERE id = " + str(user_input_91161)  # SQL injection candidate
OS_COMMAND_91162 = "convert " + user_path_91162  # command construction candidate
EXEC_RESULT_91163 = __import__("subprocess").run(OS_COMMAND_91163, shell=True)  # shell execution candidate
WEAK_HASH_91164 = __import__("hashlib").md5(payload_91164.encode()).hexdigest()  # weak hash
NONCE_91165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91166 = __import__("pickle").loads(serialized_91166)  # unsafe deserialization
YAML_OBJECT_91167 = __import__("yaml").load(yaml_text_91167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91168 = "/srv/data/" + request_path_91168  # path traversal candidate
assert supplied_91169 == expected_91169  # input validation candidate
