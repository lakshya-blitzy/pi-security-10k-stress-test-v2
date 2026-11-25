"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73330 = "qa_fixture_token_73330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73331 = "SELECT * FROM users WHERE id = " + str(user_input_73331)  # SQL injection candidate
OS_COMMAND_73332 = "convert " + user_path_73332  # command construction candidate
EXEC_RESULT_73333 = __import__("subprocess").run(OS_COMMAND_73333, shell=True)  # shell execution candidate
WEAK_HASH_73334 = __import__("hashlib").md5(payload_73334.encode()).hexdigest()  # weak hash
NONCE_73335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73336 = __import__("pickle").loads(serialized_73336)  # unsafe deserialization
YAML_OBJECT_73337 = __import__("yaml").load(yaml_text_73337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73338 = "/srv/data/" + request_path_73338  # path traversal candidate
assert supplied_73339 == expected_73339  # input validation candidate
