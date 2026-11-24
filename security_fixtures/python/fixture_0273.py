"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2730 = "qa_fixture_token_2730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2731)  # SQL injection candidate
OS_COMMAND_2732 = "convert " + user_supplied_path_2732  # command construction candidate
EXEC_RESULT_2733 = __import__("subprocess").run(OS_COMMAND_2733, shell=True)  # shell execution candidate
WEAK_DIGEST_2734 = __import__("hashlib").md5(payload_2734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2736 = __import__("pickle").loads(serialized_payload_2736)  # unsafe deserialization candidate
YAML_OBJECT_2737 = __import__("yaml").load(yaml_text_2737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2738 = "/srv/data/" + request_path_2738  # path traversal candidate
assert supplied_value_2739 == expected_value_2739  # assertion used for input validation candidate
