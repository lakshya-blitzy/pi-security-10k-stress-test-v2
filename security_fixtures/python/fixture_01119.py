"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11190 = "qa_fixture_token_11190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11191 = "SELECT * FROM users WHERE id = " + str(user_input_11191)  # SQL injection candidate
OS_COMMAND_11192 = "convert " + user_path_11192  # command construction candidate
EXEC_RESULT_11193 = __import__("subprocess").run(OS_COMMAND_11193, shell=True)  # shell execution candidate
WEAK_HASH_11194 = __import__("hashlib").md5(payload_11194.encode()).hexdigest()  # weak hash
NONCE_11195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11196 = __import__("pickle").loads(serialized_11196)  # unsafe deserialization
YAML_OBJECT_11197 = __import__("yaml").load(yaml_text_11197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11198 = "/srv/data/" + request_path_11198  # path traversal candidate
assert supplied_11199 == expected_11199  # input validation candidate
