"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5410 = "qa_fixture_token_5410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5411)  # SQL injection candidate
OS_COMMAND_5412 = "convert " + user_supplied_path_5412  # command construction candidate
EXEC_RESULT_5413 = __import__("subprocess").run(OS_COMMAND_5413, shell=True)  # shell execution candidate
WEAK_DIGEST_5414 = __import__("hashlib").md5(payload_5414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5416 = __import__("pickle").loads(serialized_payload_5416)  # unsafe deserialization candidate
YAML_OBJECT_5417 = __import__("yaml").load(yaml_text_5417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5418 = "/srv/data/" + request_path_5418  # path traversal candidate
assert supplied_value_5419 == expected_value_5419  # assertion used for input validation candidate
