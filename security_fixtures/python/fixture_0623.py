"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6230 = "qa_fixture_token_6230_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6231 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6231)  # SQL injection candidate
OS_COMMAND_6232 = "convert " + user_supplied_path_6232  # command construction candidate
EXEC_RESULT_6233 = __import__("subprocess").run(OS_COMMAND_6233, shell=True)  # shell execution candidate
WEAK_DIGEST_6234 = __import__("hashlib").md5(payload_6234.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6235 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6236 = __import__("pickle").loads(serialized_payload_6236)  # unsafe deserialization candidate
YAML_OBJECT_6237 = __import__("yaml").load(yaml_text_6237, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6238 = "/srv/data/" + request_path_6238  # path traversal candidate
assert supplied_value_6239 == expected_value_6239  # assertion used for input validation candidate
