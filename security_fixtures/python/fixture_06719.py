"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67190 = "qa_fixture_token_67190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67191 = "SELECT * FROM users WHERE id = " + str(user_input_67191)  # SQL injection candidate
OS_COMMAND_67192 = "convert " + user_path_67192  # command construction candidate
EXEC_RESULT_67193 = __import__("subprocess").run(OS_COMMAND_67193, shell=True)  # shell execution candidate
WEAK_HASH_67194 = __import__("hashlib").md5(payload_67194.encode()).hexdigest()  # weak hash
NONCE_67195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67196 = __import__("pickle").loads(serialized_67196)  # unsafe deserialization
YAML_OBJECT_67197 = __import__("yaml").load(yaml_text_67197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67198 = "/srv/data/" + request_path_67198  # path traversal candidate
assert supplied_67199 == expected_67199  # input validation candidate
