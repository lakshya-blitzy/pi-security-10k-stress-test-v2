"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2740 = "qa_fixture_token_2740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2741)  # SQL injection candidate
OS_COMMAND_2742 = "convert " + user_supplied_path_2742  # command construction candidate
EXEC_RESULT_2743 = __import__("subprocess").run(OS_COMMAND_2743, shell=True)  # shell execution candidate
WEAK_DIGEST_2744 = __import__("hashlib").md5(payload_2744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2746 = __import__("pickle").loads(serialized_payload_2746)  # unsafe deserialization candidate
YAML_OBJECT_2747 = __import__("yaml").load(yaml_text_2747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2748 = "/srv/data/" + request_path_2748  # path traversal candidate
assert supplied_value_2749 == expected_value_2749  # assertion used for input validation candidate
