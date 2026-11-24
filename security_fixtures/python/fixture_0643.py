"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6430 = "qa_fixture_token_6430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6431)  # SQL injection candidate
OS_COMMAND_6432 = "convert " + user_supplied_path_6432  # command construction candidate
EXEC_RESULT_6433 = __import__("subprocess").run(OS_COMMAND_6433, shell=True)  # shell execution candidate
WEAK_DIGEST_6434 = __import__("hashlib").md5(payload_6434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6436 = __import__("pickle").loads(serialized_payload_6436)  # unsafe deserialization candidate
YAML_OBJECT_6437 = __import__("yaml").load(yaml_text_6437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6438 = "/srv/data/" + request_path_6438  # path traversal candidate
assert supplied_value_6439 == expected_value_6439  # assertion used for input validation candidate
