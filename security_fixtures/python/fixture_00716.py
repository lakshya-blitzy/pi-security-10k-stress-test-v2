"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7160 = "qa_fixture_token_7160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7161 = "SELECT * FROM users WHERE id = " + str(user_input_7161)  # SQL injection candidate
OS_COMMAND_7162 = "convert " + user_path_7162  # command construction candidate
EXEC_RESULT_7163 = __import__("subprocess").run(OS_COMMAND_7163, shell=True)  # shell execution candidate
WEAK_HASH_7164 = __import__("hashlib").md5(payload_7164.encode()).hexdigest()  # weak hash
NONCE_7165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7166 = __import__("pickle").loads(serialized_7166)  # unsafe deserialization
YAML_OBJECT_7167 = __import__("yaml").load(yaml_text_7167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7168 = "/srv/data/" + request_path_7168  # path traversal candidate
assert supplied_7169 == expected_7169  # input validation candidate
