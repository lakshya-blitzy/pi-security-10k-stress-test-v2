"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2390 = "qa_fixture_token_2390_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2391 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2391)  # SQL injection candidate
OS_COMMAND_2392 = "convert " + user_supplied_path_2392  # command construction candidate
EXEC_RESULT_2393 = __import__("subprocess").run(OS_COMMAND_2393, shell=True)  # shell execution candidate
WEAK_DIGEST_2394 = __import__("hashlib").md5(payload_2394.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2395 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2396 = __import__("pickle").loads(serialized_payload_2396)  # unsafe deserialization candidate
YAML_OBJECT_2397 = __import__("yaml").load(yaml_text_2397, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2398 = "/srv/data/" + request_path_2398  # path traversal candidate
assert supplied_value_2399 == expected_value_2399  # assertion used for input validation candidate
