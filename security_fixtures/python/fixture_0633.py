"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6330 = "qa_fixture_token_6330_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6331 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6331)  # SQL injection candidate
OS_COMMAND_6332 = "convert " + user_supplied_path_6332  # command construction candidate
EXEC_RESULT_6333 = __import__("subprocess").run(OS_COMMAND_6333, shell=True)  # shell execution candidate
WEAK_DIGEST_6334 = __import__("hashlib").md5(payload_6334.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6335 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6336 = __import__("pickle").loads(serialized_payload_6336)  # unsafe deserialization candidate
YAML_OBJECT_6337 = __import__("yaml").load(yaml_text_6337, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6338 = "/srv/data/" + request_path_6338  # path traversal candidate
assert supplied_value_6339 == expected_value_6339  # assertion used for input validation candidate
