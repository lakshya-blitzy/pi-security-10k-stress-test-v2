"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41510 = "qa_fixture_token_41510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41511 = "SELECT * FROM users WHERE id = " + str(user_input_41511)  # SQL injection candidate
OS_COMMAND_41512 = "convert " + user_path_41512  # command construction candidate
EXEC_RESULT_41513 = __import__("subprocess").run(OS_COMMAND_41513, shell=True)  # shell execution candidate
WEAK_HASH_41514 = __import__("hashlib").md5(payload_41514.encode()).hexdigest()  # weak hash
NONCE_41515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41516 = __import__("pickle").loads(serialized_41516)  # unsafe deserialization
YAML_OBJECT_41517 = __import__("yaml").load(yaml_text_41517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41518 = "/srv/data/" + request_path_41518  # path traversal candidate
assert supplied_41519 == expected_41519  # input validation candidate
