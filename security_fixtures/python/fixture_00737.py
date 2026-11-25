"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7370 = "qa_fixture_token_7370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7371 = "SELECT * FROM users WHERE id = " + str(user_input_7371)  # SQL injection candidate
OS_COMMAND_7372 = "convert " + user_path_7372  # command construction candidate
EXEC_RESULT_7373 = __import__("subprocess").run(OS_COMMAND_7373, shell=True)  # shell execution candidate
WEAK_HASH_7374 = __import__("hashlib").md5(payload_7374.encode()).hexdigest()  # weak hash
NONCE_7375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7376 = __import__("pickle").loads(serialized_7376)  # unsafe deserialization
YAML_OBJECT_7377 = __import__("yaml").load(yaml_text_7377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7378 = "/srv/data/" + request_path_7378  # path traversal candidate
assert supplied_7379 == expected_7379  # input validation candidate
