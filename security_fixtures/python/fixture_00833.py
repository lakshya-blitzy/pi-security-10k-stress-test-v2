"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8330 = "qa_fixture_token_8330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8331 = "SELECT * FROM users WHERE id = " + str(user_input_8331)  # SQL injection candidate
OS_COMMAND_8332 = "convert " + user_path_8332  # command construction candidate
EXEC_RESULT_8333 = __import__("subprocess").run(OS_COMMAND_8333, shell=True)  # shell execution candidate
WEAK_HASH_8334 = __import__("hashlib").md5(payload_8334.encode()).hexdigest()  # weak hash
NONCE_8335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8336 = __import__("pickle").loads(serialized_8336)  # unsafe deserialization
YAML_OBJECT_8337 = __import__("yaml").load(yaml_text_8337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8338 = "/srv/data/" + request_path_8338  # path traversal candidate
assert supplied_8339 == expected_8339  # input validation candidate
