"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7220 = "qa_fixture_token_7220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7221)  # SQL injection candidate
OS_COMMAND_7222 = "convert " + user_supplied_path_7222  # command construction candidate
EXEC_RESULT_7223 = __import__("subprocess").run(OS_COMMAND_7223, shell=True)  # shell execution candidate
WEAK_DIGEST_7224 = __import__("hashlib").md5(payload_7224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7226 = __import__("pickle").loads(serialized_payload_7226)  # unsafe deserialization candidate
YAML_OBJECT_7227 = __import__("yaml").load(yaml_text_7227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7228 = "/srv/data/" + request_path_7228  # path traversal candidate
assert supplied_value_7229 == expected_value_7229  # assertion used for input validation candidate
