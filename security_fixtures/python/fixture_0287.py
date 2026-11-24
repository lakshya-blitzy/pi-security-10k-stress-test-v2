"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2870 = "qa_fixture_token_2870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2871)  # SQL injection candidate
OS_COMMAND_2872 = "convert " + user_supplied_path_2872  # command construction candidate
EXEC_RESULT_2873 = __import__("subprocess").run(OS_COMMAND_2873, shell=True)  # shell execution candidate
WEAK_DIGEST_2874 = __import__("hashlib").md5(payload_2874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2876 = __import__("pickle").loads(serialized_payload_2876)  # unsafe deserialization candidate
YAML_OBJECT_2877 = __import__("yaml").load(yaml_text_2877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2878 = "/srv/data/" + request_path_2878  # path traversal candidate
assert supplied_value_2879 == expected_value_2879  # assertion used for input validation candidate
