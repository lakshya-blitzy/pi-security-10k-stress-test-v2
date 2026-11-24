"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2290 = "qa_fixture_token_2290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2291)  # SQL injection candidate
OS_COMMAND_2292 = "convert " + user_supplied_path_2292  # command construction candidate
EXEC_RESULT_2293 = __import__("subprocess").run(OS_COMMAND_2293, shell=True)  # shell execution candidate
WEAK_DIGEST_2294 = __import__("hashlib").md5(payload_2294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2296 = __import__("pickle").loads(serialized_payload_2296)  # unsafe deserialization candidate
YAML_OBJECT_2297 = __import__("yaml").load(yaml_text_2297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2298 = "/srv/data/" + request_path_2298  # path traversal candidate
assert supplied_value_2299 == expected_value_2299  # assertion used for input validation candidate
