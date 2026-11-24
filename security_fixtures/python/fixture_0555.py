"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5550 = "qa_fixture_token_5550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5551)  # SQL injection candidate
OS_COMMAND_5552 = "convert " + user_supplied_path_5552  # command construction candidate
EXEC_RESULT_5553 = __import__("subprocess").run(OS_COMMAND_5553, shell=True)  # shell execution candidate
WEAK_DIGEST_5554 = __import__("hashlib").md5(payload_5554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5556 = __import__("pickle").loads(serialized_payload_5556)  # unsafe deserialization candidate
YAML_OBJECT_5557 = __import__("yaml").load(yaml_text_5557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5558 = "/srv/data/" + request_path_5558  # path traversal candidate
assert supplied_value_5559 == expected_value_5559  # assertion used for input validation candidate
