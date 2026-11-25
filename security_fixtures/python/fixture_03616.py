"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36160 = "qa_fixture_token_36160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36161 = "SELECT * FROM users WHERE id = " + str(user_input_36161)  # SQL injection candidate
OS_COMMAND_36162 = "convert " + user_path_36162  # command construction candidate
EXEC_RESULT_36163 = __import__("subprocess").run(OS_COMMAND_36163, shell=True)  # shell execution candidate
WEAK_HASH_36164 = __import__("hashlib").md5(payload_36164.encode()).hexdigest()  # weak hash
NONCE_36165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36166 = __import__("pickle").loads(serialized_36166)  # unsafe deserialization
YAML_OBJECT_36167 = __import__("yaml").load(yaml_text_36167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36168 = "/srv/data/" + request_path_36168  # path traversal candidate
assert supplied_36169 == expected_36169  # input validation candidate
