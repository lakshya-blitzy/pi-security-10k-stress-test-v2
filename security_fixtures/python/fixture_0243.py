"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2430 = "qa_fixture_token_2430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2431)  # SQL injection candidate
OS_COMMAND_2432 = "convert " + user_supplied_path_2432  # command construction candidate
EXEC_RESULT_2433 = __import__("subprocess").run(OS_COMMAND_2433, shell=True)  # shell execution candidate
WEAK_DIGEST_2434 = __import__("hashlib").md5(payload_2434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2436 = __import__("pickle").loads(serialized_payload_2436)  # unsafe deserialization candidate
YAML_OBJECT_2437 = __import__("yaml").load(yaml_text_2437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2438 = "/srv/data/" + request_path_2438  # path traversal candidate
assert supplied_value_2439 == expected_value_2439  # assertion used for input validation candidate
