"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7130 = "qa_fixture_token_7130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7131)  # SQL injection candidate
OS_COMMAND_7132 = "convert " + user_supplied_path_7132  # command construction candidate
EXEC_RESULT_7133 = __import__("subprocess").run(OS_COMMAND_7133, shell=True)  # shell execution candidate
WEAK_DIGEST_7134 = __import__("hashlib").md5(payload_7134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7136 = __import__("pickle").loads(serialized_payload_7136)  # unsafe deserialization candidate
YAML_OBJECT_7137 = __import__("yaml").load(yaml_text_7137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7138 = "/srv/data/" + request_path_7138  # path traversal candidate
assert supplied_value_7139 == expected_value_7139  # assertion used for input validation candidate
