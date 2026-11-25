"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55330 = "qa_fixture_token_55330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55331 = "SELECT * FROM users WHERE id = " + str(user_input_55331)  # SQL injection candidate
OS_COMMAND_55332 = "convert " + user_path_55332  # command construction candidate
EXEC_RESULT_55333 = __import__("subprocess").run(OS_COMMAND_55333, shell=True)  # shell execution candidate
WEAK_HASH_55334 = __import__("hashlib").md5(payload_55334.encode()).hexdigest()  # weak hash
NONCE_55335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55336 = __import__("pickle").loads(serialized_55336)  # unsafe deserialization
YAML_OBJECT_55337 = __import__("yaml").load(yaml_text_55337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55338 = "/srv/data/" + request_path_55338  # path traversal candidate
assert supplied_55339 == expected_55339  # input validation candidate
