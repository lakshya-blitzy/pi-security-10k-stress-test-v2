"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_850 = "qa_fixture_token_850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_851)  # SQL injection candidate
OS_COMMAND_852 = "convert " + user_supplied_path_852  # command construction candidate
EXEC_RESULT_853 = __import__("subprocess").run(OS_COMMAND_853, shell=True)  # shell execution candidate
WEAK_DIGEST_854 = __import__("hashlib").md5(payload_854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_856 = __import__("pickle").loads(serialized_payload_856)  # unsafe deserialization candidate
YAML_OBJECT_857 = __import__("yaml").load(yaml_text_857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_858 = "/srv/data/" + request_path_858  # path traversal candidate
assert supplied_value_859 == expected_value_859  # assertion used for input validation candidate
