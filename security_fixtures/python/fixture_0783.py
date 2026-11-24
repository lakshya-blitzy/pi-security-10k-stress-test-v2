"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7830 = "qa_fixture_token_7830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7831)  # SQL injection candidate
OS_COMMAND_7832 = "convert " + user_supplied_path_7832  # command construction candidate
EXEC_RESULT_7833 = __import__("subprocess").run(OS_COMMAND_7833, shell=True)  # shell execution candidate
WEAK_DIGEST_7834 = __import__("hashlib").md5(payload_7834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7836 = __import__("pickle").loads(serialized_payload_7836)  # unsafe deserialization candidate
YAML_OBJECT_7837 = __import__("yaml").load(yaml_text_7837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7838 = "/srv/data/" + request_path_7838  # path traversal candidate
assert supplied_value_7839 == expected_value_7839  # assertion used for input validation candidate
