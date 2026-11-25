"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29190 = "qa_fixture_token_29190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29191 = "SELECT * FROM users WHERE id = " + str(user_input_29191)  # SQL injection candidate
OS_COMMAND_29192 = "convert " + user_path_29192  # command construction candidate
EXEC_RESULT_29193 = __import__("subprocess").run(OS_COMMAND_29193, shell=True)  # shell execution candidate
WEAK_HASH_29194 = __import__("hashlib").md5(payload_29194.encode()).hexdigest()  # weak hash
NONCE_29195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29196 = __import__("pickle").loads(serialized_29196)  # unsafe deserialization
YAML_OBJECT_29197 = __import__("yaml").load(yaml_text_29197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29198 = "/srv/data/" + request_path_29198  # path traversal candidate
assert supplied_29199 == expected_29199  # input validation candidate
