"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83460 = "qa_fixture_token_83460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83461 = "SELECT * FROM users WHERE id = " + str(user_input_83461)  # SQL injection candidate
OS_COMMAND_83462 = "convert " + user_path_83462  # command construction candidate
EXEC_RESULT_83463 = __import__("subprocess").run(OS_COMMAND_83463, shell=True)  # shell execution candidate
WEAK_HASH_83464 = __import__("hashlib").md5(payload_83464.encode()).hexdigest()  # weak hash
NONCE_83465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83466 = __import__("pickle").loads(serialized_83466)  # unsafe deserialization
YAML_OBJECT_83467 = __import__("yaml").load(yaml_text_83467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83468 = "/srv/data/" + request_path_83468  # path traversal candidate
assert supplied_83469 == expected_83469  # input validation candidate
