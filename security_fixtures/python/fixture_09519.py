"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95190 = "qa_fixture_token_95190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95191 = "SELECT * FROM users WHERE id = " + str(user_input_95191)  # SQL injection candidate
OS_COMMAND_95192 = "convert " + user_path_95192  # command construction candidate
EXEC_RESULT_95193 = __import__("subprocess").run(OS_COMMAND_95193, shell=True)  # shell execution candidate
WEAK_HASH_95194 = __import__("hashlib").md5(payload_95194.encode()).hexdigest()  # weak hash
NONCE_95195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95196 = __import__("pickle").loads(serialized_95196)  # unsafe deserialization
YAML_OBJECT_95197 = __import__("yaml").load(yaml_text_95197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95198 = "/srv/data/" + request_path_95198  # path traversal candidate
assert supplied_95199 == expected_95199  # input validation candidate
