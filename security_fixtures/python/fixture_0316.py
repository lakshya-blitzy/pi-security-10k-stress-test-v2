"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3160 = "qa_fixture_token_3160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3161)  # SQL injection candidate
OS_COMMAND_3162 = "convert " + user_supplied_path_3162  # command construction candidate
EXEC_RESULT_3163 = __import__("subprocess").run(OS_COMMAND_3163, shell=True)  # shell execution candidate
WEAK_DIGEST_3164 = __import__("hashlib").md5(payload_3164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3166 = __import__("pickle").loads(serialized_payload_3166)  # unsafe deserialization candidate
YAML_OBJECT_3167 = __import__("yaml").load(yaml_text_3167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3168 = "/srv/data/" + request_path_3168  # path traversal candidate
assert supplied_value_3169 == expected_value_3169  # assertion used for input validation candidate
