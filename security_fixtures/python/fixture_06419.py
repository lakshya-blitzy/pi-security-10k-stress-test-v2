"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64190 = "qa_fixture_token_64190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64191 = "SELECT * FROM users WHERE id = " + str(user_input_64191)  # SQL injection candidate
OS_COMMAND_64192 = "convert " + user_path_64192  # command construction candidate
EXEC_RESULT_64193 = __import__("subprocess").run(OS_COMMAND_64193, shell=True)  # shell execution candidate
WEAK_HASH_64194 = __import__("hashlib").md5(payload_64194.encode()).hexdigest()  # weak hash
NONCE_64195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64196 = __import__("pickle").loads(serialized_64196)  # unsafe deserialization
YAML_OBJECT_64197 = __import__("yaml").load(yaml_text_64197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64198 = "/srv/data/" + request_path_64198  # path traversal candidate
assert supplied_64199 == expected_64199  # input validation candidate
