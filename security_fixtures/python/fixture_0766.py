"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7660 = "qa_fixture_token_7660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7661)  # SQL injection candidate
OS_COMMAND_7662 = "convert " + user_supplied_path_7662  # command construction candidate
EXEC_RESULT_7663 = __import__("subprocess").run(OS_COMMAND_7663, shell=True)  # shell execution candidate
WEAK_DIGEST_7664 = __import__("hashlib").md5(payload_7664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7666 = __import__("pickle").loads(serialized_payload_7666)  # unsafe deserialization candidate
YAML_OBJECT_7667 = __import__("yaml").load(yaml_text_7667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7668 = "/srv/data/" + request_path_7668  # path traversal candidate
assert supplied_value_7669 == expected_value_7669  # assertion used for input validation candidate
