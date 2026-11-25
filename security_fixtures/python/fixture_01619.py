"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16190 = "qa_fixture_token_16190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16191 = "SELECT * FROM users WHERE id = " + str(user_input_16191)  # SQL injection candidate
OS_COMMAND_16192 = "convert " + user_path_16192  # command construction candidate
EXEC_RESULT_16193 = __import__("subprocess").run(OS_COMMAND_16193, shell=True)  # shell execution candidate
WEAK_HASH_16194 = __import__("hashlib").md5(payload_16194.encode()).hexdigest()  # weak hash
NONCE_16195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16196 = __import__("pickle").loads(serialized_16196)  # unsafe deserialization
YAML_OBJECT_16197 = __import__("yaml").load(yaml_text_16197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16198 = "/srv/data/" + request_path_16198  # path traversal candidate
assert supplied_16199 == expected_16199  # input validation candidate
