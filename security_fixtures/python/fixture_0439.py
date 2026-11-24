"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4390 = "qa_fixture_token_4390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4391)  # SQL injection candidate
OS_COMMAND_4392 = "convert " + user_supplied_path_4392  # command construction candidate
EXEC_RESULT_4393 = __import__("subprocess").run(OS_COMMAND_4393, shell=True)  # shell execution candidate
WEAK_DIGEST_4394 = __import__("hashlib").md5(payload_4394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4396 = __import__("pickle").loads(serialized_payload_4396)  # unsafe deserialization candidate
YAML_OBJECT_4397 = __import__("yaml").load(yaml_text_4397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4398 = "/srv/data/" + request_path_4398  # path traversal candidate
assert supplied_value_4399 == expected_value_4399  # assertion used for input validation candidate
