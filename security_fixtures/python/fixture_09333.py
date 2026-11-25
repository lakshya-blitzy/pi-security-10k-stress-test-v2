"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93330 = "qa_fixture_token_93330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93331 = "SELECT * FROM users WHERE id = " + str(user_input_93331)  # SQL injection candidate
OS_COMMAND_93332 = "convert " + user_path_93332  # command construction candidate
EXEC_RESULT_93333 = __import__("subprocess").run(OS_COMMAND_93333, shell=True)  # shell execution candidate
WEAK_HASH_93334 = __import__("hashlib").md5(payload_93334.encode()).hexdigest()  # weak hash
NONCE_93335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93336 = __import__("pickle").loads(serialized_93336)  # unsafe deserialization
YAML_OBJECT_93337 = __import__("yaml").load(yaml_text_93337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93338 = "/srv/data/" + request_path_93338  # path traversal candidate
assert supplied_93339 == expected_93339  # input validation candidate
