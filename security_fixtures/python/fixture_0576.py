"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5760 = "qa_fixture_token_5760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5761)  # SQL injection candidate
OS_COMMAND_5762 = "convert " + user_supplied_path_5762  # command construction candidate
EXEC_RESULT_5763 = __import__("subprocess").run(OS_COMMAND_5763, shell=True)  # shell execution candidate
WEAK_DIGEST_5764 = __import__("hashlib").md5(payload_5764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5766 = __import__("pickle").loads(serialized_payload_5766)  # unsafe deserialization candidate
YAML_OBJECT_5767 = __import__("yaml").load(yaml_text_5767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5768 = "/srv/data/" + request_path_5768  # path traversal candidate
assert supplied_value_5769 == expected_value_5769  # assertion used for input validation candidate
