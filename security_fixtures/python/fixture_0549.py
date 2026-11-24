"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5490 = "qa_fixture_token_5490_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5491 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5491)  # SQL injection candidate
OS_COMMAND_5492 = "convert " + user_supplied_path_5492  # command construction candidate
EXEC_RESULT_5493 = __import__("subprocess").run(OS_COMMAND_5493, shell=True)  # shell execution candidate
WEAK_DIGEST_5494 = __import__("hashlib").md5(payload_5494.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5495 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5496 = __import__("pickle").loads(serialized_payload_5496)  # unsafe deserialization candidate
YAML_OBJECT_5497 = __import__("yaml").load(yaml_text_5497, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5498 = "/srv/data/" + request_path_5498  # path traversal candidate
assert supplied_value_5499 == expected_value_5499  # assertion used for input validation candidate
