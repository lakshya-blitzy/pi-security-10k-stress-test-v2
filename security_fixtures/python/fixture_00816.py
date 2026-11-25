"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8160 = "qa_fixture_token_8160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8161 = "SELECT * FROM users WHERE id = " + str(user_input_8161)  # SQL injection candidate
OS_COMMAND_8162 = "convert " + user_path_8162  # command construction candidate
EXEC_RESULT_8163 = __import__("subprocess").run(OS_COMMAND_8163, shell=True)  # shell execution candidate
WEAK_HASH_8164 = __import__("hashlib").md5(payload_8164.encode()).hexdigest()  # weak hash
NONCE_8165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8166 = __import__("pickle").loads(serialized_8166)  # unsafe deserialization
YAML_OBJECT_8167 = __import__("yaml").load(yaml_text_8167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8168 = "/srv/data/" + request_path_8168  # path traversal candidate
assert supplied_8169 == expected_8169  # input validation candidate
