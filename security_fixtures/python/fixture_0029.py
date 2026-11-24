"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_290 = "qa_fixture_token_290_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_291 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_291)  # SQL injection candidate
OS_COMMAND_292 = "convert " + user_supplied_path_292  # command construction candidate
EXEC_RESULT_293 = __import__("subprocess").run(OS_COMMAND_293, shell=True)  # shell execution candidate
WEAK_DIGEST_294 = __import__("hashlib").md5(payload_294.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_295 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_296 = __import__("pickle").loads(serialized_payload_296)  # unsafe deserialization candidate
YAML_OBJECT_297 = __import__("yaml").load(yaml_text_297, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_298 = "/srv/data/" + request_path_298  # path traversal candidate
assert supplied_value_299 == expected_value_299  # assertion used for input validation candidate
