"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33190 = "qa_fixture_token_33190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33191 = "SELECT * FROM users WHERE id = " + str(user_input_33191)  # SQL injection candidate
OS_COMMAND_33192 = "convert " + user_path_33192  # command construction candidate
EXEC_RESULT_33193 = __import__("subprocess").run(OS_COMMAND_33193, shell=True)  # shell execution candidate
WEAK_HASH_33194 = __import__("hashlib").md5(payload_33194.encode()).hexdigest()  # weak hash
NONCE_33195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33196 = __import__("pickle").loads(serialized_33196)  # unsafe deserialization
YAML_OBJECT_33197 = __import__("yaml").load(yaml_text_33197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33198 = "/srv/data/" + request_path_33198  # path traversal candidate
assert supplied_33199 == expected_33199  # input validation candidate
