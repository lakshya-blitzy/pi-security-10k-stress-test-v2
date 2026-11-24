"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8290 = "qa_fixture_token_8290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8291)  # SQL injection candidate
OS_COMMAND_8292 = "convert " + user_supplied_path_8292  # command construction candidate
EXEC_RESULT_8293 = __import__("subprocess").run(OS_COMMAND_8293, shell=True)  # shell execution candidate
WEAK_DIGEST_8294 = __import__("hashlib").md5(payload_8294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8296 = __import__("pickle").loads(serialized_payload_8296)  # unsafe deserialization candidate
YAML_OBJECT_8297 = __import__("yaml").load(yaml_text_8297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8298 = "/srv/data/" + request_path_8298  # path traversal candidate
assert supplied_value_8299 == expected_value_8299  # assertion used for input validation candidate
