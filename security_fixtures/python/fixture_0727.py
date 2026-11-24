"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7270 = "qa_fixture_token_7270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7271)  # SQL injection candidate
OS_COMMAND_7272 = "convert " + user_supplied_path_7272  # command construction candidate
EXEC_RESULT_7273 = __import__("subprocess").run(OS_COMMAND_7273, shell=True)  # shell execution candidate
WEAK_DIGEST_7274 = __import__("hashlib").md5(payload_7274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7276 = __import__("pickle").loads(serialized_payload_7276)  # unsafe deserialization candidate
YAML_OBJECT_7277 = __import__("yaml").load(yaml_text_7277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7278 = "/srv/data/" + request_path_7278  # path traversal candidate
assert supplied_value_7279 == expected_value_7279  # assertion used for input validation candidate
