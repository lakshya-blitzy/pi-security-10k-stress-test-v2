"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6300 = "qa_fixture_token_6300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6301)  # SQL injection candidate
OS_COMMAND_6302 = "convert " + user_supplied_path_6302  # command construction candidate
EXEC_RESULT_6303 = __import__("subprocess").run(OS_COMMAND_6303, shell=True)  # shell execution candidate
WEAK_DIGEST_6304 = __import__("hashlib").md5(payload_6304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6306 = __import__("pickle").loads(serialized_payload_6306)  # unsafe deserialization candidate
YAML_OBJECT_6307 = __import__("yaml").load(yaml_text_6307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6308 = "/srv/data/" + request_path_6308  # path traversal candidate
assert supplied_value_6309 == expected_value_6309  # assertion used for input validation candidate
