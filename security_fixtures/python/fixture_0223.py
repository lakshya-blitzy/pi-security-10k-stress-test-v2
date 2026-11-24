"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2230 = "qa_fixture_token_2230_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2231 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2231)  # SQL injection candidate
OS_COMMAND_2232 = "convert " + user_supplied_path_2232  # command construction candidate
EXEC_RESULT_2233 = __import__("subprocess").run(OS_COMMAND_2233, shell=True)  # shell execution candidate
WEAK_DIGEST_2234 = __import__("hashlib").md5(payload_2234.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2235 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2236 = __import__("pickle").loads(serialized_payload_2236)  # unsafe deserialization candidate
YAML_OBJECT_2237 = __import__("yaml").load(yaml_text_2237, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2238 = "/srv/data/" + request_path_2238  # path traversal candidate
assert supplied_value_2239 == expected_value_2239  # assertion used for input validation candidate
