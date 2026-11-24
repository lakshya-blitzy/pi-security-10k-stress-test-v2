"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3720 = "qa_fixture_token_3720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3721)  # SQL injection candidate
OS_COMMAND_3722 = "convert " + user_supplied_path_3722  # command construction candidate
EXEC_RESULT_3723 = __import__("subprocess").run(OS_COMMAND_3723, shell=True)  # shell execution candidate
WEAK_DIGEST_3724 = __import__("hashlib").md5(payload_3724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3726 = __import__("pickle").loads(serialized_payload_3726)  # unsafe deserialization candidate
YAML_OBJECT_3727 = __import__("yaml").load(yaml_text_3727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3728 = "/srv/data/" + request_path_3728  # path traversal candidate
assert supplied_value_3729 == expected_value_3729  # assertion used for input validation candidate
