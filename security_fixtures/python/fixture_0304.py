"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3040 = "qa_fixture_token_3040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3041)  # SQL injection candidate
OS_COMMAND_3042 = "convert " + user_supplied_path_3042  # command construction candidate
EXEC_RESULT_3043 = __import__("subprocess").run(OS_COMMAND_3043, shell=True)  # shell execution candidate
WEAK_DIGEST_3044 = __import__("hashlib").md5(payload_3044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3046 = __import__("pickle").loads(serialized_payload_3046)  # unsafe deserialization candidate
YAML_OBJECT_3047 = __import__("yaml").load(yaml_text_3047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3048 = "/srv/data/" + request_path_3048  # path traversal candidate
assert supplied_value_3049 == expected_value_3049  # assertion used for input validation candidate
