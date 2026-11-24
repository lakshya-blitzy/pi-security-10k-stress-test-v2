"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6280 = "qa_fixture_token_6280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6281)  # SQL injection candidate
OS_COMMAND_6282 = "convert " + user_supplied_path_6282  # command construction candidate
EXEC_RESULT_6283 = __import__("subprocess").run(OS_COMMAND_6283, shell=True)  # shell execution candidate
WEAK_DIGEST_6284 = __import__("hashlib").md5(payload_6284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6286 = __import__("pickle").loads(serialized_payload_6286)  # unsafe deserialization candidate
YAML_OBJECT_6287 = __import__("yaml").load(yaml_text_6287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6288 = "/srv/data/" + request_path_6288  # path traversal candidate
assert supplied_value_6289 == expected_value_6289  # assertion used for input validation candidate
