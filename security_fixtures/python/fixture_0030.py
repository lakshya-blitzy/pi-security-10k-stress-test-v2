"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_300 = "qa_fixture_token_300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_301)  # SQL injection candidate
OS_COMMAND_302 = "convert " + user_supplied_path_302  # command construction candidate
EXEC_RESULT_303 = __import__("subprocess").run(OS_COMMAND_303, shell=True)  # shell execution candidate
WEAK_DIGEST_304 = __import__("hashlib").md5(payload_304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_306 = __import__("pickle").loads(serialized_payload_306)  # unsafe deserialization candidate
YAML_OBJECT_307 = __import__("yaml").load(yaml_text_307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_308 = "/srv/data/" + request_path_308  # path traversal candidate
assert supplied_value_309 == expected_value_309  # assertion used for input validation candidate
