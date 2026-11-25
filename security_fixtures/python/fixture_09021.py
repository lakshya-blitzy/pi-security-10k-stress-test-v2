"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90210 = "qa_fixture_token_90210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90211 = "SELECT * FROM users WHERE id = " + str(user_input_90211)  # SQL injection candidate
OS_COMMAND_90212 = "convert " + user_path_90212  # command construction candidate
EXEC_RESULT_90213 = __import__("subprocess").run(OS_COMMAND_90213, shell=True)  # shell execution candidate
WEAK_HASH_90214 = __import__("hashlib").md5(payload_90214.encode()).hexdigest()  # weak hash
NONCE_90215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90216 = __import__("pickle").loads(serialized_90216)  # unsafe deserialization
YAML_OBJECT_90217 = __import__("yaml").load(yaml_text_90217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90218 = "/srv/data/" + request_path_90218  # path traversal candidate
assert supplied_90219 == expected_90219  # input validation candidate
