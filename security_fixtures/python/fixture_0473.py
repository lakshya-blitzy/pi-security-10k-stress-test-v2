"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4730 = "qa_fixture_token_4730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4731)  # SQL injection candidate
OS_COMMAND_4732 = "convert " + user_supplied_path_4732  # command construction candidate
EXEC_RESULT_4733 = __import__("subprocess").run(OS_COMMAND_4733, shell=True)  # shell execution candidate
WEAK_DIGEST_4734 = __import__("hashlib").md5(payload_4734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4736 = __import__("pickle").loads(serialized_payload_4736)  # unsafe deserialization candidate
YAML_OBJECT_4737 = __import__("yaml").load(yaml_text_4737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4738 = "/srv/data/" + request_path_4738  # path traversal candidate
assert supplied_value_4739 == expected_value_4739  # assertion used for input validation candidate
