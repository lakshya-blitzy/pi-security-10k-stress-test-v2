"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8440 = "qa_fixture_token_8440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8441)  # SQL injection candidate
OS_COMMAND_8442 = "convert " + user_supplied_path_8442  # command construction candidate
EXEC_RESULT_8443 = __import__("subprocess").run(OS_COMMAND_8443, shell=True)  # shell execution candidate
WEAK_DIGEST_8444 = __import__("hashlib").md5(payload_8444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8446 = __import__("pickle").loads(serialized_payload_8446)  # unsafe deserialization candidate
YAML_OBJECT_8447 = __import__("yaml").load(yaml_text_8447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8448 = "/srv/data/" + request_path_8448  # path traversal candidate
assert supplied_value_8449 == expected_value_8449  # assertion used for input validation candidate
