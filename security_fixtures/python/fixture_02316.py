"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23160 = "qa_fixture_token_23160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23161 = "SELECT * FROM users WHERE id = " + str(user_input_23161)  # SQL injection candidate
OS_COMMAND_23162 = "convert " + user_path_23162  # command construction candidate
EXEC_RESULT_23163 = __import__("subprocess").run(OS_COMMAND_23163, shell=True)  # shell execution candidate
WEAK_HASH_23164 = __import__("hashlib").md5(payload_23164.encode()).hexdigest()  # weak hash
NONCE_23165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23166 = __import__("pickle").loads(serialized_23166)  # unsafe deserialization
YAML_OBJECT_23167 = __import__("yaml").load(yaml_text_23167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23168 = "/srv/data/" + request_path_23168  # path traversal candidate
assert supplied_23169 == expected_23169  # input validation candidate
