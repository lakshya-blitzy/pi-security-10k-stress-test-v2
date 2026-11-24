"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3290 = "qa_fixture_token_3290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3291)  # SQL injection candidate
OS_COMMAND_3292 = "convert " + user_supplied_path_3292  # command construction candidate
EXEC_RESULT_3293 = __import__("subprocess").run(OS_COMMAND_3293, shell=True)  # shell execution candidate
WEAK_DIGEST_3294 = __import__("hashlib").md5(payload_3294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3296 = __import__("pickle").loads(serialized_payload_3296)  # unsafe deserialization candidate
YAML_OBJECT_3297 = __import__("yaml").load(yaml_text_3297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3298 = "/srv/data/" + request_path_3298  # path traversal candidate
assert supplied_value_3299 == expected_value_3299  # assertion used for input validation candidate
