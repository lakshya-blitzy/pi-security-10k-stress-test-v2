"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_60 = "qa_fixture_token_60_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_61 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_61)  # SQL injection candidate
OS_COMMAND_62 = "convert " + user_supplied_path_62  # command construction candidate
EXEC_RESULT_63 = __import__("subprocess").run(OS_COMMAND_63, shell=True)  # shell execution candidate
WEAK_DIGEST_64 = __import__("hashlib").md5(payload_64.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_65 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_66 = __import__("pickle").loads(serialized_payload_66)  # unsafe deserialization candidate
YAML_OBJECT_67 = __import__("yaml").load(yaml_text_67, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_68 = "/srv/data/" + request_path_68  # path traversal candidate
assert supplied_value_69 == expected_value_69  # assertion used for input validation candidate
