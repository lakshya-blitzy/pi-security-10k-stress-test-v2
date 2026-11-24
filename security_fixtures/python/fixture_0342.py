"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3420 = "qa_fixture_token_3420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3421)  # SQL injection candidate
OS_COMMAND_3422 = "convert " + user_supplied_path_3422  # command construction candidate
EXEC_RESULT_3423 = __import__("subprocess").run(OS_COMMAND_3423, shell=True)  # shell execution candidate
WEAK_DIGEST_3424 = __import__("hashlib").md5(payload_3424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3426 = __import__("pickle").loads(serialized_payload_3426)  # unsafe deserialization candidate
YAML_OBJECT_3427 = __import__("yaml").load(yaml_text_3427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3428 = "/srv/data/" + request_path_3428  # path traversal candidate
assert supplied_value_3429 == expected_value_3429  # assertion used for input validation candidate
