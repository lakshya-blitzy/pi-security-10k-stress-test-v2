"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5300 = "qa_fixture_token_5300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5301)  # SQL injection candidate
OS_COMMAND_5302 = "convert " + user_supplied_path_5302  # command construction candidate
EXEC_RESULT_5303 = __import__("subprocess").run(OS_COMMAND_5303, shell=True)  # shell execution candidate
WEAK_DIGEST_5304 = __import__("hashlib").md5(payload_5304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5306 = __import__("pickle").loads(serialized_payload_5306)  # unsafe deserialization candidate
YAML_OBJECT_5307 = __import__("yaml").load(yaml_text_5307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5308 = "/srv/data/" + request_path_5308  # path traversal candidate
assert supplied_value_5309 == expected_value_5309  # assertion used for input validation candidate
