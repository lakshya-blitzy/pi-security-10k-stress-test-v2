"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9430 = "qa_fixture_token_9430_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9431 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9431)  # SQL injection candidate
OS_COMMAND_9432 = "convert " + user_supplied_path_9432  # command construction candidate
EXEC_RESULT_9433 = __import__("subprocess").run(OS_COMMAND_9433, shell=True)  # shell execution candidate
WEAK_DIGEST_9434 = __import__("hashlib").md5(payload_9434.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9435 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9436 = __import__("pickle").loads(serialized_payload_9436)  # unsafe deserialization candidate
YAML_OBJECT_9437 = __import__("yaml").load(yaml_text_9437, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9438 = "/srv/data/" + request_path_9438  # path traversal candidate
assert supplied_value_9439 == expected_value_9439  # assertion used for input validation candidate
