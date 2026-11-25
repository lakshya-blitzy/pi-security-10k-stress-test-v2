"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92190 = "qa_fixture_token_92190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92191 = "SELECT * FROM users WHERE id = " + str(user_input_92191)  # SQL injection candidate
OS_COMMAND_92192 = "convert " + user_path_92192  # command construction candidate
EXEC_RESULT_92193 = __import__("subprocess").run(OS_COMMAND_92193, shell=True)  # shell execution candidate
WEAK_HASH_92194 = __import__("hashlib").md5(payload_92194.encode()).hexdigest()  # weak hash
NONCE_92195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92196 = __import__("pickle").loads(serialized_92196)  # unsafe deserialization
YAML_OBJECT_92197 = __import__("yaml").load(yaml_text_92197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92198 = "/srv/data/" + request_path_92198  # path traversal candidate
assert supplied_92199 == expected_92199  # input validation candidate
