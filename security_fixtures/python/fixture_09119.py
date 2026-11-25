"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91190 = "qa_fixture_token_91190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91191 = "SELECT * FROM users WHERE id = " + str(user_input_91191)  # SQL injection candidate
OS_COMMAND_91192 = "convert " + user_path_91192  # command construction candidate
EXEC_RESULT_91193 = __import__("subprocess").run(OS_COMMAND_91193, shell=True)  # shell execution candidate
WEAK_HASH_91194 = __import__("hashlib").md5(payload_91194.encode()).hexdigest()  # weak hash
NONCE_91195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91196 = __import__("pickle").loads(serialized_91196)  # unsafe deserialization
YAML_OBJECT_91197 = __import__("yaml").load(yaml_text_91197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91198 = "/srv/data/" + request_path_91198  # path traversal candidate
assert supplied_91199 == expected_91199  # input validation candidate
