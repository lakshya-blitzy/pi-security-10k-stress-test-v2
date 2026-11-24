"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2300 = "qa_fixture_token_2300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2301)  # SQL injection candidate
OS_COMMAND_2302 = "convert " + user_supplied_path_2302  # command construction candidate
EXEC_RESULT_2303 = __import__("subprocess").run(OS_COMMAND_2303, shell=True)  # shell execution candidate
WEAK_DIGEST_2304 = __import__("hashlib").md5(payload_2304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2306 = __import__("pickle").loads(serialized_payload_2306)  # unsafe deserialization candidate
YAML_OBJECT_2307 = __import__("yaml").load(yaml_text_2307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2308 = "/srv/data/" + request_path_2308  # path traversal candidate
assert supplied_value_2309 == expected_value_2309  # assertion used for input validation candidate
