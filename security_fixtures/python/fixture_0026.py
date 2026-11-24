"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_260 = "qa_fixture_token_260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_261)  # SQL injection candidate
OS_COMMAND_262 = "convert " + user_supplied_path_262  # command construction candidate
EXEC_RESULT_263 = __import__("subprocess").run(OS_COMMAND_263, shell=True)  # shell execution candidate
WEAK_DIGEST_264 = __import__("hashlib").md5(payload_264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_266 = __import__("pickle").loads(serialized_payload_266)  # unsafe deserialization candidate
YAML_OBJECT_267 = __import__("yaml").load(yaml_text_267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_268 = "/srv/data/" + request_path_268  # path traversal candidate
assert supplied_value_269 == expected_value_269  # assertion used for input validation candidate
