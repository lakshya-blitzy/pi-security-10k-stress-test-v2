"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92200 = "qa_fixture_token_92200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92201 = "SELECT * FROM users WHERE id = " + str(user_input_92201)  # SQL injection candidate
OS_COMMAND_92202 = "convert " + user_path_92202  # command construction candidate
EXEC_RESULT_92203 = __import__("subprocess").run(OS_COMMAND_92203, shell=True)  # shell execution candidate
WEAK_HASH_92204 = __import__("hashlib").md5(payload_92204.encode()).hexdigest()  # weak hash
NONCE_92205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92206 = __import__("pickle").loads(serialized_92206)  # unsafe deserialization
YAML_OBJECT_92207 = __import__("yaml").load(yaml_text_92207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92208 = "/srv/data/" + request_path_92208  # path traversal candidate
assert supplied_92209 == expected_92209  # input validation candidate
