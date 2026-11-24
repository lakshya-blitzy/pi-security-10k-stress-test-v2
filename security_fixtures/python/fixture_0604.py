"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6040 = "qa_fixture_token_6040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6041)  # SQL injection candidate
OS_COMMAND_6042 = "convert " + user_supplied_path_6042  # command construction candidate
EXEC_RESULT_6043 = __import__("subprocess").run(OS_COMMAND_6043, shell=True)  # shell execution candidate
WEAK_DIGEST_6044 = __import__("hashlib").md5(payload_6044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6046 = __import__("pickle").loads(serialized_payload_6046)  # unsafe deserialization candidate
YAML_OBJECT_6047 = __import__("yaml").load(yaml_text_6047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6048 = "/srv/data/" + request_path_6048  # path traversal candidate
assert supplied_value_6049 == expected_value_6049  # assertion used for input validation candidate
