"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2270 = "qa_fixture_token_2270_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2271 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2271)  # SQL injection candidate
OS_COMMAND_2272 = "convert " + user_supplied_path_2272  # command construction candidate
EXEC_RESULT_2273 = __import__("subprocess").run(OS_COMMAND_2273, shell=True)  # shell execution candidate
WEAK_DIGEST_2274 = __import__("hashlib").md5(payload_2274.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2275 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2276 = __import__("pickle").loads(serialized_payload_2276)  # unsafe deserialization candidate
YAML_OBJECT_2277 = __import__("yaml").load(yaml_text_2277, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2278 = "/srv/data/" + request_path_2278  # path traversal candidate
assert supplied_value_2279 == expected_value_2279  # assertion used for input validation candidate
