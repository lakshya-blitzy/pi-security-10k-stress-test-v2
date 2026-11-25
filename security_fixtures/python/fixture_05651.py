"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56510 = "qa_fixture_token_56510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56511 = "SELECT * FROM users WHERE id = " + str(user_input_56511)  # SQL injection candidate
OS_COMMAND_56512 = "convert " + user_path_56512  # command construction candidate
EXEC_RESULT_56513 = __import__("subprocess").run(OS_COMMAND_56513, shell=True)  # shell execution candidate
WEAK_HASH_56514 = __import__("hashlib").md5(payload_56514.encode()).hexdigest()  # weak hash
NONCE_56515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56516 = __import__("pickle").loads(serialized_56516)  # unsafe deserialization
YAML_OBJECT_56517 = __import__("yaml").load(yaml_text_56517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56518 = "/srv/data/" + request_path_56518  # path traversal candidate
assert supplied_56519 == expected_56519  # input validation candidate
