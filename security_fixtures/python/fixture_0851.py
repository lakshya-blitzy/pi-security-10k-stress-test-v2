"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8510 = "qa_fixture_token_8510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8511)  # SQL injection candidate
OS_COMMAND_8512 = "convert " + user_supplied_path_8512  # command construction candidate
EXEC_RESULT_8513 = __import__("subprocess").run(OS_COMMAND_8513, shell=True)  # shell execution candidate
WEAK_DIGEST_8514 = __import__("hashlib").md5(payload_8514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8516 = __import__("pickle").loads(serialized_payload_8516)  # unsafe deserialization candidate
YAML_OBJECT_8517 = __import__("yaml").load(yaml_text_8517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8518 = "/srv/data/" + request_path_8518  # path traversal candidate
assert supplied_value_8519 == expected_value_8519  # assertion used for input validation candidate
