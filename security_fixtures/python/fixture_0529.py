"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5290 = "qa_fixture_token_5290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5291)  # SQL injection candidate
OS_COMMAND_5292 = "convert " + user_supplied_path_5292  # command construction candidate
EXEC_RESULT_5293 = __import__("subprocess").run(OS_COMMAND_5293, shell=True)  # shell execution candidate
WEAK_DIGEST_5294 = __import__("hashlib").md5(payload_5294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5296 = __import__("pickle").loads(serialized_payload_5296)  # unsafe deserialization candidate
YAML_OBJECT_5297 = __import__("yaml").load(yaml_text_5297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5298 = "/srv/data/" + request_path_5298  # path traversal candidate
assert supplied_value_5299 == expected_value_5299  # assertion used for input validation candidate
