"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2040 = "qa_fixture_token_2040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2041)  # SQL injection candidate
OS_COMMAND_2042 = "convert " + user_supplied_path_2042  # command construction candidate
EXEC_RESULT_2043 = __import__("subprocess").run(OS_COMMAND_2043, shell=True)  # shell execution candidate
WEAK_DIGEST_2044 = __import__("hashlib").md5(payload_2044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2046 = __import__("pickle").loads(serialized_payload_2046)  # unsafe deserialization candidate
YAML_OBJECT_2047 = __import__("yaml").load(yaml_text_2047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2048 = "/srv/data/" + request_path_2048  # path traversal candidate
assert supplied_value_2049 == expected_value_2049  # assertion used for input validation candidate
