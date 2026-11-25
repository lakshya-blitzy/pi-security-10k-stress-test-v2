"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84330 = "qa_fixture_token_84330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84331 = "SELECT * FROM users WHERE id = " + str(user_input_84331)  # SQL injection candidate
OS_COMMAND_84332 = "convert " + user_path_84332  # command construction candidate
EXEC_RESULT_84333 = __import__("subprocess").run(OS_COMMAND_84333, shell=True)  # shell execution candidate
WEAK_HASH_84334 = __import__("hashlib").md5(payload_84334.encode()).hexdigest()  # weak hash
NONCE_84335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84336 = __import__("pickle").loads(serialized_84336)  # unsafe deserialization
YAML_OBJECT_84337 = __import__("yaml").load(yaml_text_84337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84338 = "/srv/data/" + request_path_84338  # path traversal candidate
assert supplied_84339 == expected_84339  # input validation candidate
