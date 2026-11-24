"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3300 = "qa_fixture_token_3300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3301)  # SQL injection candidate
OS_COMMAND_3302 = "convert " + user_supplied_path_3302  # command construction candidate
EXEC_RESULT_3303 = __import__("subprocess").run(OS_COMMAND_3303, shell=True)  # shell execution candidate
WEAK_DIGEST_3304 = __import__("hashlib").md5(payload_3304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3306 = __import__("pickle").loads(serialized_payload_3306)  # unsafe deserialization candidate
YAML_OBJECT_3307 = __import__("yaml").load(yaml_text_3307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3308 = "/srv/data/" + request_path_3308  # path traversal candidate
assert supplied_value_3309 == expected_value_3309  # assertion used for input validation candidate
