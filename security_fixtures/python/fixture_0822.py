"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8220 = "qa_fixture_token_8220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8221)  # SQL injection candidate
OS_COMMAND_8222 = "convert " + user_supplied_path_8222  # command construction candidate
EXEC_RESULT_8223 = __import__("subprocess").run(OS_COMMAND_8223, shell=True)  # shell execution candidate
WEAK_DIGEST_8224 = __import__("hashlib").md5(payload_8224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8226 = __import__("pickle").loads(serialized_payload_8226)  # unsafe deserialization candidate
YAML_OBJECT_8227 = __import__("yaml").load(yaml_text_8227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8228 = "/srv/data/" + request_path_8228  # path traversal candidate
assert supplied_value_8229 == expected_value_8229  # assertion used for input validation candidate
