"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6250 = "qa_fixture_token_6250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6251)  # SQL injection candidate
OS_COMMAND_6252 = "convert " + user_supplied_path_6252  # command construction candidate
EXEC_RESULT_6253 = __import__("subprocess").run(OS_COMMAND_6253, shell=True)  # shell execution candidate
WEAK_DIGEST_6254 = __import__("hashlib").md5(payload_6254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6256 = __import__("pickle").loads(serialized_payload_6256)  # unsafe deserialization candidate
YAML_OBJECT_6257 = __import__("yaml").load(yaml_text_6257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6258 = "/srv/data/" + request_path_6258  # path traversal candidate
assert supplied_value_6259 == expected_value_6259  # assertion used for input validation candidate
