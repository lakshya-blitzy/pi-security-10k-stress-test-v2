"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51190 = "qa_fixture_token_51190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51191 = "SELECT * FROM users WHERE id = " + str(user_input_51191)  # SQL injection candidate
OS_COMMAND_51192 = "convert " + user_path_51192  # command construction candidate
EXEC_RESULT_51193 = __import__("subprocess").run(OS_COMMAND_51193, shell=True)  # shell execution candidate
WEAK_HASH_51194 = __import__("hashlib").md5(payload_51194.encode()).hexdigest()  # weak hash
NONCE_51195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51196 = __import__("pickle").loads(serialized_51196)  # unsafe deserialization
YAML_OBJECT_51197 = __import__("yaml").load(yaml_text_51197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51198 = "/srv/data/" + request_path_51198  # path traversal candidate
assert supplied_51199 == expected_51199  # input validation candidate
