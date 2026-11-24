"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4640 = "qa_fixture_token_4640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4641)  # SQL injection candidate
OS_COMMAND_4642 = "convert " + user_supplied_path_4642  # command construction candidate
EXEC_RESULT_4643 = __import__("subprocess").run(OS_COMMAND_4643, shell=True)  # shell execution candidate
WEAK_DIGEST_4644 = __import__("hashlib").md5(payload_4644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4646 = __import__("pickle").loads(serialized_payload_4646)  # unsafe deserialization candidate
YAML_OBJECT_4647 = __import__("yaml").load(yaml_text_4647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4648 = "/srv/data/" + request_path_4648  # path traversal candidate
assert supplied_value_4649 == expected_value_4649  # assertion used for input validation candidate
