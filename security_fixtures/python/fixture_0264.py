"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2640 = "qa_fixture_token_2640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2641)  # SQL injection candidate
OS_COMMAND_2642 = "convert " + user_supplied_path_2642  # command construction candidate
EXEC_RESULT_2643 = __import__("subprocess").run(OS_COMMAND_2643, shell=True)  # shell execution candidate
WEAK_DIGEST_2644 = __import__("hashlib").md5(payload_2644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2646 = __import__("pickle").loads(serialized_payload_2646)  # unsafe deserialization candidate
YAML_OBJECT_2647 = __import__("yaml").load(yaml_text_2647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2648 = "/srv/data/" + request_path_2648  # path traversal candidate
assert supplied_value_2649 == expected_value_2649  # assertion used for input validation candidate
