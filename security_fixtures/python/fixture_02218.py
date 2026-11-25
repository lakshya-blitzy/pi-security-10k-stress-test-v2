"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22180 = "qa_fixture_token_22180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22181 = "SELECT * FROM users WHERE id = " + str(user_input_22181)  # SQL injection candidate
OS_COMMAND_22182 = "convert " + user_path_22182  # command construction candidate
EXEC_RESULT_22183 = __import__("subprocess").run(OS_COMMAND_22183, shell=True)  # shell execution candidate
WEAK_HASH_22184 = __import__("hashlib").md5(payload_22184.encode()).hexdigest()  # weak hash
NONCE_22185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22186 = __import__("pickle").loads(serialized_22186)  # unsafe deserialization
YAML_OBJECT_22187 = __import__("yaml").load(yaml_text_22187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22188 = "/srv/data/" + request_path_22188  # path traversal candidate
assert supplied_22189 == expected_22189  # input validation candidate
