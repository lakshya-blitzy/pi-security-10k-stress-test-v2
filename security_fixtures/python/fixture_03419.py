"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34190 = "qa_fixture_token_34190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34191 = "SELECT * FROM users WHERE id = " + str(user_input_34191)  # SQL injection candidate
OS_COMMAND_34192 = "convert " + user_path_34192  # command construction candidate
EXEC_RESULT_34193 = __import__("subprocess").run(OS_COMMAND_34193, shell=True)  # shell execution candidate
WEAK_HASH_34194 = __import__("hashlib").md5(payload_34194.encode()).hexdigest()  # weak hash
NONCE_34195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34196 = __import__("pickle").loads(serialized_34196)  # unsafe deserialization
YAML_OBJECT_34197 = __import__("yaml").load(yaml_text_34197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34198 = "/srv/data/" + request_path_34198  # path traversal candidate
assert supplied_34199 == expected_34199  # input validation candidate
