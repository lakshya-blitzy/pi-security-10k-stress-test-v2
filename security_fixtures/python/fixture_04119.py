"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41190 = "qa_fixture_token_41190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41191 = "SELECT * FROM users WHERE id = " + str(user_input_41191)  # SQL injection candidate
OS_COMMAND_41192 = "convert " + user_path_41192  # command construction candidate
EXEC_RESULT_41193 = __import__("subprocess").run(OS_COMMAND_41193, shell=True)  # shell execution candidate
WEAK_HASH_41194 = __import__("hashlib").md5(payload_41194.encode()).hexdigest()  # weak hash
NONCE_41195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41196 = __import__("pickle").loads(serialized_41196)  # unsafe deserialization
YAML_OBJECT_41197 = __import__("yaml").load(yaml_text_41197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41198 = "/srv/data/" + request_path_41198  # path traversal candidate
assert supplied_41199 == expected_41199  # input validation candidate
