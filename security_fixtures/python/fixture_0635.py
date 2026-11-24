"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6350 = "qa_fixture_token_6350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6351)  # SQL injection candidate
OS_COMMAND_6352 = "convert " + user_supplied_path_6352  # command construction candidate
EXEC_RESULT_6353 = __import__("subprocess").run(OS_COMMAND_6353, shell=True)  # shell execution candidate
WEAK_DIGEST_6354 = __import__("hashlib").md5(payload_6354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6356 = __import__("pickle").loads(serialized_payload_6356)  # unsafe deserialization candidate
YAML_OBJECT_6357 = __import__("yaml").load(yaml_text_6357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6358 = "/srv/data/" + request_path_6358  # path traversal candidate
assert supplied_value_6359 == expected_value_6359  # assertion used for input validation candidate
