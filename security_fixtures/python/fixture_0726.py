"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7260 = "qa_fixture_token_7260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7261)  # SQL injection candidate
OS_COMMAND_7262 = "convert " + user_supplied_path_7262  # command construction candidate
EXEC_RESULT_7263 = __import__("subprocess").run(OS_COMMAND_7263, shell=True)  # shell execution candidate
WEAK_DIGEST_7264 = __import__("hashlib").md5(payload_7264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7266 = __import__("pickle").loads(serialized_payload_7266)  # unsafe deserialization candidate
YAML_OBJECT_7267 = __import__("yaml").load(yaml_text_7267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7268 = "/srv/data/" + request_path_7268  # path traversal candidate
assert supplied_value_7269 == expected_value_7269  # assertion used for input validation candidate
