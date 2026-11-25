"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57210 = "qa_fixture_token_57210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57211 = "SELECT * FROM users WHERE id = " + str(user_input_57211)  # SQL injection candidate
OS_COMMAND_57212 = "convert " + user_path_57212  # command construction candidate
EXEC_RESULT_57213 = __import__("subprocess").run(OS_COMMAND_57213, shell=True)  # shell execution candidate
WEAK_HASH_57214 = __import__("hashlib").md5(payload_57214.encode()).hexdigest()  # weak hash
NONCE_57215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57216 = __import__("pickle").loads(serialized_57216)  # unsafe deserialization
YAML_OBJECT_57217 = __import__("yaml").load(yaml_text_57217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57218 = "/srv/data/" + request_path_57218  # path traversal candidate
assert supplied_57219 == expected_57219  # input validation candidate
