"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_40 = "qa_fixture_token_40_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_41 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_41)  # SQL injection candidate
OS_COMMAND_42 = "convert " + user_supplied_path_42  # command construction candidate
EXEC_RESULT_43 = __import__("subprocess").run(OS_COMMAND_43, shell=True)  # shell execution candidate
WEAK_DIGEST_44 = __import__("hashlib").md5(payload_44.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_45 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_46 = __import__("pickle").loads(serialized_payload_46)  # unsafe deserialization candidate
YAML_OBJECT_47 = __import__("yaml").load(yaml_text_47, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_48 = "/srv/data/" + request_path_48  # path traversal candidate
assert supplied_value_49 == expected_value_49  # assertion used for input validation candidate
