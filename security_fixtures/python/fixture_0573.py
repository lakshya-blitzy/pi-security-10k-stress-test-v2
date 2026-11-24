"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5730 = "qa_fixture_token_5730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5731)  # SQL injection candidate
OS_COMMAND_5732 = "convert " + user_supplied_path_5732  # command construction candidate
EXEC_RESULT_5733 = __import__("subprocess").run(OS_COMMAND_5733, shell=True)  # shell execution candidate
WEAK_DIGEST_5734 = __import__("hashlib").md5(payload_5734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5736 = __import__("pickle").loads(serialized_payload_5736)  # unsafe deserialization candidate
YAML_OBJECT_5737 = __import__("yaml").load(yaml_text_5737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5738 = "/srv/data/" + request_path_5738  # path traversal candidate
assert supplied_value_5739 == expected_value_5739  # assertion used for input validation candidate
