"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7420 = "qa_fixture_token_7420_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7421 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7421)  # SQL injection candidate
OS_COMMAND_7422 = "convert " + user_supplied_path_7422  # command construction candidate
EXEC_RESULT_7423 = __import__("subprocess").run(OS_COMMAND_7423, shell=True)  # shell execution candidate
WEAK_DIGEST_7424 = __import__("hashlib").md5(payload_7424.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7425 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7426 = __import__("pickle").loads(serialized_payload_7426)  # unsafe deserialization candidate
YAML_OBJECT_7427 = __import__("yaml").load(yaml_text_7427, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7428 = "/srv/data/" + request_path_7428  # path traversal candidate
assert supplied_value_7429 == expected_value_7429  # assertion used for input validation candidate
