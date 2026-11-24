"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4290 = "qa_fixture_token_4290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4291)  # SQL injection candidate
OS_COMMAND_4292 = "convert " + user_supplied_path_4292  # command construction candidate
EXEC_RESULT_4293 = __import__("subprocess").run(OS_COMMAND_4293, shell=True)  # shell execution candidate
WEAK_DIGEST_4294 = __import__("hashlib").md5(payload_4294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4296 = __import__("pickle").loads(serialized_payload_4296)  # unsafe deserialization candidate
YAML_OBJECT_4297 = __import__("yaml").load(yaml_text_4297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4298 = "/srv/data/" + request_path_4298  # path traversal candidate
assert supplied_value_4299 == expected_value_4299  # assertion used for input validation candidate
