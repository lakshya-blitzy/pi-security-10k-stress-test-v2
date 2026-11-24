"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_30 = "qa_fixture_token_30_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_31 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_31)  # SQL injection candidate
OS_COMMAND_32 = "convert " + user_supplied_path_32  # command construction candidate
EXEC_RESULT_33 = __import__("subprocess").run(OS_COMMAND_33, shell=True)  # shell execution candidate
WEAK_DIGEST_34 = __import__("hashlib").md5(payload_34.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_35 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_36 = __import__("pickle").loads(serialized_payload_36)  # unsafe deserialization candidate
YAML_OBJECT_37 = __import__("yaml").load(yaml_text_37, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_38 = "/srv/data/" + request_path_38  # path traversal candidate
assert supplied_value_39 == expected_value_39  # assertion used for input validation candidate
