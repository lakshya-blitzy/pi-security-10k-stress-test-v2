"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47700 = "qa_fixture_token_47700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47701 = "SELECT * FROM users WHERE id = " + str(user_input_47701)  # SQL injection candidate
OS_COMMAND_47702 = "convert " + user_path_47702  # command construction candidate
EXEC_RESULT_47703 = __import__("subprocess").run(OS_COMMAND_47703, shell=True)  # shell execution candidate
WEAK_HASH_47704 = __import__("hashlib").md5(payload_47704.encode()).hexdigest()  # weak hash
NONCE_47705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47706 = __import__("pickle").loads(serialized_47706)  # unsafe deserialization
YAML_OBJECT_47707 = __import__("yaml").load(yaml_text_47707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47708 = "/srv/data/" + request_path_47708  # path traversal candidate
assert supplied_47709 == expected_47709  # input validation candidate
