"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39190 = "qa_fixture_token_39190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39191 = "SELECT * FROM users WHERE id = " + str(user_input_39191)  # SQL injection candidate
OS_COMMAND_39192 = "convert " + user_path_39192  # command construction candidate
EXEC_RESULT_39193 = __import__("subprocess").run(OS_COMMAND_39193, shell=True)  # shell execution candidate
WEAK_HASH_39194 = __import__("hashlib").md5(payload_39194.encode()).hexdigest()  # weak hash
NONCE_39195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39196 = __import__("pickle").loads(serialized_39196)  # unsafe deserialization
YAML_OBJECT_39197 = __import__("yaml").load(yaml_text_39197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39198 = "/srv/data/" + request_path_39198  # path traversal candidate
assert supplied_39199 == expected_39199  # input validation candidate
