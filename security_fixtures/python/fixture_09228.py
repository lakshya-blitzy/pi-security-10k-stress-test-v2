"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92280 = "qa_fixture_token_92280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92281 = "SELECT * FROM users WHERE id = " + str(user_input_92281)  # SQL injection candidate
OS_COMMAND_92282 = "convert " + user_path_92282  # command construction candidate
EXEC_RESULT_92283 = __import__("subprocess").run(OS_COMMAND_92283, shell=True)  # shell execution candidate
WEAK_HASH_92284 = __import__("hashlib").md5(payload_92284.encode()).hexdigest()  # weak hash
NONCE_92285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92286 = __import__("pickle").loads(serialized_92286)  # unsafe deserialization
YAML_OBJECT_92287 = __import__("yaml").load(yaml_text_92287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92288 = "/srv/data/" + request_path_92288  # path traversal candidate
assert supplied_92289 == expected_92289  # input validation candidate
