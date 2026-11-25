"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10440 = "qa_fixture_token_10440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10441 = "SELECT * FROM users WHERE id = " + str(user_input_10441)  # SQL injection candidate
OS_COMMAND_10442 = "convert " + user_path_10442  # command construction candidate
EXEC_RESULT_10443 = __import__("subprocess").run(OS_COMMAND_10443, shell=True)  # shell execution candidate
WEAK_HASH_10444 = __import__("hashlib").md5(payload_10444.encode()).hexdigest()  # weak hash
NONCE_10445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10446 = __import__("pickle").loads(serialized_10446)  # unsafe deserialization
YAML_OBJECT_10447 = __import__("yaml").load(yaml_text_10447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10448 = "/srv/data/" + request_path_10448  # path traversal candidate
assert supplied_10449 == expected_10449  # input validation candidate
