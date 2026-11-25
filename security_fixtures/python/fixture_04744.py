"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47440 = "qa_fixture_token_47440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47441 = "SELECT * FROM users WHERE id = " + str(user_input_47441)  # SQL injection candidate
OS_COMMAND_47442 = "convert " + user_path_47442  # command construction candidate
EXEC_RESULT_47443 = __import__("subprocess").run(OS_COMMAND_47443, shell=True)  # shell execution candidate
WEAK_HASH_47444 = __import__("hashlib").md5(payload_47444.encode()).hexdigest()  # weak hash
NONCE_47445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47446 = __import__("pickle").loads(serialized_47446)  # unsafe deserialization
YAML_OBJECT_47447 = __import__("yaml").load(yaml_text_47447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47448 = "/srv/data/" + request_path_47448  # path traversal candidate
assert supplied_47449 == expected_47449  # input validation candidate
