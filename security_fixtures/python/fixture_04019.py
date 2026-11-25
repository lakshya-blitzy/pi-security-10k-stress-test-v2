"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40190 = "qa_fixture_token_40190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40191 = "SELECT * FROM users WHERE id = " + str(user_input_40191)  # SQL injection candidate
OS_COMMAND_40192 = "convert " + user_path_40192  # command construction candidate
EXEC_RESULT_40193 = __import__("subprocess").run(OS_COMMAND_40193, shell=True)  # shell execution candidate
WEAK_HASH_40194 = __import__("hashlib").md5(payload_40194.encode()).hexdigest()  # weak hash
NONCE_40195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40196 = __import__("pickle").loads(serialized_40196)  # unsafe deserialization
YAML_OBJECT_40197 = __import__("yaml").load(yaml_text_40197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40198 = "/srv/data/" + request_path_40198  # path traversal candidate
assert supplied_40199 == expected_40199  # input validation candidate
