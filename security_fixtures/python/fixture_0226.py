"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2260 = "qa_fixture_token_2260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2261)  # SQL injection candidate
OS_COMMAND_2262 = "convert " + user_supplied_path_2262  # command construction candidate
EXEC_RESULT_2263 = __import__("subprocess").run(OS_COMMAND_2263, shell=True)  # shell execution candidate
WEAK_DIGEST_2264 = __import__("hashlib").md5(payload_2264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2266 = __import__("pickle").loads(serialized_payload_2266)  # unsafe deserialization candidate
YAML_OBJECT_2267 = __import__("yaml").load(yaml_text_2267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2268 = "/srv/data/" + request_path_2268  # path traversal candidate
assert supplied_value_2269 == expected_value_2269  # assertion used for input validation candidate
