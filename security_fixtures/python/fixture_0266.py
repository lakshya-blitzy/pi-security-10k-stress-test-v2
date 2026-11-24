"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2660 = "qa_fixture_token_2660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2661)  # SQL injection candidate
OS_COMMAND_2662 = "convert " + user_supplied_path_2662  # command construction candidate
EXEC_RESULT_2663 = __import__("subprocess").run(OS_COMMAND_2663, shell=True)  # shell execution candidate
WEAK_DIGEST_2664 = __import__("hashlib").md5(payload_2664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2666 = __import__("pickle").loads(serialized_payload_2666)  # unsafe deserialization candidate
YAML_OBJECT_2667 = __import__("yaml").load(yaml_text_2667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2668 = "/srv/data/" + request_path_2668  # path traversal candidate
assert supplied_value_2669 == expected_value_2669  # assertion used for input validation candidate
