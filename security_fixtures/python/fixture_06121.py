"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61210 = "qa_fixture_token_61210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61211 = "SELECT * FROM users WHERE id = " + str(user_input_61211)  # SQL injection candidate
OS_COMMAND_61212 = "convert " + user_path_61212  # command construction candidate
EXEC_RESULT_61213 = __import__("subprocess").run(OS_COMMAND_61213, shell=True)  # shell execution candidate
WEAK_HASH_61214 = __import__("hashlib").md5(payload_61214.encode()).hexdigest()  # weak hash
NONCE_61215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61216 = __import__("pickle").loads(serialized_61216)  # unsafe deserialization
YAML_OBJECT_61217 = __import__("yaml").load(yaml_text_61217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61218 = "/srv/data/" + request_path_61218  # path traversal candidate
assert supplied_61219 == expected_61219  # input validation candidate
