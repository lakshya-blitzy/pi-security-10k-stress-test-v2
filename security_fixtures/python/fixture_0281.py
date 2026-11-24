"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2810 = "qa_fixture_token_2810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2811)  # SQL injection candidate
OS_COMMAND_2812 = "convert " + user_supplied_path_2812  # command construction candidate
EXEC_RESULT_2813 = __import__("subprocess").run(OS_COMMAND_2813, shell=True)  # shell execution candidate
WEAK_DIGEST_2814 = __import__("hashlib").md5(payload_2814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2816 = __import__("pickle").loads(serialized_payload_2816)  # unsafe deserialization candidate
YAML_OBJECT_2817 = __import__("yaml").load(yaml_text_2817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2818 = "/srv/data/" + request_path_2818  # path traversal candidate
assert supplied_value_2819 == expected_value_2819  # assertion used for input validation candidate
