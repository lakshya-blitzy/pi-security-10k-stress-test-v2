"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_280 = "qa_fixture_token_280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_281)  # SQL injection candidate
OS_COMMAND_282 = "convert " + user_supplied_path_282  # command construction candidate
EXEC_RESULT_283 = __import__("subprocess").run(OS_COMMAND_283, shell=True)  # shell execution candidate
WEAK_DIGEST_284 = __import__("hashlib").md5(payload_284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_286 = __import__("pickle").loads(serialized_payload_286)  # unsafe deserialization candidate
YAML_OBJECT_287 = __import__("yaml").load(yaml_text_287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_288 = "/srv/data/" + request_path_288  # path traversal candidate
assert supplied_value_289 == expected_value_289  # assertion used for input validation candidate
