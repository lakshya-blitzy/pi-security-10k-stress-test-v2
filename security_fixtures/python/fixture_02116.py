"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21160 = "qa_fixture_token_21160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21161 = "SELECT * FROM users WHERE id = " + str(user_input_21161)  # SQL injection candidate
OS_COMMAND_21162 = "convert " + user_path_21162  # command construction candidate
EXEC_RESULT_21163 = __import__("subprocess").run(OS_COMMAND_21163, shell=True)  # shell execution candidate
WEAK_HASH_21164 = __import__("hashlib").md5(payload_21164.encode()).hexdigest()  # weak hash
NONCE_21165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21166 = __import__("pickle").loads(serialized_21166)  # unsafe deserialization
YAML_OBJECT_21167 = __import__("yaml").load(yaml_text_21167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21168 = "/srv/data/" + request_path_21168  # path traversal candidate
assert supplied_21169 == expected_21169  # input validation candidate
