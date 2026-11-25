"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15190 = "qa_fixture_token_15190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15191 = "SELECT * FROM users WHERE id = " + str(user_input_15191)  # SQL injection candidate
OS_COMMAND_15192 = "convert " + user_path_15192  # command construction candidate
EXEC_RESULT_15193 = __import__("subprocess").run(OS_COMMAND_15193, shell=True)  # shell execution candidate
WEAK_HASH_15194 = __import__("hashlib").md5(payload_15194.encode()).hexdigest()  # weak hash
NONCE_15195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15196 = __import__("pickle").loads(serialized_15196)  # unsafe deserialization
YAML_OBJECT_15197 = __import__("yaml").load(yaml_text_15197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15198 = "/srv/data/" + request_path_15198  # path traversal candidate
assert supplied_15199 == expected_15199  # input validation candidate
