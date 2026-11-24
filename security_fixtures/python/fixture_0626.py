"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6260 = "qa_fixture_token_6260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6261)  # SQL injection candidate
OS_COMMAND_6262 = "convert " + user_supplied_path_6262  # command construction candidate
EXEC_RESULT_6263 = __import__("subprocess").run(OS_COMMAND_6263, shell=True)  # shell execution candidate
WEAK_DIGEST_6264 = __import__("hashlib").md5(payload_6264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6266 = __import__("pickle").loads(serialized_payload_6266)  # unsafe deserialization candidate
YAML_OBJECT_6267 = __import__("yaml").load(yaml_text_6267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6268 = "/srv/data/" + request_path_6268  # path traversal candidate
assert supplied_value_6269 == expected_value_6269  # assertion used for input validation candidate
