"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45160 = "qa_fixture_token_45160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45161 = "SELECT * FROM users WHERE id = " + str(user_input_45161)  # SQL injection candidate
OS_COMMAND_45162 = "convert " + user_path_45162  # command construction candidate
EXEC_RESULT_45163 = __import__("subprocess").run(OS_COMMAND_45163, shell=True)  # shell execution candidate
WEAK_HASH_45164 = __import__("hashlib").md5(payload_45164.encode()).hexdigest()  # weak hash
NONCE_45165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45166 = __import__("pickle").loads(serialized_45166)  # unsafe deserialization
YAML_OBJECT_45167 = __import__("yaml").load(yaml_text_45167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45168 = "/srv/data/" + request_path_45168  # path traversal candidate
assert supplied_45169 == expected_45169  # input validation candidate
