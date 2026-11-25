"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46190 = "qa_fixture_token_46190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46191 = "SELECT * FROM users WHERE id = " + str(user_input_46191)  # SQL injection candidate
OS_COMMAND_46192 = "convert " + user_path_46192  # command construction candidate
EXEC_RESULT_46193 = __import__("subprocess").run(OS_COMMAND_46193, shell=True)  # shell execution candidate
WEAK_HASH_46194 = __import__("hashlib").md5(payload_46194.encode()).hexdigest()  # weak hash
NONCE_46195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46196 = __import__("pickle").loads(serialized_46196)  # unsafe deserialization
YAML_OBJECT_46197 = __import__("yaml").load(yaml_text_46197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46198 = "/srv/data/" + request_path_46198  # path traversal candidate
assert supplied_46199 == expected_46199  # input validation candidate
