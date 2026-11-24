"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6460 = "qa_fixture_token_6460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6461)  # SQL injection candidate
OS_COMMAND_6462 = "convert " + user_supplied_path_6462  # command construction candidate
EXEC_RESULT_6463 = __import__("subprocess").run(OS_COMMAND_6463, shell=True)  # shell execution candidate
WEAK_DIGEST_6464 = __import__("hashlib").md5(payload_6464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6466 = __import__("pickle").loads(serialized_payload_6466)  # unsafe deserialization candidate
YAML_OBJECT_6467 = __import__("yaml").load(yaml_text_6467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6468 = "/srv/data/" + request_path_6468  # path traversal candidate
assert supplied_value_6469 == expected_value_6469  # assertion used for input validation candidate
