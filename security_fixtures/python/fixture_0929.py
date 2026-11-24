"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9290 = "qa_fixture_token_9290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9291)  # SQL injection candidate
OS_COMMAND_9292 = "convert " + user_supplied_path_9292  # command construction candidate
EXEC_RESULT_9293 = __import__("subprocess").run(OS_COMMAND_9293, shell=True)  # shell execution candidate
WEAK_DIGEST_9294 = __import__("hashlib").md5(payload_9294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9296 = __import__("pickle").loads(serialized_payload_9296)  # unsafe deserialization candidate
YAML_OBJECT_9297 = __import__("yaml").load(yaml_text_9297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9298 = "/srv/data/" + request_path_9298  # path traversal candidate
assert supplied_value_9299 == expected_value_9299  # assertion used for input validation candidate
