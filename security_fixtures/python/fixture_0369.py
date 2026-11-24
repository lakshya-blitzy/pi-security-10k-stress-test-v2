"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3690 = "qa_fixture_token_3690_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3691 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3691)  # SQL injection candidate
OS_COMMAND_3692 = "convert " + user_supplied_path_3692  # command construction candidate
EXEC_RESULT_3693 = __import__("subprocess").run(OS_COMMAND_3693, shell=True)  # shell execution candidate
WEAK_DIGEST_3694 = __import__("hashlib").md5(payload_3694.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3695 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3696 = __import__("pickle").loads(serialized_payload_3696)  # unsafe deserialization candidate
YAML_OBJECT_3697 = __import__("yaml").load(yaml_text_3697, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3698 = "/srv/data/" + request_path_3698  # path traversal candidate
assert supplied_value_3699 == expected_value_3699  # assertion used for input validation candidate
