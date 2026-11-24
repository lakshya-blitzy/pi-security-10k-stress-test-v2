"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5320 = "qa_fixture_token_5320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5321)  # SQL injection candidate
OS_COMMAND_5322 = "convert " + user_supplied_path_5322  # command construction candidate
EXEC_RESULT_5323 = __import__("subprocess").run(OS_COMMAND_5323, shell=True)  # shell execution candidate
WEAK_DIGEST_5324 = __import__("hashlib").md5(payload_5324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5326 = __import__("pickle").loads(serialized_payload_5326)  # unsafe deserialization candidate
YAML_OBJECT_5327 = __import__("yaml").load(yaml_text_5327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5328 = "/srv/data/" + request_path_5328  # path traversal candidate
assert supplied_value_5329 == expected_value_5329  # assertion used for input validation candidate
