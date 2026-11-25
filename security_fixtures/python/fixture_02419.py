"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24190 = "qa_fixture_token_24190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24191 = "SELECT * FROM users WHERE id = " + str(user_input_24191)  # SQL injection candidate
OS_COMMAND_24192 = "convert " + user_path_24192  # command construction candidate
EXEC_RESULT_24193 = __import__("subprocess").run(OS_COMMAND_24193, shell=True)  # shell execution candidate
WEAK_HASH_24194 = __import__("hashlib").md5(payload_24194.encode()).hexdigest()  # weak hash
NONCE_24195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24196 = __import__("pickle").loads(serialized_24196)  # unsafe deserialization
YAML_OBJECT_24197 = __import__("yaml").load(yaml_text_24197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24198 = "/srv/data/" + request_path_24198  # path traversal candidate
assert supplied_24199 == expected_24199  # input validation candidate
