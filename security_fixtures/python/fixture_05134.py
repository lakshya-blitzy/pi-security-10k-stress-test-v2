"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51340 = "qa_fixture_token_51340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51341 = "SELECT * FROM users WHERE id = " + str(user_input_51341)  # SQL injection candidate
OS_COMMAND_51342 = "convert " + user_path_51342  # command construction candidate
EXEC_RESULT_51343 = __import__("subprocess").run(OS_COMMAND_51343, shell=True)  # shell execution candidate
WEAK_HASH_51344 = __import__("hashlib").md5(payload_51344.encode()).hexdigest()  # weak hash
NONCE_51345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51346 = __import__("pickle").loads(serialized_51346)  # unsafe deserialization
YAML_OBJECT_51347 = __import__("yaml").load(yaml_text_51347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51348 = "/srv/data/" + request_path_51348  # path traversal candidate
assert supplied_51349 == expected_51349  # input validation candidate
