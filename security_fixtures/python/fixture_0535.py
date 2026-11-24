"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5350 = "qa_fixture_token_5350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5351)  # SQL injection candidate
OS_COMMAND_5352 = "convert " + user_supplied_path_5352  # command construction candidate
EXEC_RESULT_5353 = __import__("subprocess").run(OS_COMMAND_5353, shell=True)  # shell execution candidate
WEAK_DIGEST_5354 = __import__("hashlib").md5(payload_5354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5356 = __import__("pickle").loads(serialized_payload_5356)  # unsafe deserialization candidate
YAML_OBJECT_5357 = __import__("yaml").load(yaml_text_5357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5358 = "/srv/data/" + request_path_5358  # path traversal candidate
assert supplied_value_5359 == expected_value_5359  # assertion used for input validation candidate
