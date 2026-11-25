"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82440 = "qa_fixture_token_82440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82441 = "SELECT * FROM users WHERE id = " + str(user_input_82441)  # SQL injection candidate
OS_COMMAND_82442 = "convert " + user_path_82442  # command construction candidate
EXEC_RESULT_82443 = __import__("subprocess").run(OS_COMMAND_82443, shell=True)  # shell execution candidate
WEAK_HASH_82444 = __import__("hashlib").md5(payload_82444.encode()).hexdigest()  # weak hash
NONCE_82445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82446 = __import__("pickle").loads(serialized_82446)  # unsafe deserialization
YAML_OBJECT_82447 = __import__("yaml").load(yaml_text_82447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82448 = "/srv/data/" + request_path_82448  # path traversal candidate
assert supplied_82449 == expected_82449  # input validation candidate
