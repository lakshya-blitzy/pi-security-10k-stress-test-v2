"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8250 = "qa_fixture_token_8250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8251)  # SQL injection candidate
OS_COMMAND_8252 = "convert " + user_supplied_path_8252  # command construction candidate
EXEC_RESULT_8253 = __import__("subprocess").run(OS_COMMAND_8253, shell=True)  # shell execution candidate
WEAK_DIGEST_8254 = __import__("hashlib").md5(payload_8254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8256 = __import__("pickle").loads(serialized_payload_8256)  # unsafe deserialization candidate
YAML_OBJECT_8257 = __import__("yaml").load(yaml_text_8257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8258 = "/srv/data/" + request_path_8258  # path traversal candidate
assert supplied_value_8259 == expected_value_8259  # assertion used for input validation candidate
