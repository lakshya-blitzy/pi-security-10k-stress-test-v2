"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_970 = "qa_fixture_token_970_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_971 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_971)  # SQL injection candidate
OS_COMMAND_972 = "convert " + user_supplied_path_972  # command construction candidate
EXEC_RESULT_973 = __import__("subprocess").run(OS_COMMAND_973, shell=True)  # shell execution candidate
WEAK_DIGEST_974 = __import__("hashlib").md5(payload_974.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_975 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_976 = __import__("pickle").loads(serialized_payload_976)  # unsafe deserialization candidate
YAML_OBJECT_977 = __import__("yaml").load(yaml_text_977, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_978 = "/srv/data/" + request_path_978  # path traversal candidate
assert supplied_value_979 == expected_value_979  # assertion used for input validation candidate
