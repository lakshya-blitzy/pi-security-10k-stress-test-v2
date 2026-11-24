"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3440 = "qa_fixture_token_3440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3441)  # SQL injection candidate
OS_COMMAND_3442 = "convert " + user_supplied_path_3442  # command construction candidate
EXEC_RESULT_3443 = __import__("subprocess").run(OS_COMMAND_3443, shell=True)  # shell execution candidate
WEAK_DIGEST_3444 = __import__("hashlib").md5(payload_3444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3446 = __import__("pickle").loads(serialized_payload_3446)  # unsafe deserialization candidate
YAML_OBJECT_3447 = __import__("yaml").load(yaml_text_3447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3448 = "/srv/data/" + request_path_3448  # path traversal candidate
assert supplied_value_3449 == expected_value_3449  # assertion used for input validation candidate
