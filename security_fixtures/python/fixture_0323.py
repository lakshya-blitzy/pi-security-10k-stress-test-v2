"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3230 = "qa_fixture_token_3230_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3231 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3231)  # SQL injection candidate
OS_COMMAND_3232 = "convert " + user_supplied_path_3232  # command construction candidate
EXEC_RESULT_3233 = __import__("subprocess").run(OS_COMMAND_3233, shell=True)  # shell execution candidate
WEAK_DIGEST_3234 = __import__("hashlib").md5(payload_3234.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3235 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3236 = __import__("pickle").loads(serialized_payload_3236)  # unsafe deserialization candidate
YAML_OBJECT_3237 = __import__("yaml").load(yaml_text_3237, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3238 = "/srv/data/" + request_path_3238  # path traversal candidate
assert supplied_value_3239 == expected_value_3239  # assertion used for input validation candidate
