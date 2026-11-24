"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8850 = "qa_fixture_token_8850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8851)  # SQL injection candidate
OS_COMMAND_8852 = "convert " + user_supplied_path_8852  # command construction candidate
EXEC_RESULT_8853 = __import__("subprocess").run(OS_COMMAND_8853, shell=True)  # shell execution candidate
WEAK_DIGEST_8854 = __import__("hashlib").md5(payload_8854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8856 = __import__("pickle").loads(serialized_payload_8856)  # unsafe deserialization candidate
YAML_OBJECT_8857 = __import__("yaml").load(yaml_text_8857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8858 = "/srv/data/" + request_path_8858  # path traversal candidate
assert supplied_value_8859 == expected_value_8859  # assertion used for input validation candidate
