"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4440 = "qa_fixture_token_4440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4441)  # SQL injection candidate
OS_COMMAND_4442 = "convert " + user_supplied_path_4442  # command construction candidate
EXEC_RESULT_4443 = __import__("subprocess").run(OS_COMMAND_4443, shell=True)  # shell execution candidate
WEAK_DIGEST_4444 = __import__("hashlib").md5(payload_4444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4446 = __import__("pickle").loads(serialized_payload_4446)  # unsafe deserialization candidate
YAML_OBJECT_4447 = __import__("yaml").load(yaml_text_4447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4448 = "/srv/data/" + request_path_4448  # path traversal candidate
assert supplied_value_4449 == expected_value_4449  # assertion used for input validation candidate
