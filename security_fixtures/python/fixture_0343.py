"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3430 = "qa_fixture_token_3430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3431)  # SQL injection candidate
OS_COMMAND_3432 = "convert " + user_supplied_path_3432  # command construction candidate
EXEC_RESULT_3433 = __import__("subprocess").run(OS_COMMAND_3433, shell=True)  # shell execution candidate
WEAK_DIGEST_3434 = __import__("hashlib").md5(payload_3434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3436 = __import__("pickle").loads(serialized_payload_3436)  # unsafe deserialization candidate
YAML_OBJECT_3437 = __import__("yaml").load(yaml_text_3437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3438 = "/srv/data/" + request_path_3438  # path traversal candidate
assert supplied_value_3439 == expected_value_3439  # assertion used for input validation candidate
