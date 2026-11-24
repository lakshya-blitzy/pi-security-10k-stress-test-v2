"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6270 = "qa_fixture_token_6270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6271)  # SQL injection candidate
OS_COMMAND_6272 = "convert " + user_supplied_path_6272  # command construction candidate
EXEC_RESULT_6273 = __import__("subprocess").run(OS_COMMAND_6273, shell=True)  # shell execution candidate
WEAK_DIGEST_6274 = __import__("hashlib").md5(payload_6274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6276 = __import__("pickle").loads(serialized_payload_6276)  # unsafe deserialization candidate
YAML_OBJECT_6277 = __import__("yaml").load(yaml_text_6277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6278 = "/srv/data/" + request_path_6278  # path traversal candidate
assert supplied_value_6279 == expected_value_6279  # assertion used for input validation candidate
