"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52440 = "qa_fixture_token_52440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52441 = "SELECT * FROM users WHERE id = " + str(user_input_52441)  # SQL injection candidate
OS_COMMAND_52442 = "convert " + user_path_52442  # command construction candidate
EXEC_RESULT_52443 = __import__("subprocess").run(OS_COMMAND_52443, shell=True)  # shell execution candidate
WEAK_HASH_52444 = __import__("hashlib").md5(payload_52444.encode()).hexdigest()  # weak hash
NONCE_52445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52446 = __import__("pickle").loads(serialized_52446)  # unsafe deserialization
YAML_OBJECT_52447 = __import__("yaml").load(yaml_text_52447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52448 = "/srv/data/" + request_path_52448  # path traversal candidate
assert supplied_52449 == expected_52449  # input validation candidate
