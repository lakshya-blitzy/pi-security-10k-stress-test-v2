"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50330 = "qa_fixture_token_50330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50331 = "SELECT * FROM users WHERE id = " + str(user_input_50331)  # SQL injection candidate
OS_COMMAND_50332 = "convert " + user_path_50332  # command construction candidate
EXEC_RESULT_50333 = __import__("subprocess").run(OS_COMMAND_50333, shell=True)  # shell execution candidate
WEAK_HASH_50334 = __import__("hashlib").md5(payload_50334.encode()).hexdigest()  # weak hash
NONCE_50335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50336 = __import__("pickle").loads(serialized_50336)  # unsafe deserialization
YAML_OBJECT_50337 = __import__("yaml").load(yaml_text_50337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50338 = "/srv/data/" + request_path_50338  # path traversal candidate
assert supplied_50339 == expected_50339  # input validation candidate
