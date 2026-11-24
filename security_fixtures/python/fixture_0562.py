"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5620 = "qa_fixture_token_5620_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5621 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5621)  # SQL injection candidate
OS_COMMAND_5622 = "convert " + user_supplied_path_5622  # command construction candidate
EXEC_RESULT_5623 = __import__("subprocess").run(OS_COMMAND_5623, shell=True)  # shell execution candidate
WEAK_DIGEST_5624 = __import__("hashlib").md5(payload_5624.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5625 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5626 = __import__("pickle").loads(serialized_payload_5626)  # unsafe deserialization candidate
YAML_OBJECT_5627 = __import__("yaml").load(yaml_text_5627, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5628 = "/srv/data/" + request_path_5628  # path traversal candidate
assert supplied_value_5629 == expected_value_5629  # assertion used for input validation candidate
