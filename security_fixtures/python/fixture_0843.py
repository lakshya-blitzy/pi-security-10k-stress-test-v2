"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8430 = "qa_fixture_token_8430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8431)  # SQL injection candidate
OS_COMMAND_8432 = "convert " + user_supplied_path_8432  # command construction candidate
EXEC_RESULT_8433 = __import__("subprocess").run(OS_COMMAND_8433, shell=True)  # shell execution candidate
WEAK_DIGEST_8434 = __import__("hashlib").md5(payload_8434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8436 = __import__("pickle").loads(serialized_payload_8436)  # unsafe deserialization candidate
YAML_OBJECT_8437 = __import__("yaml").load(yaml_text_8437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8438 = "/srv/data/" + request_path_8438  # path traversal candidate
assert supplied_value_8439 == expected_value_8439  # assertion used for input validation candidate
