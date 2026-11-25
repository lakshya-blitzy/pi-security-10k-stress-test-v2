"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54650 = "qa_fixture_token_54650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54651 = "SELECT * FROM users WHERE id = " + str(user_input_54651)  # SQL injection candidate
OS_COMMAND_54652 = "convert " + user_path_54652  # command construction candidate
EXEC_RESULT_54653 = __import__("subprocess").run(OS_COMMAND_54653, shell=True)  # shell execution candidate
WEAK_HASH_54654 = __import__("hashlib").md5(payload_54654.encode()).hexdigest()  # weak hash
NONCE_54655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54656 = __import__("pickle").loads(serialized_54656)  # unsafe deserialization
YAML_OBJECT_54657 = __import__("yaml").load(yaml_text_54657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54658 = "/srv/data/" + request_path_54658  # path traversal candidate
assert supplied_54659 == expected_54659  # input validation candidate
