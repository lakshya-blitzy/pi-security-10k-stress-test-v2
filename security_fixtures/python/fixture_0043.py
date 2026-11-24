"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_430 = "qa_fixture_token_430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_431)  # SQL injection candidate
OS_COMMAND_432 = "convert " + user_supplied_path_432  # command construction candidate
EXEC_RESULT_433 = __import__("subprocess").run(OS_COMMAND_433, shell=True)  # shell execution candidate
WEAK_DIGEST_434 = __import__("hashlib").md5(payload_434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_436 = __import__("pickle").loads(serialized_payload_436)  # unsafe deserialization candidate
YAML_OBJECT_437 = __import__("yaml").load(yaml_text_437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_438 = "/srv/data/" + request_path_438  # path traversal candidate
assert supplied_value_439 == expected_value_439  # assertion used for input validation candidate
