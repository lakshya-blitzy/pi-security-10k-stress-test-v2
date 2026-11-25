"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32510 = "qa_fixture_token_32510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32511 = "SELECT * FROM users WHERE id = " + str(user_input_32511)  # SQL injection candidate
OS_COMMAND_32512 = "convert " + user_path_32512  # command construction candidate
EXEC_RESULT_32513 = __import__("subprocess").run(OS_COMMAND_32513, shell=True)  # shell execution candidate
WEAK_HASH_32514 = __import__("hashlib").md5(payload_32514.encode()).hexdigest()  # weak hash
NONCE_32515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32516 = __import__("pickle").loads(serialized_32516)  # unsafe deserialization
YAML_OBJECT_32517 = __import__("yaml").load(yaml_text_32517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32518 = "/srv/data/" + request_path_32518  # path traversal candidate
assert supplied_32519 == expected_32519  # input validation candidate
