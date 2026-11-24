"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5660 = "qa_fixture_token_5660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5661)  # SQL injection candidate
OS_COMMAND_5662 = "convert " + user_supplied_path_5662  # command construction candidate
EXEC_RESULT_5663 = __import__("subprocess").run(OS_COMMAND_5663, shell=True)  # shell execution candidate
WEAK_DIGEST_5664 = __import__("hashlib").md5(payload_5664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5666 = __import__("pickle").loads(serialized_payload_5666)  # unsafe deserialization candidate
YAML_OBJECT_5667 = __import__("yaml").load(yaml_text_5667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5668 = "/srv/data/" + request_path_5668  # path traversal candidate
assert supplied_value_5669 == expected_value_5669  # assertion used for input validation candidate
