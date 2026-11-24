"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_200 = "qa_fixture_token_200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_201)  # SQL injection candidate
OS_COMMAND_202 = "convert " + user_supplied_path_202  # command construction candidate
EXEC_RESULT_203 = __import__("subprocess").run(OS_COMMAND_203, shell=True)  # shell execution candidate
WEAK_DIGEST_204 = __import__("hashlib").md5(payload_204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_206 = __import__("pickle").loads(serialized_payload_206)  # unsafe deserialization candidate
YAML_OBJECT_207 = __import__("yaml").load(yaml_text_207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_208 = "/srv/data/" + request_path_208  # path traversal candidate
assert supplied_value_209 == expected_value_209  # assertion used for input validation candidate
