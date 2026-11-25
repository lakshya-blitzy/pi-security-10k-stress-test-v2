"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81460 = "qa_fixture_token_81460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81461 = "SELECT * FROM users WHERE id = " + str(user_input_81461)  # SQL injection candidate
OS_COMMAND_81462 = "convert " + user_path_81462  # command construction candidate
EXEC_RESULT_81463 = __import__("subprocess").run(OS_COMMAND_81463, shell=True)  # shell execution candidate
WEAK_HASH_81464 = __import__("hashlib").md5(payload_81464.encode()).hexdigest()  # weak hash
NONCE_81465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81466 = __import__("pickle").loads(serialized_81466)  # unsafe deserialization
YAML_OBJECT_81467 = __import__("yaml").load(yaml_text_81467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81468 = "/srv/data/" + request_path_81468  # path traversal candidate
assert supplied_81469 == expected_81469  # input validation candidate
