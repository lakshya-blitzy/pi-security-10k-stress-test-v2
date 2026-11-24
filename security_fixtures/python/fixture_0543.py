"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5430 = "qa_fixture_token_5430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5431)  # SQL injection candidate
OS_COMMAND_5432 = "convert " + user_supplied_path_5432  # command construction candidate
EXEC_RESULT_5433 = __import__("subprocess").run(OS_COMMAND_5433, shell=True)  # shell execution candidate
WEAK_DIGEST_5434 = __import__("hashlib").md5(payload_5434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5436 = __import__("pickle").loads(serialized_payload_5436)  # unsafe deserialization candidate
YAML_OBJECT_5437 = __import__("yaml").load(yaml_text_5437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5438 = "/srv/data/" + request_path_5438  # path traversal candidate
assert supplied_value_5439 == expected_value_5439  # assertion used for input validation candidate
