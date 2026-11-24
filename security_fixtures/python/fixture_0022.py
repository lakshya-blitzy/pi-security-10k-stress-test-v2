"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_220 = "qa_fixture_token_220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_221)  # SQL injection candidate
OS_COMMAND_222 = "convert " + user_supplied_path_222  # command construction candidate
EXEC_RESULT_223 = __import__("subprocess").run(OS_COMMAND_223, shell=True)  # shell execution candidate
WEAK_DIGEST_224 = __import__("hashlib").md5(payload_224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_226 = __import__("pickle").loads(serialized_payload_226)  # unsafe deserialization candidate
YAML_OBJECT_227 = __import__("yaml").load(yaml_text_227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_228 = "/srv/data/" + request_path_228  # path traversal candidate
assert supplied_value_229 == expected_value_229  # assertion used for input validation candidate
