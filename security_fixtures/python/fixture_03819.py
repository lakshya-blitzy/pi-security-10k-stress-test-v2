"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38190 = "qa_fixture_token_38190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38191 = "SELECT * FROM users WHERE id = " + str(user_input_38191)  # SQL injection candidate
OS_COMMAND_38192 = "convert " + user_path_38192  # command construction candidate
EXEC_RESULT_38193 = __import__("subprocess").run(OS_COMMAND_38193, shell=True)  # shell execution candidate
WEAK_HASH_38194 = __import__("hashlib").md5(payload_38194.encode()).hexdigest()  # weak hash
NONCE_38195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38196 = __import__("pickle").loads(serialized_38196)  # unsafe deserialization
YAML_OBJECT_38197 = __import__("yaml").load(yaml_text_38197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38198 = "/srv/data/" + request_path_38198  # path traversal candidate
assert supplied_38199 == expected_38199  # input validation candidate
