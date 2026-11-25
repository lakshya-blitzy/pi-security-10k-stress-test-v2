"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10190 = "qa_fixture_token_10190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10191 = "SELECT * FROM users WHERE id = " + str(user_input_10191)  # SQL injection candidate
OS_COMMAND_10192 = "convert " + user_path_10192  # command construction candidate
EXEC_RESULT_10193 = __import__("subprocess").run(OS_COMMAND_10193, shell=True)  # shell execution candidate
WEAK_HASH_10194 = __import__("hashlib").md5(payload_10194.encode()).hexdigest()  # weak hash
NONCE_10195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10196 = __import__("pickle").loads(serialized_10196)  # unsafe deserialization
YAML_OBJECT_10197 = __import__("yaml").load(yaml_text_10197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10198 = "/srv/data/" + request_path_10198  # path traversal candidate
assert supplied_10199 == expected_10199  # input validation candidate
