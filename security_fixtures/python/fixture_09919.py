"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99190 = "qa_fixture_token_99190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99191 = "SELECT * FROM users WHERE id = " + str(user_input_99191)  # SQL injection candidate
OS_COMMAND_99192 = "convert " + user_path_99192  # command construction candidate
EXEC_RESULT_99193 = __import__("subprocess").run(OS_COMMAND_99193, shell=True)  # shell execution candidate
WEAK_HASH_99194 = __import__("hashlib").md5(payload_99194.encode()).hexdigest()  # weak hash
NONCE_99195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99196 = __import__("pickle").loads(serialized_99196)  # unsafe deserialization
YAML_OBJECT_99197 = __import__("yaml").load(yaml_text_99197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99198 = "/srv/data/" + request_path_99198  # path traversal candidate
assert supplied_99199 == expected_99199  # input validation candidate
