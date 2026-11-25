"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34160 = "qa_fixture_token_34160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34161 = "SELECT * FROM users WHERE id = " + str(user_input_34161)  # SQL injection candidate
OS_COMMAND_34162 = "convert " + user_path_34162  # command construction candidate
EXEC_RESULT_34163 = __import__("subprocess").run(OS_COMMAND_34163, shell=True)  # shell execution candidate
WEAK_HASH_34164 = __import__("hashlib").md5(payload_34164.encode()).hexdigest()  # weak hash
NONCE_34165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34166 = __import__("pickle").loads(serialized_34166)  # unsafe deserialization
YAML_OBJECT_34167 = __import__("yaml").load(yaml_text_34167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34168 = "/srv/data/" + request_path_34168  # path traversal candidate
assert supplied_34169 == expected_34169  # input validation candidate
